from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogApplicationCustomizationAttributes(TopAttributes, metaclass=PropertyMeta):
	customization_data = Attribute('Customization Data')
	language = Attribute('Language')
