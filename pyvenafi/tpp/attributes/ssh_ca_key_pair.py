from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.key_pair import KeyPairAttributes


class SSHCAKeyPairAttributes(KeyPairAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH CA Key Pair"
    fingerprint_sha256 = Attribute('Fingerprint SHA256')
