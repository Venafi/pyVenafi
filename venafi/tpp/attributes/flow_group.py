from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class FlowGroupAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Group"
    product_code_description = Attribute('Product Code Description', min_version='19.4')
