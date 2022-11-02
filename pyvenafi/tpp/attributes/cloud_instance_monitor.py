from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class CloudInstanceMonitorAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Cloud Instance Monitor"
