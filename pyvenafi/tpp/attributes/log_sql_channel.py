from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogSQLChannelAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log SQL Channel"
    create_sql_expression = Attribute('Create SQL Expression', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    dsn_vault_id = Attribute('DSN Vault Id', min_version='21.4')
    database = Attribute('Database', min_version='21.4')
    expiration = Attribute('Expiration', min_version='21.4')
    expire_sql_expression = Attribute('Expire SQL Expression', min_version='21.4')
    last_run = Attribute('Last Run', min_version='21.4')
    max_log_age_days = Attribute('Max Log Age Days', min_version='21.4')
    table_name = Attribute('Table Name', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    view_dsn = Attribute('View DSN', min_version='21.4')
