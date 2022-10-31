from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.ssh_certificate_base import SSHCertificateBaseAttributes
from venafi.tpp.attributes.top import TopAttributes


class SSHHostCertificateAttributes(SSHCertificateBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Host Certificate"
