from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class SelfSignedCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Self Signed CA"
    algorithm = Attribute('Algorithm', min_version='21.4')
    enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='21.4')
    key_usage = Attribute('Key Usage', min_version='21.4')
