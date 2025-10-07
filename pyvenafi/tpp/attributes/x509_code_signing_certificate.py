from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.x509_certificate import X509CertificateAttributes

class X509CodeSigningCertificateAttributes(X509CertificateAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 Code Signing Certificate"
    owner = Attribute('Owner', min_version='22.1')
    pending_certificate_vault_id = Attribute('Pending Certificate Vault Id', min_version='23.3')
    pending_private_key_vault_id = Attribute('Pending Private Key Vault Id', min_version='23.3')
    pending_public_key_vault_id = Attribute('Pending Public Key Vault Id', min_version='23.3')
