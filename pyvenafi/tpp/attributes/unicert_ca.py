from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class UniCERTCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "UniCERT CA"
    ca_dn = Attribute('CA DN')
    ra_dn = Attribute('RA DN')
    secure = Attribute('Secure')
    web_instance = Attribute('Web Instance')
