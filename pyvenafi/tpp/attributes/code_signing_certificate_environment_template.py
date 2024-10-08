from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes

class CodeSigningCertificateEnvironmentTemplateAttributes(
    CodeSigningEnvironmentTemplateBaseAttributes,
    metaclass=IterableMeta
):
    __config_class__ = "Code Signing Certificate Environment Template"
    certificate_authority = Attribute('Certificate Authority', min_version='21.4')
    certificate_container_dn = Attribute('Certificate Container DN', min_version='21.4')
    city = Attribute('City', min_version='21.4')
    country = Attribute('Country', min_version='21.4')
    key_algorithm = Attribute('Key Algorithm', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    organization = Attribute('Organization', min_version='21.4')
    organizational_unit = Attribute('Organizational Unit', min_version='21.4')
    state = Attribute('State', min_version='21.4')
    x509_subject = Attribute('X509 Subject', min_version='21.4')
    x509_subjectaltname_rfc822 = Attribute('X509 SubjectAltName RFC822', min_version='21.4')
