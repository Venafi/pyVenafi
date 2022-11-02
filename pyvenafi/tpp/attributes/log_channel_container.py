from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LogChannelContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Channel Container"
    description = Attribute('Description')
