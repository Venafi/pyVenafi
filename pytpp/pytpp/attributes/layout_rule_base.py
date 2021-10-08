from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LayoutRuleBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	rule = Attribute('Rule', min_version='19.1')
	vault_id = Attribute('Vault Id')
