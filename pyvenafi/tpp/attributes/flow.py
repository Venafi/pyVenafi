from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class FlowAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow"
    archive_process = Attribute('Archive Process')
    archive_validity = Attribute('Archive Validity')
    product_code = Attribute('Product Code')
