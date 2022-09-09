from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.driver_base import DriverBaseAttributes


class EncryptionDriverAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Encryption Driver"
    encryption_data = Attribute('Encryption Data')
