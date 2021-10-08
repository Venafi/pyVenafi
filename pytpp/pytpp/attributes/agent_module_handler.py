from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class AgentModuleHandlerAttributes(DriverBaseAttributes, metaclass=PropertyMeta):
	version = Attribute('Version')
