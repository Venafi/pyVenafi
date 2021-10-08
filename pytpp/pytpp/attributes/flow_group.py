from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class FlowGroupAttributes(TopAttributes, metaclass=PropertyMeta):
	product_code_description = Attribute('Product Code Description', min_version='19.4')
