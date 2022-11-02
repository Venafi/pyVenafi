from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes


class IdentityDriverAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Identity Driver"
    display_name_attributes = Attribute('Display Name Attributes')
    mapping_table = Attribute('Mapping Table')
