from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.encryption_driver import EncryptionDriverAttributes


class NullEncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=PropertyMeta):
	pass