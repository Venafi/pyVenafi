from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ServiceModuleAttributes(TopAttributes, metaclass=PropertyMeta):
	driver_arguments = Attribute('Driver Arguments')
	driver_name = Attribute('Driver Name')
	heartbeat_interval = Attribute('Heartbeat Interval')
	interval = Attribute('Interval')
	started_by = Attribute('Started By')
