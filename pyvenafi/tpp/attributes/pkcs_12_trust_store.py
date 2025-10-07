from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class PKCS12TrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "PKCS#12 Trust Store"
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
