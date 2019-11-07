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
            command = self._cmd if not isinstance(self._cmd, SQLCommandBuilder) else self._cmd.sqltext
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


class SQLColumn:
    def __init__(self, table, name):
        """
        :param name: Column name
        """
        self.name = name
        self.table = table
        self.aliased_name = table + "." + name

    def __repr__(self):
        return self.aliased_name

    def _format_value(self, value):
        return str(value)

    def Equals(self, value):
        return "%s = (%s)" % (self.aliased_name, value)

    def NotEquals(self, value):
        return "%s <> (%s)" % (self.aliased_name, value)

    def GreaterThan(self, value):
        return "%s > (%s)" % (self.aliased_name, value)

    def GreaterThanEquals(self, value):
        return "%s >= (%s)" % (self.aliased_name, value)

    def LessThan(self, value):
        return "%s < (%s)" % (self.aliased_name, value)

    def LessThanEquals(self, value):
        return "%s <= (%s)" % (self.aliased_name, value)

    def Like(self, value):
        return "%s LIKE (%s)" % (self.aliased_name, value)

    def NotLike(self, value):
        return "%s NOT LIKE (%s)" % (self.aliased_name, value)

    def Between(self, value1, value2):
        return "%s BETWEEN %s AND %s" % (self.aliased_name, value1, value2)

    def NotBetween(self, value1, value2):
        return "%s NOT BETWEEN %s AND %s" % (self.aliased_name, value1, value2)

    def In(self, values):
        if not isinstance(values, list):
            values = [values]
        return "%s IN (%s)" % (self.aliased_name, ", ".join(str(v) for v in values))

    def NotIn(self, values):
        if not isinstance(values, list):
            values = [values]
        return "%s NOT IN (%s)" % (self.aliased_name, ", ".join(str(v) for v in values))


def quote(value):
    return "'%s'" % str(value).replace("'", "''")


class SQLCommandBuilder:
    def __init__(self):
        self._text = ""

    @property
    def sqltext(self):
        cmd = self._text
        self._text = ""
        return cmd

    def Select(self, items, distinct=False, top=0):
        if not isinstance(items, list):
            items = [items]

        self._text += "SELECT "
        if distinct is True:
            self._text += "DISTINCT "

        if top > 0:
            self._text += "TOP %s " % top

        self._text += ",\n\t".join([str(item) for item in items]) + "\n"

        return self

    def From(self, tables):
        if not isinstance(tables, list):
            tables = [tables]
        self._text += "FROM " + ",\n\t".join([str(table) for table in tables]) + "\n"

        return self

    def Join(self, table):
        self._text += "JOIN %s " % table
        return self

    def On(self, arg):
        self._text += "ON %s\n" % arg
        return self

    def OrderBy(self, args):
        if not isinstance(args, list):
            args = [args]
        self._text += "ORDER BY " + ", ".join([str(a) for a in args])

        return self

    def Where(self, args):
        if not isinstance(args, list):
            args = [args]
        self._text += "WHERE " + "\n".join([str(a) for a in args]) + "\n"

        return self

    def Update(self, table):
        self._text += "UPDATE %s\n" % table
        return self

    def InsertInto(self, table):
        self._text += "INSERT INTO %s\n" % table
        return self

    def Set(self, args):
        if not isinstance(args, list):
            args = [args]
        self._text += "SET %s\n" % ",\n\t".join(str(a) for a in args)
        return self

    def Values(self, args):
        if isinstance(args, dict):
            columns = []
            values = []
            for key in args:
                columns.append(str(key))
                values.append(str(args[key]))

            self._text += "\t({columns})\nVALUES\n\t({values})".format(
                columns=",\n\t".join(columns),
                values=",\n\t".join(values)
            )
        else:
            if not isinstance(args, list):
                args = [args]
            self._text += "VALUES (%s)" % ",\n\t".join(args)

        return self

    def Delete(self):
        self._text += "DELETE\n"
        return self

    @staticmethod
    def And(args):
        if not isinstance(args, list):
            args = [args]
        return "(" + "\n\tAND ".join([str(a) for a in args]) + ") "

    @staticmethod
    def Or(args):
        if not isinstance(args, list):
            args = [args]
        return "OR ((" + "\n\tAND ".join([str(a) for a in args]) + ")) "

    @staticmethod
    def Max(arg, alias=None):
        if alias:
            return "MAX({a}) AS {alias}".format(a=arg, alias=alias)
        else:
            return "MAX({a})".format(a=arg)

    @staticmethod
    def IsNull(arg, default_value, alias=None):
        if alias:
            return "ISNULL({a}, {d}) AS {alias}".format(a=arg, d=str(default_value), alias=alias)
        else:
            return "ISNULL({a}, {d})".format(a=arg, d=str(default_value))

    @staticmethod
    def Trim(arg, alias=None):
        if alias:
            return "TRIM({a}) AS {alias}".format(a=arg, alias=quote(alias))
        else:
            return "TRIM({a})".format(a=arg)

    @staticmethod
    def As(arg, alias):
        return "{arg} AS {alias}".format(arg=arg, alias=quote(alias))


