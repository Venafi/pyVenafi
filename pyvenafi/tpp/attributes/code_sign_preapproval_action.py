from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes

class CodeSignPreApprovalActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Sign PreApproval Action"
    stage_identifier = Attribute('Stage Identifier', min_version='21.4')
