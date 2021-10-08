from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class EncryptionRootAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	encryption_driver = Attribute('Encryption Driver')
	protection_key = Attribute('Protection Key')
