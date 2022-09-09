from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.driver_base import DriverBaseAttributes


class AgentModuleHandlerAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Module Handler"
    version = Attribute('Version')
