from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class MicrosoftCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Microsoft CA"
    enrollment_agent_certificate = Attribute('Enrollment Agent Certificate', min_version='21.4')
    given_name = Attribute('Given Name', min_version='21.4')
    include_cn_as_san = Attribute('Include CN as SAN', min_version='21.4')
    use_external_msca_communicator = Attribute('Use External MSCA Communicator', min_version='22.1')
