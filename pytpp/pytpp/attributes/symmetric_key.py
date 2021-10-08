from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from pytpp.attributes.monitoring_base import MonitoringBaseAttributes
from pytpp.attributes.top import TopAttributes


class SymmetricKeyAttributes(LegacyKeyBaseAttributes, MonitoringBaseAttributes, TopAttributes, metaclass=PropertyMeta):
	check_value = Attribute('Check Value')
