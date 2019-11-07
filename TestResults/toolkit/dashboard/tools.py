from toolkit.sqlTools import venafiTesting as VT
from toolkit.sqlTools.sqlHelper import SQLCommandBuilder as sql, quote
from datetime import datetime
from dateutil.parser import parser


def get_frameworks(frameworkNames=None):
    if frameworkNames and not isinstance(frameworkNames, list):
        frameworkNames = [frameworkNames]

    FrameworksTable = VT.Frameworks()
    if frameworkNames:
        sqlCmd = sql().Select(['DISTINCT *']) \
                      .From(FrameworksTable.tableName) \
                      .Where([FrameworksTable.Columns.name.In([quote(f) for f in frameworkNames])]) \
                      .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']).From(FrameworksTable.tableName).sqltext

    all_fws = FrameworksTable.query(sqlCmd).execute()
    return all_fws or {}

def get_jobs(frameworkIds=None):
    if frameworkIds and not isinstance(frameworkIds, list):
        frameworkIds = [frameworkIds]

    JobsTable = VT.Jobs()
    if frameworkIds:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([JobsTable.tableName]) \
             .Where([JobsTable.Columns.frameworkId.In(frameworkIds)]) \
             .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']) \
                      .From([JobsTable.tableName]) \
                      .sqltext
    jobs = JobsTable.query(sqlCmd).execute()
    return jobs or {}

def get_tests(jobIds=None):
    if jobIds and not isinstance(jobIds, list):
        jobIds = [jobIds]

    TestsTable = VT.Tests()
    if jobIds:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([TestsTable.tableName]) \
             .Where([TestsTable.Columns.jobId.In(jobIds)]) \
             .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']) \
                      .From([TestsTable.tableName]) \
                      .sqltext
    tests = TestsTable.query(sqlCmd).execute()
    return tests or {}

def get_runs(startDate=None, endDate=None):
    RunsTable = VT.Runs()
    if startDate and endDate:
        fmt = lambda x, y: datetime.strftime(parser().parse(x), y)
        startDate = fmt(startDate, '%Y-%m-%d 00:00:00')
        endDate = fmt(endDate, '%Y-%m-%d 23:59:59')
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([RunsTable.tableName]) \
             .Where([RunsTable.Columns.created.Between(quote(startDate), quote(endDate))]) \
             .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']) \
                      .From([RunsTable.tableName]) \
                      .sqltext
    runs = RunsTable.query(sqlCmd).execute()
    return runs or {}

def get_job_history(jobIds, runIds=None):
    if not isinstance(jobIds, list):
        jobIds  = [jobIds]

    if runIds and not isinstance(runIds, list):
        runIds = [runIds]

    JobHistoryTable = VT.JobHistory()
    if runIds:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([JobHistoryTable.tableName]) \
             .Where([
                    sql.And([
                        JobHistoryTable.Columns.jobId.In(jobIds),
                        JobHistoryTable.Columns.runId.In(runIds)
                    ])
                ]) \
             .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([JobHistoryTable.tableName]) \
             .Where([
                    sql.And([
                        JobHistoryTable.Columns.jobId.In(jobIds)
                    ])
                ]) \
             .sqltext
    jobs = JobHistoryTable.query(sqlCmd).execute()
    return jobs or {}

def get_test_history(testIds, runIds=None):
    if not isinstance(testIds, list):
        testIds = [testIds]

    if runIds and not isinstance(runIds, list):
        runIds = [runIds]

    TestHistoryTable = VT.TestHistory()
    if runIds:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([TestHistoryTable.tableName]) \
             .Where([
                    sql.And([
                        TestHistoryTable.Columns.testId.In(testIds),
                        TestHistoryTable.Columns.runId.In(runIds)
                    ])
                ]) \
             .sqltext
    else:
        sqlCmd = sql().Select(['DISTINCT *']) \
             .From([TestHistoryTable.tableName]) \
             .Where([
                    sql.And([
                        TestHistoryTable.Columns.testId.In(testIds)
                    ])
                ]) \
             .sqltext
    tests = TestHistoryTable.query(sqlCmd).execute()
    return tests or {}


def  update_test_history_resolution(testIds, runIds, resolution):
    TH = VT.TestHistory()
    try:
        TH.update_resolution_for_many_tests(testIds, runIds, resolution)
        return True
    except:
        return False


