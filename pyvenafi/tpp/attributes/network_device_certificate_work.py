from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.client_certificate_work import ClientCertificateWorkAttributes

class NetworkDeviceCertificateWorkAttributes(ClientCertificateWorkAttributes, metaclass=IterableMeta):
    __config_class__ = "Network Device Certificate Work"
    authentication_credentials = Attribute('Authentication Credentials', min_version='21.4')
    ca_template_trust_anchors_enabled = Attribute('CA Template Trust Anchors Enabled', min_version='21.4')
    certificates_distribution_type = Attribute('Certificates Distribution Type', min_version='21.4')
    client_certificate_eku_checks_enabled = Attribute('Client Certificate Eku Checks Enabled', min_version='21.4')
    explicit_trust_anchors = Attribute('Explicit Trust Anchors', min_version='21.4')
    fallback_to_http_auth = Attribute('Fallback To Http Auth', min_version='21.4')
    http_basic_auth_disabled = Attribute('Http Basic Auth Disabled', min_version='21.4')
    http_digest_auth_disabled = Attribute('Http Digest Auth Disabled', min_version='21.4')
    pop_mode = Attribute('PoP Mode', min_version='21.4')
    reenrollment_subset_subject_matching_disabled = Attribute('ReEnrollment Subset Subject Matching Disabled', min_version='21.4')
    require_additional_http_auth = Attribute('Require Additional Http Auth', min_version='21.4')
    retryafter_disabled = Attribute('RetryAfter Disabled', min_version='21.4')
    revocation_check_timeout = Attribute('Revocation Check Timeout', min_version='21.4')
    revocation_mode = Attribute('Revocation Mode', min_version='21.4')
    revoke_existing_certificate_on_reenrollment = Attribute('Revoke Existing Certificate On ReEnrollment', min_version='21.4')
    revoke_existing_certificate_on_reenrollment_delay = Attribute('Revoke Existing Certificate On ReEnrollment Delay', min_version='21.4')
    use_implicit_trust_anchors = Attribute('Use Implicit Trust Anchors', min_version='21.4')
