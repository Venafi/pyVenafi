from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.branch_base import BranchBaseAttributes


class MetadataRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Root"
