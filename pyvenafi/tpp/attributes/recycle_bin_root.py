from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class RecycleBinRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Recycle Bin Root"
    deletion_daily_max_time = Attribute('Deletion Daily Max Time', min_version='22.2')
    expiration_daily_max_time = Attribute('Expiration Daily Max Time', min_version='22.2')
    expiration_days = Attribute('Expiration Days', min_version='22.2')
    recycle_deletion_query_size = Attribute('Recycle Deletion Query Size', min_version='22.2')
    recycle_deletion_sql_timeout = Attribute('Recycle Deletion SQL Timeout', min_version='22.2')
    recycle_deletion_server_dn = Attribute('Recycle Deletion Server DN', min_version='22.2')
    recycle_deletion_tasks = Attribute('Recycle Deletion Tasks', min_version='22.2')
    recycle_purge_server_dn = Attribute('Recycle Purge Server DN', min_version='22.2')
