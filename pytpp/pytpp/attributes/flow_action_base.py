from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class FlowActionBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	rank = Attribute('Rank', min_version='19.2')
