from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class CloudInstanceMonitorAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Cloud Instance Monitor"
