from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.service_module import ServiceModuleAttributes


class CloudInstanceMonitorAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=PropertyMeta):
	pass