from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class ComodoCCMAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Comodo CCM"
    customer_login_uri = Attribute('Customer Login URI', min_version='21.4')
    organization = Attribute('Organization', min_version='21.4')
    secret_key = Attribute('Secret Key', min_version='21.4')
