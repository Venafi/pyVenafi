import pymssql
import traceback
import time


class SQLCommandExecutor:
    def __init__(self, server, port, database, username, password):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password

        self._cmd = None

    @property
    def command(self):
        return str(self._cmd.strip())

    def _connect(self):
        return pymssql.connect(
            server=self.server,
            port=self.port,
            database=self.database,
            user=self.username,
            password=self.password
        )

    def _connect_mssql(self):
        timeout = time.time() + 60
        while time.time() < timeout:
            try:
                return self._connect()
            except:
                pass
        self._connect()

    def _execute(self, to_dict=True):
        conn = None
        try:
            conn = self._connect_mssql()
            cursor = conn.cursor()
            cursor.execute(self._cmd)
            response = list(cursor)
            conn.commit()
            conn.close()

            if not response:
                return None

            if to_dict:
                results = self._dict(response, cursor.description)
            else:
                results = ([x[0] for x in cursor.description], response)

            return results
        except Exception:
            e = traceback.format_exc()
            if conn:
                print('--------------------------------------------')
                print(self._cmd)
                print('--------------------------------------------')
                conn.close()
            raise Exception('Error executing this command:\n%s\nError:%s' % (self.command, e))

    def execute(self, to_dict=True):
        max_retries = 2
        attempts = 0
        while True:
            try:
                return self._execute(to_dict=to_dict)
            except Exception:
                e = traceback.format_exc()
                if attempts < max_retries:
                    attempts += 1
                    continue
                raise Exception(e)

    def _dict(self, response, description):
        dictResponse = {}
        colNames = [x[0] for x in description]
        for row in response:
            colCount = 0
            for col in row:
                try:
                    dictResponse[colNames[colCount]].append(col)
                except:
                    dictResponse[colNames[colCount]] = [col]

                colCount += 1

        return dictResponse

