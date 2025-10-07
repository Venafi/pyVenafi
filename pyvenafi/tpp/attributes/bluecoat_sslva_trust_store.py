from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class BlueCoatSSLVATrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "BlueCoat SSLVA Trust Store"
    create_lists = Attribute('Create Lists', min_version='21.4')
    key_store = Attribute('Key Store', min_version='21.4')