def get_all_view(startDate, endDate, frameworkNames=None, latest_result_only=False, failures_only=False):
    if frameworkNames:
        if not isinstance(frameworkNames, list):
            frameworkNames = [frameworkNames]
    else:
        frameworkNames = ['Python', 'Integration']

    frameworkNames = [quote(f) for f in frameworkNames]
    fmt = lambda x, y: datetime.strftime(parser().parse(x), y)
    startDate = fmt(startDate, '%Y-%m-%d 00:00:00')
    endDate = fmt(endDate, '%Y-%m-%d 23:59:59')

    FrameworksTable = VT.Frameworks()
    RunsTable = VT.Runs()
    JobsTable = VT.Jobs()
    JobHistoryTable = VT.JobHistory()
    TestsTable = VT.Tests()
    TestHistoryTable = VT.TestHistory()

    fwids = FrameworksTable.query(
        sql().Select([
            FrameworksTable.Columns.frameworkId.name
        ]).From([
            FrameworksTable.tableName
        ]).Where([
            FrameworksTable.Columns.name.In(frameworkNames)
        ]).sqltext
    ).execute().get(FrameworksTable.Columns.frameworkId.name)

    if not fwids:
        return {}

    runIds = RunsTable.query(
        sql().Select([
            RunsTable.Columns.runId.name
        ]).From([
            RunsTable.tableName
        ]).Where([
            RunsTable.Columns.created.Between(quote(startDate), quote(endDate))
        ]).sqltext
    ).execute().get(RunsTable.Columns.runId.name)

    if not runIds:
        return {}

    if latest_result_only is False:
        conditions = [
            FrameworksTable.Columns.frameworkId.In(fwids),
            JobsTable.Columns.frameworkId.In(fwids),
            JobsTable.Columns.frameworkId.Equals(FrameworksTable.Columns.frameworkId.aliased_name),
            JobsTable.Columns.jobId.Equals(TestsTable.Columns.jobId.aliased_name),
            JobsTable.Columns.jobId.Equals(JobHistoryTable.Columns.jobId.aliased_name),
            JobHistoryTable.Columns.runId.Equals(TestHistoryTable.Columns.runId.aliased_name),
            TestsTable.Columns.testId.Equals(TestHistoryTable.Columns.testId.aliased_name),
            RunsTable.Columns.runId.Equals(JobHistoryTable.Columns.runId.aliased_name),
            TestHistoryTable.Columns.runId.Between(min(runIds), max(runIds)),
            JobHistoryTable.Columns.runId.Between(min(runIds), max(runIds))
        ]
    else:
        maxRunIdForTests = sql().Select([
            sql.Max(TestHistoryTable.Columns.runId.name)
        ]).From([TestHistoryTable.tableName]).Where([
            sql.And([
                TestHistoryTable.Columns.testId.Equals(TestsTable.Columns.testId.aliased_name),
                TestHistoryTable.Columns.runId.Between(min(runIds), max(runIds))
            ])
        ]).sqltext

        maxRunIdForJobs = sql().Select([
            sql.Max(JobHistoryTable.Columns.runId.name)
        ]).From([JobHistoryTable.tableName]).Where([
            sql.And([
                JobHistoryTable.Columns.jobId.Equals(JobsTable.Columns.jobId.aliased_name),
                JobHistoryTable.Columns.runId.Between(min(runIds), max(runIds))
            ])
        ]).sqltext

        conditions = [
            FrameworksTable.Columns.frameworkId.In(fwids),
            JobsTable.Columns.frameworkId.In(fwids),
            JobsTable.Columns.frameworkId.Equals(FrameworksTable.Columns.frameworkId.aliased_name),
            JobsTable.Columns.jobId.Equals(TestsTable.Columns.jobId.aliased_name),
            JobsTable.Columns.jobId.Equals(JobHistoryTable.Columns.jobId.aliased_name),
            JobHistoryTable.Columns.runId.Equals(TestHistoryTable.Columns.runId.aliased_name),
            TestsTable.Columns.testId.Equals(TestHistoryTable.Columns.testId.aliased_name),
            RunsTable.Columns.runId.Equals(JobHistoryTable.Columns.runId.aliased_name),
            TestHistoryTable.Columns.runId.Equals(maxRunIdForTests),
            JobHistoryTable.Columns.runId.Equals(maxRunIdForJobs)
        ]

    if failures_only is True:
        conditions.append(TestHistoryTable.Columns.age.GreaterThan(0))

    As = lambda x, trim: sql.As(x, x) if trim is False else sql.Trim(x, x)

    desired_columns = [
        As(FrameworksTable.Columns.frameworkId.aliased_name, False),
        As(FrameworksTable.Columns.name.aliased_name, True),

        As(JobsTable.Columns.name.aliased_name, True),
        As(JobsTable.Columns.lastUpdated.aliased_name, False),
        As(JobsTable.Columns.created.aliased_name, False),
        As(JobsTable.Columns.lastBuildNo.aliased_name, False),

        As(JobHistoryTable.Columns.jobId.aliased_name, False),
        As(JobHistoryTable.Columns.runId.aliased_name, False),
        As(JobHistoryTable.Columns.buildNo.aliased_name, False),
        As(JobHistoryTable.Columns.build.aliased_name, True),
        As(JobHistoryTable.Columns.gitBranch.aliased_name, True),
        As(JobHistoryTable.Columns.releaseVersion.aliased_name, True),
        As(JobHistoryTable.Columns.totalTests.aliased_name, False),
        As(JobHistoryTable.Columns.passed.aliased_name, False),
        As(JobHistoryTable.Columns.failed.aliased_name, False),
        As(JobHistoryTable.Columns.skipped.aliased_name, False),
        As(JobHistoryTable.Columns.lapse.aliased_name, False),

        As(TestsTable.Columns.className.aliased_name, True),
        As(TestsTable.Columns.testName.aliased_name, True),
        As(TestsTable.Columns.feature.aliased_name, True),
        As(TestsTable.Columns.owner.aliased_name, True),
        As(TestsTable.Columns.created.aliased_name, False),
        As(TestsTable.Columns.lastUpdated.aliased_name, False),

        As(TestHistoryTable.Columns.testId.aliased_name, False),
        As(TestHistoryTable.Columns.runId.aliased_name, False),
        As(TestHistoryTable.Columns.testResult.aliased_name, True),
        As(TestHistoryTable.Columns.resolution.aliased_name, True),
        As(TestHistoryTable.Columns.reason.aliased_name, True),
        As(TestHistoryTable.Columns.age.aliased_name, False),
        As(TestHistoryTable.Columns.lapse.aliased_name, False),

        As(RunsTable.Columns.created, False)
    ]

    required_tables = [
        FrameworksTable.tableName,
        JobsTable.tableName,
        JobHistoryTable.tableName,
        TestsTable.tableName,
        TestHistoryTable.tableName,
        RunsTable.tableName
    ]

    conditions = [sql.And(conditions)]

    sqlCmd = sql().Select(desired_columns).From(required_tables).Where(conditions).sqltext

    columns, rows = FrameworksTable.query(sqlCmd).execute(to_dict=False)
    return columns, rows if rows else ()


class ToolsTest:
    @staticmethod
    def frameworks():
        python = get_frameworks('Python')
        if not python.get('name')[0].strip() == 'Python':
            raise ToolError('Could not find Python.')

        all_fws = get_frameworks()
        if not 'Integration' in [x.strip() for x in all_fws.get('name')]:
            raise ToolError('Could not find Integration.')

    @staticmethod
    def jobs():
        python = get_frameworks('Python')
        jobs = get_jobs(python.get('frameworkId')[0])
        if not jobs:
            raise ToolError('Could not get Python jobs.')

        all_fws = get_frameworks()
        jobs = get_jobs(all_fws.get('frameworkId'))
        if not jobs:
            raise ToolError('Could not get Python jobs.')

    @staticmethod
    def t():
        python = get_frameworks('Python')
        jobs = get_jobs(python.get('frameworkId')[0])
        tests = get_tests(jobs.get('jobId'))
        if not tests:
            raise ToolError('Could not get Python tests.')

class ToolError(Exception):
    pass


if __name__ == '__main__':
    # TestTools.test_frameworks()
    # TestTools.test_jobs()
    # TestTools.test_tests()
    get_all_view(startDate='2019-08-13', endDate='2019-08-13', frameworkNames='Python', latest_result_only=False)