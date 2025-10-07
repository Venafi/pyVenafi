from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes

class X509CertificateValidationAttributes(ValidationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 Certificate Validation"
    detect_all_ssl_tls_protocols = Attribute('Detect All SSL TLS Protocols', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    use_common_name = Attribute('Use Common Name', min_version='21.4')
    use_dns_subjectaltname = Attribute('Use DNS SubjectAltName', min_version='21.4')
    validate_chain_returned_by_host = Attribute('Validate Chain Returned By Host', min_version='21.4')
