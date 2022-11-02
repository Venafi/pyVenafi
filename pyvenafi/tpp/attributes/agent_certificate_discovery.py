from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.agent_discovery_base import AgentDiscoveryBaseAttributes


class AgentCertificateDiscoveryAttributes(AgentDiscoveryBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Certificate Discovery"
