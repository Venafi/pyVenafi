from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class UpgradeTaskAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Upgrade Task"
    display_name = Attribute('Display Name', min_version='20.1')
    upgrade_task_execution_order_id = Attribute('Upgrade Task Execution Order Id', min_version='20.1')
