from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class KeynectisSequoiaCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Keynectis Sequoia CA"
    csr_format_name = Attribute('CSR Format Name', min_version='21.4')
    csr_name = Attribute('CSR Name', min_version='21.4')
    customer = Attribute('Customer', min_version='21.4')
    encryption_certificate = Attribute('Encryption Certificate', min_version='21.4')
    enrollment_mode = Attribute('Enrollment Mode', min_version='21.4')
    enterprise = Attribute('Enterprise', min_version='21.4')
    fields = Attribute('Fields', min_version='21.4')
    offer = Attribute('Offer', min_version='21.4')
    uri = Attribute('URI', min_version='21.4')
