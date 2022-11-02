from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.ssh_certificate_base import SSHCertificateBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class SSHHostCertificateAttributes(SSHCertificateBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Host Certificate"
