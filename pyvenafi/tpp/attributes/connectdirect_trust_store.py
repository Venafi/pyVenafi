from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class ConnectDirectTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "ConnectDirect Trust Store"
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    node_name = Attribute('Node Name', min_version='21.4')
    protocol = Attribute('Protocol', min_version='21.4')
