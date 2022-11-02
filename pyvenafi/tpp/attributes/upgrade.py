from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class UpgradeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Upgrade"
    grouping_id = Attribute('Grouping Id', min_version='20.1')
