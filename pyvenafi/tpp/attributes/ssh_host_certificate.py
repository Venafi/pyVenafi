from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.ssh_certificate_base import SSHCertificateBaseAttributes

class SSHHostCertificateAttributes(SSHCertificateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Host Certificate"
