from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class AgentContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Container"
