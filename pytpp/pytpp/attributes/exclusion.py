from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ExclusionAttributes(TopAttributes, metaclass=PropertyMeta):
	rule = Attribute('Rule')
