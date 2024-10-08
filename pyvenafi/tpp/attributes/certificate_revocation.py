from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class CertificateRevocationAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Revocation"
    ca_issuer_monitor_disabled = Attribute('CA Issuer Monitor Disabled', min_version='21.4')
    ocsp_concurrent_connection_limit = Attribute('OCSP Concurrent Connection Limit', min_version='21.4')
    ocsp_concurrent_request_limit = Attribute('OCSP Concurrent Request Limit', min_version='21.4')
