from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes


class AgentModuleHandlerAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Module Handler"
    version = Attribute('Version')
