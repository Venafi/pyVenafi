from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class ValidationManagerAttributes(ServiceModuleAttributes, metaclass=PropertyMeta):
	start_time = Attribute('Start Time')
