from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.driver_base import DriverBaseAttributes


class LayoutDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Driver Base"
