from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.log_sql_channel import LogSQLChannelAttributes


class LogMSSQLAttributes(LogSQLChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log MSSQL"
