from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes

class CertificateCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Credential"
    certificate = Attribute('Certificate')
