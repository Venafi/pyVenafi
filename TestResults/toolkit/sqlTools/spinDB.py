from toolkit.sqlTools.sqlHelper import SQLCommandExecutor, SQLColumn, SQLCommandBuilder, quote


class SPIN(SQLCommandExecutor, SQLCommandBuilder):
    def __init__(self):
        super(SPIN, self).__init__(
            server='192.168.7.148',
            port='1433',
            database='SPIN',
            username='sa',
            password='newPassw0rd!'
        )
        self.tableName = self.__class__.__name__

    def query(self, qry, print_qry=False):
        if print_qry:
            print(qry)
        self._cmd = qry
        return self


class TestInfo(SPIN):
    def __init__(self):
        super().__init__()
        self.testId = SQLColumn(table=self.tableName, name="testId")
        self.testGuid = SQLColumn(self.tableName, "testGuid")
        self.testName = SQLColumn(self.tableName, "testName")
        self.filePath = SQLColumn(self.tableName, "filePath")
        self.created = SQLColumn(self.tableName, "created")
        self.lastRun = SQLColumn(self.tableName, "lastRun")


class TestResults(SPIN):
    def __init__(self):
        super().__init__()
        self.testId = SQLColumn(table=self.tableName, name="testId")
        self.testResult = SQLColumn(table=self.tableName, name="testResult")
        self.logFile = SQLColumn(table=self.tableName, name="logFile")
        self.consecutiveFailures = SQLColumn(table=self.tableName, name="consecutiveFailures")
        self.runDate = SQLColumn(table=self.tableName, name="runDate")
        self.timeLapse = SQLColumn(table=self.tableName, name="timeLapse")


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


if __name__ == '__main__':
    _SqlTablesTest()
