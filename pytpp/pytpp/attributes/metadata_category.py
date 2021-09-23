from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class MetadataCategoryAttributes(TopAttributes, metaclass=PropertyMeta):
	label_text = Attribute('Label Text')
	localization = Attribute('Localization')
