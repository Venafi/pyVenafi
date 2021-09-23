from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ApertureConfigurationAttributes(TopAttributes, metaclass=PropertyMeta):
	applies_to = Attribute('Applies To')
	feedback_url = Attribute('Feedback Url')
	help_text = Attribute('Help Text')
	help_url = Attribute('Help Url')
	lost_and_found = Attribute('Lost and Found')
	timeout = Attribute('Timeout')
