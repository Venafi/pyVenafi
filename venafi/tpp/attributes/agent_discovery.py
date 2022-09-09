from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.agent_discovery_base import AgentDiscoveryBaseAttributes


class AgentDiscoveryAttributes(AgentDiscoveryBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Discovery"
