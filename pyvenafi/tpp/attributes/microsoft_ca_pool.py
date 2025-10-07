from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class MicrosoftCAPoolAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Microsoft CA Pool"
    certificate_authority = Attribute('Certificate Authority', min_version='21.4')
    second_certificate_authority = Attribute('Second Certificate Authority', min_version='21.4')
    third_certificate_authority = Attribute('Third Certificate Authority', min_version='21.4')
