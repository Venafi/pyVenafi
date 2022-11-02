from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from pyvenafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class SymmetricKeyAttributes(LegacyKeyBaseAttributes, MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Symmetric Key"
    check_value = Attribute('Check Value')
