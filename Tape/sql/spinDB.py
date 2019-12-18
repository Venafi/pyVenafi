from sql.sqlHelper import SQLCommandExecutor, SQLColumn, SQLCommandBuilder, quote


class SPIN:
    executor = SQLCommandExecutor(
        server='192.168.7.148',
        port='1433',
        database='SPIN',
        username='sa',
        password='newPassw0rd!'
    )
    # self.tableName = self.__class__.__name__

    def query(self, qry, print_qry=False):
        if print_qry:
            print(qry)
        self._cmd = qry
        return self

    class TestInfo:
        tableName = 'TestInfo'
        testId = SQLColumn(table=tableName, name="testId")
        testGuid = SQLColumn(tableName, "testGuid")
        testName = SQLColumn(tableName, "testName")
        filePath = SQLColumn(tableName, "filePath")
        created = SQLColumn(tableName, "created")
        lastRun = SQLColumn(tableName, "lastRun")

        def insert(self):
            pass

    class TestResults:
        tableName = 'TestResults'
        testId = SQLColumn(table=tableName, name="testId")
        testResult = SQLColumn(tableName, name="testResult")
        logFile = SQLColumn(tableName, name="logFile")
        consecutiveFailures = SQLColumn(tableName, name="consecutiveFailures")
        runDate = SQLColumn(tableName, name="runDate")
        timeLapse = SQLColumn(tableName, name="timeLapse")

        def insert(self, testId: str, result: str, logFile: str, consecutiveFailures: str, runDate: str, timeLapse: str):
            results = SPIN.query(
                SQLCommandBuilder.InsertInto(
                    self.tableName
                ).Values([
                    testId,
                    result,
                    logFile,
                    consecutiveFailures,
                    runDate,
                    timeLapse
                ]).sqltext
            ).execute()

    # @staticmethod
    # def insert_results(testId: str, result: str, logFile: str, consecutiveFailures: str, runDate: str, timeLapse: str):
    #     spin = SPIN()
    #     ops = SQLCommandBuilder()
    #     testResultsTable = TestResults()
    #
    #     # testId = '600'
    #     # result = '1'
    #     # logFile = 'log_file'
    #     # consecutiveFailures = '0'
    #     # runDate = '2019-12-12 13:41:53.743'
    #     # timeLapse = '3'
    #     results = spin.query(
    #         ops.InsertInto(
    #             testResultsTable.tableName
    #         ).Values([
    #             testId,
    #             result,
    #             logFile,
    #             consecutiveFailures,
    #             runDate,
    #             timeLapse
    #         ]).sqltext
    #     ).execute()


class TestAnnotations(SPIN):
    def __init__(self):
        super().__init__()
        self.testId = SQLColumn(table=self.tableName, name="testId")
        self.labelId = SQLColumn(table=self.tableName, name="labelId")
        self.valueId = SQLColumn(table=self.tableName, name="valueId")


class TestAnnotationLabels(SPIN):
    def __init__(self):
        super().__init__()
        self.labelId = SQLColumn(table=self.tableName, name="labelId")
        self.annotationLabel = SQLColumn(table=self.tableName, name="annotationLabel")


class TestAnnotationValues(SPIN):
    def __init__(self):
        super().__init__()
        self.valueId = SQLColumn(table=self.tableName, name="valueId")
        self.annotationValue = SQLColumn(table=self.tableName, name="annotationValue")


class TestResultValues(SPIN):
    def __init__(self):
        super().__init__()
        self.resultId = SQLColumn(table=self.tableName, name="resultId")
        self.resultValue = SQLColumn(table=self.tableName, name="resultValue")


def _SqlTablesTest():
    spin = SPIN()
    testInfoTable = TestInfo()
    ops = SQLCommandBuilder()

    results = spin.query(
        ops.Select([
            testInfoTable.testId.aliased_name,
            testInfoTable.testName.aliased_name,
            testInfoTable.lastRun
        ]).From([
            testInfoTable.tableName
        ]).Where([
            testInfoTable.testId.GreaterThanEquals(599)
        ]).sqltext
    ).execute()

    print(results)


def _insertTestResult(testId: str, result: str, logFile: str, consecutiveFailures: str, runDate: str, timeLapse: str):
    spin = SPIN()
    ops = SQLCommandBuilder()
    testResultsTable = TestResults()

    # testId = '600'
    # result = '1'
    # logFile = 'log_file'
    # consecutiveFailures = '0'
    # runDate = '2019-12-12 13:41:53.743'
    # timeLapse = '3'
    results = spin.query(
        ops.InsertInto(
            testResultsTable.tableName
        ).Values([
            quote(testId),
            quote(result),
            quote(logFile),
            quote(consecutiveFailures),
            quote(runDate),
            quote(timeLapse)
        ]).sqltext
    ).execute()


#
# if __name__ == '__main__':
# #     _SqlTablesTest()
#     _insertTestResult()

