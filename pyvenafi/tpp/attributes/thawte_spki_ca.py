from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class ThawteSPKICAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Thawte SPKI CA"
    certificate_block = Attribute('Certificate Block')
    certificate_transparency = Attribute('Certificate Transparency', min_version='16.3')
    retrieval_period = Attribute('Retrieval Period', min_version='15.4')
    server_type = Attribute('Server Type')
    signature_algorithm = Attribute('Signature Algorithm')
    uri = Attribute('URI')
