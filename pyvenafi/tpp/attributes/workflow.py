from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class WorkflowAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Workflow"
    rule = Attribute('Rule', min_version='21.4')
    rule_vault_id = Attribute('Rule Vault Id', min_version='21.4')
