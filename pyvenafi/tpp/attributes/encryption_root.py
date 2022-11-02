from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class EncryptionRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Encryption Root"
    compression_level = Attribute('Compression Level')
    encryption_driver = Attribute('Encryption Driver')
    protection_key = Attribute('Protection Key')
