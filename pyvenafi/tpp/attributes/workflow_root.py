from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class WorkflowRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Workflow Root"
    approval_reason = Attribute('Approval Reason', min_version='21.4')
    approver_not_found_expiration = Attribute('Approver Not Found Expiration', min_version='21.4')
    expiration_days = Attribute('Expiration Days', min_version='21.4')
