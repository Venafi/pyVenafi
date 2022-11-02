from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LogChannelAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Channel"
    configuration = Attribute('Configuration')
    driver_arguments = Attribute('Driver Arguments')
