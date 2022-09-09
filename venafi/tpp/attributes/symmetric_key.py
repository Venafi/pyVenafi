from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from venafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes
from venafi.tpp.attributes.top import TopAttributes


class SymmetricKeyAttributes(LegacyKeyBaseAttributes, MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Symmetric Key"
    check_value = Attribute('Check Value')
