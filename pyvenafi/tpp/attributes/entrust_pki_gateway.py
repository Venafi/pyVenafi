from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class EntrustPKIGatewayAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Entrust PKI Gateway"
    ca_capabilities = Attribute('CA Capabilities', min_version='21.4')
    ca_name = Attribute('CA Name', min_version='21.4')
    exclude_subjectvariables = Attribute('Exclude SubjectVariables', min_version='21.4')
    profile_capabilities = Attribute('Profile Capabilities', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
