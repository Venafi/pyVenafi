from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.organization import OrganizationAttributes


class AgentModuleHandlerContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Module Handler Container"
