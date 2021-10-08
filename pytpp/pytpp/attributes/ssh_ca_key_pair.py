from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.key_pair import KeyPairAttributes


class SSHCAKeyPairAttributes(KeyPairAttributes, metaclass=PropertyMeta):
	fingerprint_sha256 = Attribute('Fingerprint SHA256', min_version='21.2')
