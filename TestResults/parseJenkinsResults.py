from datetime import datetime
from jenkinsapi.jenkins import Jenkins, JenkinsAPIException
from toolkit.sqlTools import venafiTesting as VT
import requests
from lxml.etree import HTML
import traceback
import keyring
import os, sys
from dateutil import parser
import re
import json


class JobTypes:
    tpp_auto = 'TPP_Auto'
    tpp_auto_prod = 'TPP_Auto_Prod'
    integration = 'TPP_Integration'


CURRENT_RELEASE = '19.4'
NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
JOBS = [
    # {'url': 'https://jenkins.eng.venafi.com/job/TPP_Auto_Prod/view/Server%20Cert', 'type': JobTypes.tpp_auto_prod},
    # {'url': 'https://jenkins.eng.venafi.com/view/TPP_Auto/job/TPP_Auto/', 'type': JobTypes.tpp_auto},
    {'url': 'https://jenkins.eng.venafi.com/job/TPP_Build_Dev/job/TPP_Integration', 'type': JobTypes.integration}
]

BLACKLISTED_JOBS = [
    'Aggregate_Test_Results',
    'AWS_RDS_Smoke',
    'Multi_Env',
    'Single_Env',
    'TestDiscoveryReport',
    'Trigger',
    'Prod_Dashboard_License_counts',
    'Prod_ApertureUI_SystemDashboard',
    'Prod_Dashboard_Ssl',
    'TPP_Integration_Tests_17.3',
    'TPP_Integration_Tests_17.4',
    'TPP_Integration_Tests_18.1',
    'TPP_Integration_Tests_18.2',
    'TPP_Integration_Tests_18.3',
    'TPP_Integration_Tests_18.4',
    'TPP_Integration_Tests_19.1',
    'TPP_Integration_Tests_19.2',
    'TPP_Integration_Tests_19.3',
    'TPP_Integration_Tests_Branches'
]


class JenkinsTestCase:
    def __init__(self, job, case):
        """
        :type job: JenkinsJob
        """
        self.age = case.get('age')
        self.className = case.get('className')
        self.duration = case.get('duration')
        self.errorDetails = case.get('errorDetails')
        self.errorStackTrace = case.get('errorStackTrace')
        self.failedSince = case.get('failedSince')
        self.name = case.get('name')

        self.skipped = case.get('skipped')
        self.skippedMessage = case.get('skippedMessage')
        self.status = case.get('status')
        self.stderr = case.get('stderr')
        self.stdout = case.get('stdout')
        self.testActions = case.get('testActions')

        if job.python_test_collection:
            partial_path = self.className.replace('.', '.py::')
            annotations = [a for a in job.python_test_collection if partial_path in a.get('path')]
            annotations = annotations[0] if len(annotations) > 0 else {}
        else:
            annotations = {}
        self.owner = annotations.get('owner', 'Unassigned')
        self.feature = annotations.get('feature', 'Unknown')


class JenkinsJob:
    def __init__(self, build_data, job_type):
        self.jobName = build_data.job.name
        self.buildNo = build_data.buildno
        self.result_set = build_data.get_resultset()._data  # This contains test data
        self.timestamp = build_data.get_timestamp()
        self.params = build_data.get_params()
        self.passed = self.result_set.get('passCount', -1)
        self.failed = self.result_set.get('failCount', -1)
        self.skipped = self.result_set.get('skipCount', -1)
        self.duration = build_data.get_duration()
        self.gitBranch = build_data.get_actions()['buildsByBranchName'].keys()[0]

        try:
            artifacts = build_data.get_artifact_dict()
            ptc = artifacts.get('test_collection.json') if artifacts else None
            self.python_test_collection = json.loads(ptc.get_data()) if ptc else None
        except:
            self.python_test_collection = None

        if job_type == JobTypes.tpp_auto_prod:
            self.env_vars = build_data.get_env_vars()  # Here are the ENV variables set on the job.
            self.build = self.env_vars.get('TPP_BUILD_TIMESTAMP', 'Unknown')
            self.releaseVersion = self.params.get('CURRENT_BRANCH', 'Unknown').split('+')[0]

        elif job_type == JobTypes.tpp_auto:
            self.env_vars = {}
            self.releaseVersion = self.params.get('VERSION')
            self.build = self.params.get('BUILD_DIR')

        elif job_type == JobTypes.integration:
            self.env_vars = {}
            self.releaseVersion = self.params.get('TPP_BRANCH', '')
            self.build = self.params.get('BUILDSYSTEM_BRANCH', '')