def SelectTest():
    print('------- %s -------' % SelectTest.func_name)
    foo = SQLColumn('Table1', 'foo')
    bar = SQLColumn('Table1', 'bar')
    meh = SQLColumn('Table2', 'meh')
    bla = SQLColumn('Table2', 'bla')

    c = SQLCommandBuilder()
    query = c.Select([foo.aliased_name, bar.aliased_name], top=100, distinct=True)\
            .From(['Table1', 'Table3'])\
            .Join('Table2')\
            .On(bar.Equals(meh.aliased_name))\
            .Where(
                [
                    c.And(
                        [
                            foo.Equals("'FOO'"),
                            bar.GreaterThan(meh.aliased_name)
                        ]
                    ),
                    c.Or(
                        [
                            meh.Like("'%MEH%'"),
                            bla.In([1, 5])
                        ]
                    )
                ]
            )

    print(query.sqltext)

def InsertTest():
    print('------- %s -------' % InsertTest.func_name)
    c = SQLCommandBuilder()
    cmd = c.InsertInto('Table1')\
            .Values(
                {
                    'column1': 'value1',
                    'column2': 'value2'
                }
            )

    print(cmd.sqltext)

    cmd = c.InsertInto('Table2').Values('value1, value2')
    print(cmd.sqltext)

def UpdateTest():
    print('------- %s -------' % UpdateTest.func_name)
    foo = SQLColumn('Table1', 'foo')
    bar = SQLColumn('Table1', 'bar')
    meh = SQLColumn('Table2', 'meh')
    bla = SQLColumn('Table2', 'bla')

    c = SQLCommandBuilder()
    cmd = c.Update('Table1')\
           .Set(
                [
                    foo.Equals(1),
                    bar.Equals('BAR')
                ]
            )\
           .Where(
                c.And([
                    meh.GreaterThan(2),
                    bla.Equals('BLA')
                ])
            )
    print(cmd.sqltext)

def SubQueryTest():
    print('------- %s -------' % SubQueryTest.func_name)
    foo = SQLColumn('Table1', 'foo')
    bar = SQLColumn('Table1', 'bar')
    meh = SQLColumn('Table2', 'meh')
    bla = SQLColumn('Table2', 'bla')

    c = SQLCommandBuilder()
    subquery = c.Select([meh.aliased_name]) \
        .From('Table2') \
        .Where(c.And(meh.GreaterThan(3))).sqltext

    query = c.Select([foo.aliased_name, bar.aliased_name], top=100, distinct=True)\
            .From(['Table1', 'Table3'])\
            .Join('Table2')\
            .On(bar.Equals(meh.aliased_name))\
            .Where(
                bla.In(
                    subquery
                )
            )

    print(query.sqltext)

def DeleteTest():
    print('------- %s -------' % DeleteTest.func_name)
    foo = SQLColumn('Table1', 'foo')
    bar = SQLColumn('Table1', 'bar')

    c = SQLCommandBuilder()
    cmd = c.Delete().From('Table1').Where(foo.Equals(bar.aliased_name))
    print(cmd.sqltext)

def IsNullMaxTest():
    print('------- %s -------' % IsNullMaxTest.func_name)
    foo = SQLColumn('Table1', 'foo')
    bar = SQLColumn('Table1', 'bar')

    c = SQLCommandBuilder()
    query = c.Select([c.IsNull(c.Max(foo.aliased_name), 0, foo.name), c.Max(bar.aliased_name, bar.name)])\
            .From(['Table1'])\

    print(query.sqltext)


if __name__ == '__main__':
    SelectTest()
    InsertTest()
    UpdateTest()
    SubQueryTest()
    DeleteTest()
    IsNullMaxTest()