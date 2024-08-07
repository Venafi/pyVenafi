from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class GlobalSignMSSLCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "GlobalSign MSSL CA"
    domain_id = Attribute('Domain ID', min_version='21.4')
    profile_id = Attribute('Profile ID', min_version='21.4')
    san_type = Attribute('SAN Type', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
