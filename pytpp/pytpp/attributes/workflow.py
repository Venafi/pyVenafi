from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class WorkflowAttributes(TopAttributes, metaclass=PropertyMeta):
	rule = Attribute('Rule')
	rule_vault_id = Attribute('Rule Vault Id', min_version='19.3')
