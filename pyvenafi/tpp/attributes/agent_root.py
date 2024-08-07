from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class AgentRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Root"
