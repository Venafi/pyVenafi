from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes


class LayoutDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Driver Base"
