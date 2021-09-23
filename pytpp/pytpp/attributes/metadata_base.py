from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class MetadataBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	allowed_values = Attribute('Allowed Values')
	associated_classes = Attribute('Associated Classes')
	category = Attribute('Category')
	default_values = Attribute('Default Values')
	help_text = Attribute('Help Text')
	label_text = Attribute('Label Text')
	localization = Attribute('Localization')
	mandatory = Attribute('Mandatory')
	not_before = Attribute('Not Before')
	policyable = Attribute('Policyable')
	render_hidden = Attribute('Render Hidden', min_version='16.2')
	render_read_only = Attribute('Render Read Only', min_version='16.2')
