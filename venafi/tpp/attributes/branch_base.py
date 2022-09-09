from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.tree_root import TreeRootAttributes


class BranchBaseAttributes(TreeRootAttributes, metaclass=IterableMeta):
    __config_class__ = "Branch Base"
