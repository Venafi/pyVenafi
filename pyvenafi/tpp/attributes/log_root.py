from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class LogRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Root"
    log_application_container = Attribute('Log Application Container', min_version='21.4')
