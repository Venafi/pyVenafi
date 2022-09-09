from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class WorkflowAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Workflow"
    rule = Attribute('Rule')
    rule_vault_id = Attribute('Rule Vault Id', min_version='19.3')
