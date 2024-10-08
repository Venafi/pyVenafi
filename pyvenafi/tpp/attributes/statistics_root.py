from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class StatisticsRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Statistics Root"
