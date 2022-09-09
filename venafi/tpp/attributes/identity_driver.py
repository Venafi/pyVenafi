from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.driver_base import DriverBaseAttributes


class IdentityDriverAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Identity Driver"
    display_name_attributes = Attribute('Display Name Attributes', min_version='15.3')
    mapping_table = Attribute('Mapping Table')