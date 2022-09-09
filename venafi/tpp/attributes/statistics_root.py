from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.branch_base import BranchBaseAttributes


class StatisticsRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Statistics Root"
