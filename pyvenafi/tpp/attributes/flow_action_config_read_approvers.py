from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.flow_action_approver_base import FlowActionApproverBaseAttributes

class FlowActionConfigReadApproversAttributes(FlowActionApproverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Action Config Read Approvers"
    attribute_name = Attribute('Attribute Name', min_version='21.4')
    object_dn = Attribute('Object DN', min_version='21.4')
    policy_read = Attribute('Policy Read', min_version='21.4')
    use_administrators_as_fallback_approvers = Attribute('Use Administrators as Fallback Approvers', min_version='21.4')
