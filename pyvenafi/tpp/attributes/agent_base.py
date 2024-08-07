from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class AgentBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Agent Base"
    agent_guid = Attribute('Agent GUID', min_version='21.4')
    location = Attribute('Location', min_version='21.4')
