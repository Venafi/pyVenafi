from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ReportTemplateAttributes(TopAttributes, metaclass=PropertyMeta):
	item_vault_id = Attribute('Item Vault Id')
	report_class = Attribute('Report Class')
	template_vault_id = Attribute('Template Vault Id')
