from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes


class EncryptionDriverAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Encryption Driver"
    encryption_data = Attribute('Encryption Data')
