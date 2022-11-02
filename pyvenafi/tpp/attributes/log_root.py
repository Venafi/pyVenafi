from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class LogRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Root"
    log_application_container = Attribute('Log Application Container')
