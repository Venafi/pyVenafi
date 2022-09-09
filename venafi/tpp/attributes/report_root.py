from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.branch_base import BranchBaseAttributes


class ReportRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report Root"
