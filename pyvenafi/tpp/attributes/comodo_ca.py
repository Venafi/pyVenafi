from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class ComodoCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Comodo CA"
    address = Attribute('Address', min_version='21.4')
    company_number = Attribute('Company Number', min_version='21.4')
    domain_control_validation = Attribute('Domain Control Validation', min_version='21.4')
    domain_control_validation_email = Attribute('Domain Control Validation Email', min_version='21.4')
    postal_code = Attribute('Postal Code', min_version='21.4')
    uri = Attribute('URI', min_version='21.4')
