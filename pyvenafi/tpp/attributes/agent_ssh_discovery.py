from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.agent_discovery_base import AgentDiscoveryBaseAttributes


class AgentSSHDiscoveryAttributes(AgentDiscoveryBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent SSH Discovery"
