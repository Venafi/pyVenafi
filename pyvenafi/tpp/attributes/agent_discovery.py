from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.agent_discovery_base import AgentDiscoveryBaseAttributes

class AgentDiscoveryAttributes(AgentDiscoveryBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Discovery"
