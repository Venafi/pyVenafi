from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class GSKTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "GSK Trust Store"
    fips_key = Attribute('Fips Key', min_version='21.4')
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    stash_password = Attribute('Stash Password', min_version='21.4')
