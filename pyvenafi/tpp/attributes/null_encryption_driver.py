from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.encryption_driver import EncryptionDriverAttributes


class NullEncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "Null Encryption Driver"
