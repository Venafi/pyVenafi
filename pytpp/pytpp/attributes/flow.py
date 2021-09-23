from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class FlowAttributes(TopAttributes, metaclass=PropertyMeta):
	archive_process = Attribute('Archive Process', min_version='19.2')
	archive_validity = Attribute('Archive Validity', min_version='19.2')
	product_code = Attribute('Product Code', min_version='19.2')
