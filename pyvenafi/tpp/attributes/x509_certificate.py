from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.x509_certificate_base import X509CertificateBaseAttributes
from pyvenafi.tpp.attributes.x509_certificate_validation import X509CertificateValidationAttributes

class X509CertificateAttributes(
    X509CertificateBaseAttributes,
    X509CertificateValidationAttributes,
    metaclass=IterableMeta
):
    __config_class__ = "X509 Certificate"
    acme_account_dn = Attribute('ACME Account DN', min_version='21.4')
    application_group_dn = Attribute('Application Group DN', min_version='21.4')
    custom_subjectaltname_othername_definition = Attribute(
        'Custom SubjectAltName OtherName Definition',
        min_version='24.1'
    )
    microsoft_ca_pool_certificate_authority = Attribute('Microsoft CA Pool:Certificate Authority', min_version='21.4')
    portal_download_count = Attribute('Portal Download Count', min_version='21.4')
    prohibited_san_types = Attribute('Prohibited SAN Types', min_version='21.4')
    sid_extension_allow_sid_outside_of_connected_identities = Attribute(
        'SID Extension:Allow SID Outside Of Connected Identities',
        min_version='23.1'
    )
    sid_extension_allowed = Attribute('SID Extension:Allowed', min_version='23.1')
    sid_extension_do_not_automatically_include_requester_identity = Attribute(
        'SID Extension:Do Not Automatically Include Requester Identity',
        min_version='23.1'
    )
    sid_extension_effective_value = Attribute('SID Extension:Effective Value', min_version='23.1')
    sid_extension_value = Attribute('SID Extension:Value', min_version='23.1')
    ticket_dn = Attribute('Ticket DN', min_version='21.4')
    work_dn = Attribute('Work DN', min_version='21.4')
