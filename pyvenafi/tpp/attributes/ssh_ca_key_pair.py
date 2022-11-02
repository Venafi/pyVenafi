from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.key_pair import KeyPairAttributes
from pyvenafi.tpp.attributes.ssh_ca_key_pair_container import SSHCAKeyPairContainerAttributes


class SSHCAKeyPairAttributes(KeyPairAttributes, SSHCAKeyPairContainerAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH CA Key Pair"
    fingerprint_sha256 = Attribute('Fingerprint SHA256', min_version='21.2')
