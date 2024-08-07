from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.ssh_certificate_base import SSHCertificateBaseAttributes

class SSHClientCertificateAttributes(SSHCertificateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Client Certificate"
