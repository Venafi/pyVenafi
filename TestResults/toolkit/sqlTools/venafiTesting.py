from toolkit.sqlTools.sqlHelper import SQLCommandExecutor, SQLColumn, SQLCommandBuilder, quote


class VenafiTesting(SQLCommandExecutor, SQLCommandBuilder):
    def __init__(self):
        SQLCommandExecutor.__init__(
            self,
            server='192.168.7.148',
            port='1433',
            database='VenafiTesting',
            username='sa',
            password='newPassw0rd!'
        )
        SQLCommandBuilder.__init__(self)

        self.tableName = self.__class__.__name__

    def query(self, qry, print_qry=False):
        if print_qry:
            print(qry)
        self._cmd = qry
        return self


class Frameworks(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()
        
        class Columns:
            frameworkId = SQLColumn(table=self.tableName, name="frameworkId")
            name = SQLColumn(self.tableName, "name")
            lastUpdated = SQLColumn(self.tableName, "lastUpdated")
        
        self.Columns = Columns
        self.frameworkId = None
        self.name = None
        self.lastUpdated = None

    def _load(self, frameworkId=None, name=None, lastUpdated=None):
        self.frameworkId = frameworkId
        self.name = name
        self.lastUpdated = lastUpdated

    def load_framework(self, frameworkName):
        fw = self.query(
            self.Select([self.Columns.frameworkId.aliased_name, self.Columns.lastUpdated.aliased_name]).
                From([self.tableName]).
                Where([self.Columns.name.Equals(quote(frameworkName))]).
                sqltext
        ).execute()

        self._load(
            frameworkId=fw[self.Columns.frameworkId.name][0],
            name=frameworkName,
            lastUpdated=fw[self.Columns.lastUpdated.name][0]
        )

    def update_sql_cmd(self, lastUpdated):
        if not (self.frameworkId and self.name):
            raise AssertionError('Must initialize the framework by calling "load_framework" before running an update command.')

        self.query(
            self.Update(self.tableName).
                Set([self.Columns.lastUpdated.Equals(quote(lastUpdated))]).
                Where([
                    self.And([
                        self.Columns.frameworkId.Equals(self.frameworkId),
                        self.Columns.name.Equals(quote(self.name))
                    ])
                ]).
                sqltext
        ).execute()

        self._load(self.frameworkId, self.name, lastUpdated)


class JobHistory(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()

        class Columns:
            jobId = SQLColumn(self.tableName, "jobId")
            runId = SQLColumn(self.tableName, "runId")
            buildNo = SQLColumn(self.tableName, "buildNo")
            build = SQLColumn(self.tableName, "build")
            releaseVersion = SQLColumn(self.tableName, "releaseVersion")
            gitBranch = SQLColumn(self.tableName, "gitBranch")
            totalTests = SQLColumn(self.tableName, "totalTests")
            passed = SQLColumn(self.tableName, "passed")
            failed = SQLColumn(self.tableName, "failed")
            skipped = SQLColumn(self.tableName, "skipped")
            lapse = SQLColumn(self.tableName, "lapse")
        
        self.Columns = Columns

        self.jobId = None
        self.runId = None
        self.buildNo = None
        self.build = None
        self.releaseVersion = None
        self.gitBranch = None
        self.totalTest = None
        self.passed = None
        self.failed = None
        self.skipped = None
        self.lapse = None

    def _load(self, jobId=None, runId=None, buildNo=None, build=None, releaseVersion=None,
              gitBranch=None, totalTests=None, passed=None, failed=None, skipped=None, lapse=None):
        self.jobId = jobId
        self.runId = runId
        self.buildNo = buildNo
        self.build = build
        self.releaseVersion = releaseVersion
        self.gitBranch = gitBranch
        self.totalTest = totalTests
        self.passed = passed
        self.failed = failed
        self.skipped = skipped
        self.lapse = lapse

    def insert_sql_cmd(self, jobId, runId, buildNo, build, releaseVersion, gitBranch, totalTests, passed, failed, skipped, lapse):
        self.query(
            self.InsertInto(self.tableName).Values({
                self.Columns.jobId.name: jobId,
                self.Columns.runId.name: runId,
                self.Columns.build.name: quote(build),
                self.Columns.buildNo.name: buildNo,
                self.Columns.releaseVersion.name: quote(releaseVersion),
                self.Columns.gitBranch.name: quote(gitBranch),
                self.Columns.totalTests.name: totalTests,
                self.Columns.passed.name: passed,
                self.Columns.failed.name: failed,
                self.Columns.skipped.name: skipped,
                self.Columns.lapse.name: lapse
            }).sqltext
        ).execute()

        self._load(jobId=jobId, runId=runId, buildNo=buildNo, build=build, releaseVersion=releaseVersion, gitBranch=gitBranch,
                   totalTests=totalTests, passed=passed, failed=failed, skipped=skipped, lapse=lapse)


class Jobs(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()
        class Columns:
            jobId = SQLColumn(self.tableName, "jobId")
            name= SQLColumn(self.tableName, "name")
            frameworkId = SQLColumn(self.tableName, "frameworkId")
            created = SQLColumn(self.tableName, "created")
            lastUpdated = SQLColumn(self.tableName, "lastUpdated")
            lastBuildNo = SQLColumn(self.tableName, "lastBuildNo")

        self.Columns = Columns
        self.jobId = None
        self.name= None
        self.frameworkId = None
        self.created = None
        self.lastUpdated = None
        self.lastBuildNo = None

    def _load(self, jobId=None, name=None, frameworkId=None, created=None, lastUpdated=None, lastBuildNo=None):
        self.jobId = jobId
        self.name= name
        self.frameworkId = frameworkId
        self.created = created
        self.lastUpdated = lastUpdated
        self.lastBuildNo = lastBuildNo

    def load(self, frameworkId, name):
        results = self.query(
            self.Select([
                self.Columns.jobId.aliased_name,
                self.Columns.created.aliased_name,
                self.Columns.lastUpdated.aliased_name,
                self.Columns.lastBuildNo.aliased_name
            ]).From([self.tableName]).Where([
                self.And([
                    self.Columns.name.Equals(quote(name)),
                    self.Columns.frameworkId.Equals(frameworkId)
                ])
            ]).sqltext
        ).execute()

        if not results:
            raise AssertionError('No results to load.')

        self._load(
            jobId=results[self.Columns.jobId.name][0],
            name=name,
            frameworkId=frameworkId,
            created=results[self.Columns.created.name][0],
            lastUpdated=results[self.Columns.lastUpdated.name][0],
            lastBuildNo=results[self.Columns.lastBuildNo.name][0]
        )

    def insert_sql_cmd(self, name, frameworkId, created, lastUpdated, lastBuildNo):
        self.query(
            self.InsertInto(self.tableName).Values({
                self.Columns.name.name: quote(name),
                self.Columns.frameworkId.name: frameworkId,
                self.Columns.created.name: quote(created),
                self.Columns.lastUpdated.name: quote(lastUpdated),
                self.Columns.lastBuildNo.name: quote(lastBuildNo)
            }).sqltext
        ).execute()

        self.load(frameworkId=frameworkId, name=name)

    def update_last_updated(self, lastUpdated, lastBuildNo):
        self.query(
            self.Update(self.tableName)
                .Set([self.Columns.lastUpdated.Equals(quote(lastUpdated)),
                      self.Columns.lastBuildNo.Equals(lastBuildNo)])
                .Where([
                self.And([
                    self.Columns.jobId.Equals(self.jobId)
                ])
            ]).sqltext
        ).execute()

        self.lastUpdated = lastUpdated


class TestHistory(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()
        class Columns:
            testId = SQLColumn(self.tableName, "testId")
            runId = SQLColumn(self.tableName, "runId")
            testResult = SQLColumn(self.tableName, "testResult")
            reason = SQLColumn(self.tableName, "reason")
            age = SQLColumn(self.tableName, "age")
            resolution = SQLColumn(self.tableName, "resolution")
            lapse = SQLColumn(self.tableName, "lapse")
            
        self.Columns = Columns
        self.testId = None
        self.runId = None
        self.testResult = None
        self.reason = None
        self.age = None
        self.resolution = None
        self.lapse = None


    def _load(self, testId=None, runId=None, testResult=None, reason=None, age=None, resolution=None, lapse=None):
       self.testId=testId
       self.runId=runId
       self.testResult=testResult
       self.reason=reason
       self.age=age
       self.resolution=resolution
       self.lapse=lapse

    def load_most_recent_test(self, testId):
        runId = self.Select([self.Max(self.Columns.runId.name)]) \
            .From([self.tableName]) \
            .Where([self.Columns.testId.Equals(testId)]) \
            .sqltext
        self.load(testId, runId)

    def load(self, testId, runId):

        results = self.query(
            self.Select([
                self.Columns.runId.aliased_name,
                self.Columns.testResult.aliased_name,
                self.Columns.reason.aliased_name,
                self.Columns.age.aliased_name,
                self.Columns.resolution.aliased_name,
                self.Columns.lapse.aliased_name
            ]).From([self.tableName]).Where([
                self.And([
                    self.Columns.testId.Equals(testId),
                    self.Columns.runId.Equals(runId)
                ])
            ]).sqltext
        ).execute()

        if not results:
            raise ValueError('No test recorded for testId %s' % testId)

        self._load(
            testId=testId,
            runId=results[self.Columns.runId.name][0],
            testResult=results[self.Columns.testResult.name][0],
            reason=results[self.Columns.reason.name][0],
            age=results[self.Columns.age.name][0],
            resolution=results[self.Columns.resolution.name][0],
            lapse=results[self.Columns.lapse.name][0]
        )

    def get_last_resolution(self, testId):
        maxRunId = self.Select([self.Max(self.Columns.runId.name)]).From([self.tableName]).Where([self.Columns.testId.Equals(testId)]).sqltext
        results = self.query(
            self.Select([self.Columns.resolution.name])
                .From([self.tableName])
                .Where([
                    self.And([
                        self.Columns.testId.Equals(testId),
                        self.Columns.testResult.Equals(quote('FAILED')),
                        self.Columns.runId.Equals(maxRunId)
                    ])
                ])
                .sqltext
        ).execute()

        if not results:
            return None

        return results[self.Columns.resolution.name][0]

    def update_resolution_for_many_tests(self, testIds, runIds, resolution):
        if not isinstance(testIds, list):
            testIds = [testIds]
        if not isinstance(runIds, list):
            runIds = [runIds]

        pairs = zip(testIds, runIds)
        conditions = [self.And([
                self.Columns.testId.Equals(testIds[0]),
                self.Columns.runId.Equals(runIds[0])
        ])]

        conditions += [self.Or([
            self.And([
                self.Columns.testId.Equals(testId),
                self.Columns.runId.Equals(runId)
            ])
        ]) for testId, runId in pairs[1:]]
        
        self.query(
            self.Update(self.tableName).Set([
                self.Columns.resolution.Equals(quote(resolution))
            ]).Where(conditions).sqltext
        ).execute()

    def insert_sql_cmd(self, testId, runId, testResult, reason, age, resolution, lapse):
        self.query(
            self.InsertInto(self.tableName).Values({
                self.Columns.testId.name: testId,
                self.Columns.runId.name: runId,
                self.Columns.testResult.name: quote(testResult),
                self.Columns.reason.name: quote(reason),
                self.Columns.age.name: age,
                self.Columns.resolution.name: quote(resolution),
                self.Columns.lapse.name: lapse
            }).sqltext
        ).execute()

        self._load(testId=testId, runId=runId, testResult=testResult, reason=reason, age=age, resolution=resolution, lapse=lapse)


class Tests(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()
        class Columns:
            testId = SQLColumn(self.tableName, "testId")
            jobId = SQLColumn(self.tableName, "jobId")
            className = SQLColumn(self.tableName, "className")
            testName = SQLColumn(self.tableName, "testName")
            feature = SQLColumn(self.tableName, "feature")
            owner = SQLColumn(self.tableName, "owner")
            lastUpdated = SQLColumn(self.tableName, "lastUpdated")
            created = SQLColumn(self.tableName, "created")

        self.Columns = Columns
        self.testId = None
        self.jobId = None
        self.className = None
        self.testName = None
        self.feature = None
        self.owner = None
        self.lastUpdated = None
        self.created = None

    def _load(self, testId=None, jobId=None, className=None, testName=None, feature=None, owner=None, lastUpdated=None, created=None):
        self.testId = testId
        self.jobId = jobId
        self.className = className
        self.testName = testName
        self.feature = feature
        self.owner = owner
        self.lastUpdated = lastUpdated
        self.created = created

    def load(self, className, testName, jobId):
        results = self.query(
            self.Select([
                self.Columns.testId.aliased_name,
                self.Columns.feature.aliased_name,
                self.Columns.owner.aliased_name,
                self.Columns.lastUpdated.aliased_name,
                self.Columns.created.aliased_name
            ]).From([self.tableName]).Where([
                self.And([
                    self.Columns.className.Equals(quote(className)),
                    self.Columns.testName.Equals(quote(testName)),
                    self.Columns.jobId.Equals(jobId)
                ])
            ]).sqltext
        ).execute()
        
        if not results:
            raise AssertionError('No testId found for %s' % testName)
        
        self._load(testId=results[self.Columns.testId.name][0],
                   jobId=jobId,
                   className=className,
                   testName=testName,
                   feature=results[self.Columns.feature.name][0],
                   owner=results[self.Columns.owner.name][0],
                   lastUpdated=results[self.Columns.lastUpdated.name][0],
                   created=results[self.Columns.created.name][0])

    def insert_sql_cmd(self, jobId, className, testName, feature, owner, lastUpdated, created):
        self.query(
            self.InsertInto(self.tableName).Values({
                self.Columns.jobId.name: jobId,
                self.Columns.className.name: quote(className),
                self.Columns.testName.name: quote(testName),
                self.Columns.feature.name: quote(feature),
                self.Columns.owner.name: quote(owner),
                self.Columns.lastUpdated.name: quote(lastUpdated),
                self.Columns.created.name: quote(created)
            }).sqltext
        ).execute()

        self.load(className=className, testName=testName, jobId=jobId)

    def update_last_updated(self, when):
        self.query(
            self.Update(self.tableName)
                .Set([self.Columns.lastUpdated.Equals(quote(when))])
                .Where([
                    self.And([
                        self.Columns.testId.Equals(self.testId)
                    ])
                ]).sqltext
        ).execute()
        
        self.lastUpdated = when

    def update_feature(self, feature):
        self.query(
            self.Update(self.tableName)
                .Set([self.Columns.feature.Equals(quote(feature))])
                .Where([self.Columns.testId.Equals(self.testId)])
                .sqltext
        ).execute()

        self.feature = feature

    def update_owner(self, owner):
        self.query(
            self.Update(self.tableName)
                .Set([self.Columns.owner.Equals(quote(owner))])
                .Where([self.Columns.testId.Equals(self.testId)])
                .sqltext
        ).execute()

        self.owner = owner


class Runs(VenafiTesting):
    def __init__(self):
        VenafiTesting.__init__(self)
        self._load()
        class Columns:
            runId = SQLColumn(self.tableName, "runId")
            newJobs = SQLColumn(self.tableName, "newJobs")
            newTests = SQLColumn(self.tableName, "newTests")
            created = SQLColumn(self.tableName, "created")
        
        self.Columns = Columns
        self.runId = None
        self.newJobs = None
        self.newTests = None
        self.created= None

    def _max_run_id_sqltext(self):
        return self.Select([
            self.IsNull(self.Max(self.Columns.runId.name), -1)
        ]).From([self.tableName]).sqltext

    def _load(self, runId=None, newJobs=None, newTests=None, created=None):
        self.runId = runId
        self.newJobs = newJobs
        self.newTests = newTests
        self.created= created

    def load_max_run_id(self):
        self.load(self._max_run_id_sqltext())

    def load(self, runId=None):
        runId = runId or self._max_run_id_sqltext()

        results = self.query(
            self.Select([self.Columns.runId.aliased_name,
                         self.Columns.newJobs.aliased_name,
                         self.Columns.newTests.aliased_name,
                         self.Columns.created.aliased_name]).
                From([self.tableName]).
                Where([self.Columns.runId.Equals(runId)]).
                sqltext
        ).execute()

        self._load(
            runId=results[self.Columns.runId.name][0],
            newJobs=results[self.Columns.newJobs.name][0],
            newTests=results[self.Columns.newTests.name][0],
            created=results[self.Columns.created.name][0],
        )

    def insert_sql_cmd(self, newJobs, newTests, created):
        self.query(
            self.InsertInto(self.tableName).Values({
                self.Columns.newJobs.name: newJobs,
                self.Columns.newTests.name: newTests,
                self.Columns.created.name: quote(created)
            }).sqltext
        ).execute()

        self.load()


def _SqlTablesTest():
    from datetime import datetime, timedelta

    JobsTable = Jobs()
    TestsTable = Tests()
    RunsTable = Runs()
    TestHistoryTable = TestHistory()
    VT = VenafiTesting()
    ops = SQLCommandBuilder()



if __name__ == '__main__':
    _SqlTablesTest()