class BuildBot:
    server = "192.168.6.137"
    url = "http://{server}/builders/TPP_{release}_TestBuild_Integration_W2012".format(
        server=server,
        release=CURRENT_RELEASE
    )


class LogTypes:
    error = 'ERROR'
    info = 'INFO'


class UpdateTestResults:
    def __init__(self, framework):
        if not isinstance(framework, VT.Frameworks):
            raise TypeError('UpdateTestResults requires a venafiTesting.Frameworks object.')
        self.FrameworksTable = framework

        self.RunsTable = VT.Runs()
        # self.StatesTable = VT.States()
        self.JobsTable = VT.Jobs()
        self.JobHistoryTable = VT.JobHistory()
        self.TestsTable = VT.Tests()
        self.TestHistoryTable = VT.TestHistory()

        self.jobs = None
        self.new_jobs_exist = False

    def log(self, text, log_type=LogTypes.info):
        if log_type == LogTypes.error:
            log_dir = os.path.abspath(r'.\ErrorLogs')
            timestamp = parser.parse(NOW).strftime('%Y%m%d%H%M%S')
            filename = os.path.abspath(r'%s\output_%s.txt' % (log_dir, timestamp))
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            with open(filename, 'w') as f:
                text = ">>>>>>>>>> %s <<<<<<<<<<\n%s\n--\n" % (log_type, text)
                f.write(text)
        print(text)

    def get_jenkins_jobs(self, url, username, password):
        if not username.startswith('ENG\\'):
            username = r'ENG\%s' % username
        try:
            return Jenkins(
                baseurl=url,
                username=username,
                password=password,
                timeout=180
            ).get_jobs()

        except Exception as e:
            self.log(e, LogTypes.error)
            raise AssertionError('No jobs found at %s!' % url)

    def create_and_load_runs_record(self):
        self.RunsTable.insert_sql_cmd(
            newJobs=0,
            newTests=0,
            created=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        self.RunsTable.load()

    def parse_jenkins_jobs(self, job_url, job_type, username, password):
        self.jobs = self.get_jenkins_jobs(url=job_url, username=username, password=password)

        already_seen = []

        for job in self.jobs:
            job_details = job[1]
            if job_details.name in already_seen or job_details.name in BLACKLISTED_JOBS:
                continue

            already_seen.append(job_details.name)

            try:
                # Load the latest build information for this Job
                latest_build = job_details.get_last_completed_build()
                if not latest_build.has_resultset():
                    self.log('Build number "%s" for "%s" does not yet have any published results. Skipping.' % (latest_build.buildno, job_details.name))
                    continue

                try:
                    self.JobsTable.load(frameworkId=self.FrameworksTable.frameworkId, name=job_details.name)
                    if self.JobsTable.lastBuildNo >= latest_build.buildno:
                        self.log('Build number "%s" for "%s" has already been recorded. Skipping.' % (latest_build.buildno, job_details.name))
                        continue
                    self.log('Updating %s to build number %s' % (job_details.name, latest_build.buildno))
                    self.JobsTable.update_last_updated(lastUpdated=NOW, lastBuildNo=latest_build.buildno)

                except AssertionError:
                    self.log('No job recorded for %s' % job_details.name)
                    self.JobsTable.insert_sql_cmd(
                        name=job_details.name,
                        frameworkId=self.FrameworksTable.frameworkId,
                        created=NOW,
                        lastUpdated=NOW,
                        lastBuildNo=latest_build.buildno
                    )

                except Exception:
                    self.log(traceback.format_exc(), LogTypes.error)
                    continue

                if not self.new_jobs_exist:
                    self.new_jobs_exist = True
                    self.create_and_load_runs_record()

                job_props = JenkinsJob(latest_build, job_type)

                self.JobHistoryTable.insert_sql_cmd(
                    jobId=self.JobsTable.jobId,
                    runId=self.RunsTable.runId,
                    buildNo=latest_build.buildno,
                    build=job_props.build,
                    releaseVersion=job_props.releaseVersion,
                    gitBranch=job_props.gitBranch,
                    totalTests=job_props.passed + job_props.failed,
                    passed=job_props.passed,
                    failed=job_props.failed,
                    skipped=job_props.skipped,
                    lapse=job_props.duration.seconds
                )

                for suite in job_props.result_set.get('suites', []):
                    for c in suite.get('cases', []):
                        case = JenkinsTestCase(job_props, c)
                        if case.status == 'SKIPPED': continue
                        try:
                            # Load test if it exists, else create it
                            try:
                                self.TestsTable.load(className=case.className, testName=case.name, jobId=self.JobsTable.jobId)
                                self.log('Updating test %s (testId: %s)' % (case.name, self.TestsTable.testId))
                                self.TestsTable.update_last_updated(when=NOW)
                            except AssertionError as a:
                                self.log(a)
                                self.TestsTable.insert_sql_cmd(
                                    jobId=self.JobsTable.jobId,
                                    className=case.className,
                                    testName=case.name,
                                    feature=case.feature,
                                    owner=case.owner,
                                    lastUpdated=NOW,
                                    created=NOW
                                )
                            except Exception:
                                self.log(traceback.format_exc(), LogTypes.error)
                                continue

                            if self.TestsTable.feature != case.feature:
                                self.TestsTable.update_feature(case.feature)

                            if self.TestsTable.owner != case.owner:
                                self.TestsTable.update_owner(case.owner)

                            # Set resolution and reason
                            if case.status in ['PASSED', 'FIXED']:
                                resolution = 'n/a'
                                reason = 'n/a'
                                status = 'PASSED'
                            elif case.errorDetails or case.errorStackTrace:
                                resolution = self.TestHistoryTable.get_last_resolution(testId=self.TestsTable.testId) or 'Undetermined'
                                reason = case.errorDetails
                                status = 'FAILED'
                            else:
                                resolution = 'Undetermined'
                                reason = 'Unknown'
                                status = 'FAILED'

                            self.TestHistoryTable.insert_sql_cmd(
                                testId=self.TestsTable.testId,
                                runId=self.RunsTable.runId,
                                testResult=status,
                                reason=reason,
                                age=case.age,
                                resolution=resolution,
                                lapse=case.duration
                            )

                        except Exception as e:
                            if 'Cannot insert duplicate key row' in e.message:
                                self.log('Skipping duplicated record.', LogTypes.info)
                            else:
                                self.log(traceback.format_exc(), LogTypes.error)
            except JenkinsAPIException:
                continue
            except Exception as e:
                if 'Cannot insert duplicate key row' in e.message:
                    self.log('Skipping duplicated record.', LogTypes.info)
                else:
                    self.log(traceback.format_exc(), LogTypes.error)

    def parse_buildbot_integration_tests(self):
        try:
            self.JobsTable.load(frameworkId=self.FrameworksTable.frameworkId, name='BuildBot')
        except:
            self.JobsTable.insert_sql_cmd(
                name='BuildBot',
                frameworkId=self.FrameworksTable.frameworkId,
                created=NOW,
                lastUpdated=NOW,
                lastBuildNo=0
            )

        # latest_build = self.get_latest_build(update_build_record=False)
        latest_build = self.get_integration_build(build_number=2, update_build_record=False)

        try:
            build_info = self.get_integration_build(latest_build['number'])

            if not build_info['has_logs']:
                print('Build unavailable for %s.' % build_info['url'])
                return

            if build_info['number'] == self.JobsTable.lastBuildNo:
                self.log('Already seen this job. Skipping.')
                return

            self.parse_and_insert_results(build_info['content'], build_info['url'])
        except Exception as e:
            self.log(traceback.format_exc(), LogTypes.error)

    def get_latest_build(self, update_build_record=True):
        return self.get_integration_build(update_build_record=update_build_record)

    def get_integration_build(self, build_number=None, update_build_record=True):
        resp = requests.get(BuildBot.url)
        parsed_html = HTML(resp.content)
        if not build_number:
            latest_build = parsed_html.xpath('//*[@id="builds"]/descendant::a[1]/@href')[0]
            build_number = parsed_html.xpath('//*[@id="builds"]/descendant::a[1]/text()')[0].strip('#')
            build_url = latest_build.replace('../builders', 'http://%s/builders' % BuildBot.server) + "/steps/Test%20Integration%20MSSQL/logs/stdio/text"
        else:
            build_url = "{u}/builds/{n}/steps/Test%20Integration%20MSSQL/logs/stdio/text".format(u=BuildBot.url, n=build_number)

        resp = requests.get(build_url)

        if update_build_record is True:
            self.JobsTable.update_last_updated(lastUpdated=NOW, lastBuildNo=build_number)

        # Does this build have integration results?
        try:
            logs_exist = not "404" in HTML(resp.content).xpath('//title/text()')[0]
        except IndexError:
            logs_exist = True
        if not logs_exist:
            self.log("No logs exist for build number %s" % build_number)

        build_info = {
            'content': resp.content,
            'url': build_url,
            'number': int(build_number),
            'has_logs': logs_exist
        }
        return build_info

    def parse_and_insert_results(self, text, url):
        if not self.new_jobs_exist:
            self.new_jobs_exist = True
            self.create_and_load_runs_record()

        pass_flag = False
        fail_flag = False
        pass_count = 0
        skip_count = 0
        fail_count = 0

        job_history_lapse = ""
        job_start_time = ""
        job_end_time = ""
        releaseVersion = CURRENT_RELEASE
        owner = "Unassigned"
        gitBranch = ""
        build = ""

        test_duration = 0
        test = ""
        status = ""
        resolution = ""
        reason = ""
        age = 0


        for line in text.split('\n'):
            try:
                # Test Exectution Date and Time
                if line.startswith("Tests Start: "):
                    if not job_start_time:
                        job_start_time = line.split("Tests Start: ")[-1]
                    continue

                elif line.startswith("Tests End: "):
                    job_end_time = line.split("Tests End: ")[-1]
                    continue

                # Tests that failed.
                elif re.match(pattern='^Failed *Venafi.Test', string=line):
                    fail_count += 1
                    test = line.split('Failed', 1)[1].strip()
                    status = 'FAILED'
                    fail_flag = True
                    self.log(job_start_time)
                    self.log('PASSED: ' + test)
                    continue

                elif fail_flag is True and line.startswith('[duration]'):
                    fail_flag = False
                    lapse = line.split('=')[1].strip()
                    test_duration = datetime.strptime(lapse.split('.')[0], '%H:%M:%S').second

                elif fail_flag is True:
                    reason += line
                    self.log(reason)
                    continue

                # Tests that are disabled.
                elif line.startswith('Warning: The disabled test'):
                    continue
                    # skip_count += 1
                    # test = line.split("'")[1]
                    # status = 'SKIPPED'

                # Tests that passed.
                elif re.match(pattern='^Passed *Venafi.Test', string=line):
                    pass_count += 1
                    test = line.split('Passed', 1)[1].strip()
                    status = 'PASSED'
                    pass_flag = True
                    self.log(job_start_time)
                    self.log(test)
                    continue

                elif pass_flag is True and line.startswith('[duration]'):
                    pass_flag = False
                    lapse = line.split('=')[1].strip()
                    test_duration = datetime.strptime(lapse.split('.')[0], '%H:%M:%S').second

                else:
                    continue


                # Load test if it exists, else create it
                try:
                    self.TestsTable.load(className='nightlyTPP', testName=test, jobId=self.JobsTable.jobId)
                    self.log('Updating test %s' % test)
                    self.TestsTable.update_last_updated(when=NOW)
                except AssertionError:
                    self.log('Test "%s" not found. Adding it.' % test)
                    self.TestsTable.insert_sql_cmd(
                        jobId=self.JobsTable.jobId,
                        className='nightlyTPP',
                        testName=test,
                        feature='Unknown',
                        owner='Unassigned',
                        lastUpdated=NOW,
                        created=NOW
                    )
                except:
                    self.log(traceback.format_exc(), LogTypes.error)
                    continue

                current_age = 0
                try:
                    self.TestHistoryTable.load_most_recent_test(testId=self.TestsTable.testId)
                    current_age = self.TestHistoryTable.age
                except ValueError:
                    pass
                except:
                    self.log(traceback.format_exc(), LogTypes.error)

                # Set resolution and reason
                if status in ['PASSED', 'FIXED']:
                    pass_count += 1
                    resolution = 'n/a'
                    reason = 'n/a'
                    status = 'PASSED'
                    new_age = 0

                elif status == 'SKIPPED':
                #     skip_count += 1
                #     resolution = 'Skipped'
                #     reason = 'Unknown'
                #     status = 'SKIPPED'
                #     new_age = current_age + 1
                    continue

                elif status == 'FAILED' or reason:
                    fail_count += 1
                    resolution = self.TestHistoryTable.get_last_resolution(testId=self.TestsTable.testId) or 'Undetermined'
                    status = 'FAILED'
                    new_age = current_age + 1

                else:
                    resolution = 'Undetermined'
                    reason = 'Unknown'
                    status = 'FAILED'
                    new_age = current_age + 1

                self.TestHistoryTable.insert_sql_cmd(
                    testId=self.TestsTable.testId,
                    runId=self.RunsTable.runId,
                    testResult=status,
                    reason=reason,
                    age=new_age,
                    resolution=resolution,
                    lapse=test_duration
                )
                # Reset all of the tracking variables
                test_duration = 0
                test = ""
                status = ""
                resolution = ""
                reason = ""
                age = 0
            except Exception as e:
                if 'Cannot insert duplicate key row' in e.message:
                    self.log('Skipping duplicated record.', LogTypes.info)
                else:
                    self.log(traceback.format_exc(), LogTypes.error)

        # Insert JobHistory record.
        build_overview_url = url.split('/steps')[0]
        resp = requests.get(build_overview_url)
        parsed_html = HTML(resp.content)
        build_properties = lambda x: parsed_html.xpath('//*[text() = "%s"]/following-sibling::td[1]/text()' % x)[0]
        buildNo = build_properties('buildnumber')
        build = build_properties('DistributeDatedFolder')
        elapsed = build_properties('Elapsed')
        lapse = 0
        for y in elapsed.split(','):
            if 'hr' in y:
                lapse += int(y.split()[0]) * 3600
            elif 'min' in y:
                lapse += int(y.split()[0]) * 60
            elif 'sec' in y:
                lapse += int(y.split()[0])
        gb = build_properties('branches_TPP')
        try:
            gitBranches = '|'.join(eval(gb))
        except:
            gitBranches = gb

        try:
            self.JobHistoryTable.insert_sql_cmd(
                jobId=self.JobsTable.jobId,
                runId=self.RunsTable.runId,
                buildNo=buildNo,
                build=build,
                releaseVersion=CURRENT_RELEASE,
                gitBranch=gitBranches,
                totalTests=pass_count + fail_count,
                passed=pass_count,
                failed=fail_count,
                skipped=skip_count,
                lapse=lapse
            )
        except Exception as e:
            if 'Cannot insert duplicate key row' in e.message:
                self.log('Skipping duplicated record.', LogTypes.info)
            else:
                self.log(traceback.format_exc(), LogTypes.error)


def main():
    username = 'tyler.spens'
    password = keyring.get_password('ENG', username)
    if not password:
        raise ValueError('Cannot retrieve password. Be sure to set password using '
                         'keyring.set_password("ENG", <first.last>, <password>) in a python console on this machine.')

    python_framework = VT.Frameworks()
    integration_framework = VT.Frameworks()

    utr = UpdateTestResults(
        framework=python_framework
    )

    for job in JOBS:
        ############### Integration Framework ################
        if job['type'] == JobTypes.integration:
            integration_framework.load_framework('Integration')
            integration_framework.update_sql_cmd(lastUpdated=NOW)
            utr.FrameworksTable = integration_framework
            
        ############### Python Framework ################
        elif job['type'] in [JobTypes.tpp_auto, JobTypes.tpp_auto_prod]:
            python_framework.load_framework('Python')
            python_framework.update_sql_cmd(lastUpdated=NOW)
            utr.FrameworksTable = python_framework

        utr.parse_jenkins_jobs(job['url'], job['type'], username, password)


    ############### DEPRECATED: Buildbot and the Integration Framework ################
    # integration_framework = VT.Frameworks()
    # integration_framework.load_framework('Integration')
    # integration_framework.update_sql_cmd(lastUpdated=NOW)
    # utr.FrameworksTable = integration_framework
    # utr.parse_buildbot_integration_tests()


if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print('THIS SCRIPT TOOK ' + str(finish - start).split('.')[0] + ' TO COMPLETE.')