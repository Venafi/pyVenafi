from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class AgentDiscoveryBaseAttributes(DiscoveryStatisticsAttributes, ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Discovery Base"
    configuration = Attribute('Configuration')
    discovery_exclusion_dn = Attribute('Discovery Exclusion DN')
    protection_key = Attribute('Protection Key')
    report_dn = Attribute('Report DN')
    status = Attribute('Status')
