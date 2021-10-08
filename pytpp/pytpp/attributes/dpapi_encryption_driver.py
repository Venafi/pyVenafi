from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.encryption_driver import EncryptionDriverAttributes


class DPAPIEncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=PropertyMeta):
	generation_only = Attribute('Generation Only', min_version='18.1')
	key_validation = Attribute('Key Validation')
	verigram = Attribute('VeriGram', min_version='18.1')
