from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class HashiCorpVaultPKIAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "HashiCorp Vault PKI"
    crl_address = Attribute('CRL Address', min_version='21.4')
    create_certificate_authority = Attribute('Create Certificate Authority', min_version='21.4')
    create_pki_role = Attribute('Create PKI Role', min_version='21.4')
    enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    ocsp_address = Attribute('OCSP Address', min_version='21.4')
    policydn = Attribute('PolicyDN', min_version='21.4')
    role_name = Attribute('Role Name', min_version='21.4')
