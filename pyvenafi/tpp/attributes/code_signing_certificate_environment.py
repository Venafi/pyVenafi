from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes

class CodeSigningCertificateEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Certificate Environment"
    ca_specific_attributes = Attribute('CA Specific Attributes', min_version='21.4')
    certificate_authority = Attribute('Certificate Authority', min_version='21.4')
    certificate_dn = Attribute('Certificate DN', min_version='21.4')
    city = Attribute('City', min_version='21.4')
    country = Attribute('Country', min_version='21.4')
    elliptic_curve = Attribute('Elliptic Curve', min_version='21.4')
    key_algorithm = Attribute('Key Algorithm', min_version='21.4')
    key_bit_strength = Attribute('Key Bit Strength', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    organization = Attribute('Organization', min_version='21.4')
    organizational_unit = Attribute('Organizational Unit', min_version='21.4')
    parameter_set = Attribute('Parameter Set', min_version='24.1')
    provide_chain = Attribute('Provide Chain', min_version='21.4')
    state = Attribute('State', min_version='21.4')
    synchronize_chain = Attribute('Synchronize Chain', min_version='21.4')
    target_store = Attribute('Target Store', min_version='21.4')
    x509_subject = Attribute('X509 Subject', min_version='21.4')
    x509_subjectaltname_rfc822 = Attribute('X509 SubjectAltName RFC822', min_version='21.4')
