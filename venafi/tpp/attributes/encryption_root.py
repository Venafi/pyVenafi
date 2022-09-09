from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.branch_base import BranchBaseAttributes


class EncryptionRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Encryption Root"
    encryption_driver = Attribute('Encryption Driver')
    protection_key = Attribute('Protection Key')
