from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from venafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from venafi.tpp.attributes.top import TopAttributes


class AgentDiscoveryBaseAttributes(DiscoveryStatisticsAttributes, ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Discovery Base"
    configuration = Attribute('Configuration')
    discovery_exclusion_dn = Attribute('Discovery Exclusion DN')
    protection_key = Attribute('Protection Key')
    report_dn = Attribute('Report DN')
    status = Attribute('Status')
