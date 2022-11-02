from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.log_sql_channel import LogSQLChannelAttributes


class LogMSSQLAttributes(LogSQLChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log MSSQL"
