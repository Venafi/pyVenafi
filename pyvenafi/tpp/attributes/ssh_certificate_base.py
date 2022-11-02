from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.policy import PolicyAttributes


class SSHCertificateBaseAttributes(PolicyAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Certificate Base"
