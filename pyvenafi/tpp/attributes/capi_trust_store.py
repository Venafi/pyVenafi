from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class CAPITrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "CAPI Trust Store"
    log_windows_events = Attribute('Log Windows Events', min_version='21.4')
    trust_store_name = Attribute('Trust Store Name', min_version='21.4')
