from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class F5LTMAdvancedTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "F5 LTM Advanced Trust Store"
    certificate_name = Attribute('Certificate Name', min_version='21.4')
    ssh_port = Attribute('SSH Port', min_version='21.4')
    use_rest_api = Attribute('Use REST API', min_version='22.1')
