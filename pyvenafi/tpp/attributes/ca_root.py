from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class CARootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "CA Root"
