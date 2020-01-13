from sql.sqlHelper import SQLCommandExecutor
from datetime import datetime


class SPIN(SQLCommandExecutor):
    def __init__(self):
        super().__init__(
            server='192.168.7.148',
            port='1433',
            database='SPIN',
            username='sa',
            password='newPassw0rd!'
        )

    def query(self, command: str):
        self._cmd = command
        return self.execute()

    class TestInfo:
        tableName = 'TestInfo'
        testId = f"{tableName}.testId"
        testGuid = f"{tableName}.testGuid"
        testName = f"{tableName}.testName"
        filePath = f"{tableName}.filePath"
        created = f"{tableName}.created"
        lastRun = f"{tableName}.lastRun"

        @classmethod
        def fetch(cls, guid: str):
            return f"""
            SELECT 
                {cls.testId} AS '{cls.testId}',
                {cls.testGuid} AS '{cls.testGuid}',
                {cls.filePath} AS '{cls.filePath}',
                {cls.lastRun} AS '{cls.lastRun}',
                {cls.created} AS '{cls.created}',
                {cls.testName} AS '{cls.testName}'
            FROM {cls.tableName}
            WHERE {cls.testGuid} = '{guid}'
        """

        @classmethod
        def insert(cls, test_guid: str, test_name: str, file_path: str, created: datetime, last_run: datetime):
            return f"""
                INSERT INTO {cls.tableName} 
                (
                    {cls.testGuid},
                    {cls.testName},
                    {cls.filePath},
                    {cls.lastRun},
                    {cls.created}
                ) 
                VALUES 
                (
                    '{test_guid}',
                    '{test_name}',
                    '{file_path}',
                    '{created.strftime('%Y-%m-%d %H:%M:%S')}',
                    '{last_run.strftime('%Y-%m-%d %H:%M:%S')}'
                )
            """

    class TestResults:
        tableName = 'TestResults'
        testId = f"{tableName}.testId"
        testResult = f"{tableName}.testResult"
        logFile = f"{tableName}.logFile"
        consecutiveFailures = f"{tableName}.consecutiveFailures"
        runDate = f"{tableName}.runDate"
        timeLapse = f"{tableName}.timeLapse"

        @classmethod
        def fetch_most_recent(cls, test_id: int):
            return f"""
                SELECT 
                    {cls.testId} AS ' {cls.testId}',
                    {cls.testResult} AS ' {cls.testResult}',
                    {cls.logFile} AS ' {cls.logFile}',
                    {cls.consecutiveFailures} AS ' {cls.consecutiveFailures}',
                    {cls.runDate} AS ' {cls.runDate}',
                    {cls.timeLapse} AS ' {cls.timeLapse}'
                FROM {cls.tableName}
                WHERE {cls.testId} = {test_id}
                ORDER BY {cls.runDate} DESC
            """

        @classmethod
        def insert(cls, test_id: int,  test_result: int, log_file: str, consecutive_fails: int,
                   run_date: datetime, time_lapse: int):
            return f"""
                INSERT INTO {cls.tableName} 
                (
                    {cls.testId},
                    {cls.testResult},
                    {cls.logFile},
                    {cls.consecutiveFailures},
                    {cls.runDate},
                    {cls.timeLapse}
                )
                VALUES
                (
                    {test_id},
                    {test_result},
                    '{log_file}',
                    {consecutive_fails},
                    '{run_date.strftime('%Y-%m-%d %H:%M:%S')}',
                    {time_lapse}
                )
            """

    class TestAnnotations:
        tableName = 'TestAnnotations'
        testId = f"{tableName}.testId"
        labelId = f"{tableName}.labelId"
        valueId = f"{tableName}.valueId"

    class TestAnnotationLabels:
        tableName = 'TestAnnotationLabels'
        labelId = f"{tableName}.labelId"
        annotationLabel = f"{tableName}.annotationLabel"

    class TestAnnotationValues:
        tableName = 'TestAnnotationValues'
        valueId = f"{tableName}.valueId"
        annotationValue = f"{tableName}.annotationValue"

    class TestResultValues:
        tableName = 'TestResultValues'
        resultId = f"{tableName}.resultId"
        resultValue = f"{tableName}.resultValue"


def test_it():
    spin = SPIN()
    result = spin.query(spin.TestInfo.fetch('guid_0'))
    print(result)


if __name__ == '__main__':
    test_it()

