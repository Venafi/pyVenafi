from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class XolphinCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Xolphin CA"
    brand = Attribute('Brand')
    included_domains = Attribute('Included Domains')
    product = Attribute('Product')
    type = Attribute('Type')
