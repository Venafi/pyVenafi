from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.flow_action_approver_base import FlowActionApproverBaseAttributes

class CodeSigningAdminApprovalActionAttributes(FlowActionApproverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Admin Approval Action"
    include_code_signing_admin = Attribute('Include Code Signing Admin', min_version='21.4')
    include_master_admin = Attribute('Include Master Admin', min_version='21.4')
