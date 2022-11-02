from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class FlowGroupAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Group"
    product_code_description = Attribute('Product Code Description')
