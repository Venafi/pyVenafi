from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class OpenTrustPKICAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "OpenTrust PKI CA"
    connector_type = Attribute('Connector Type', min_version='21.4')
    fields = Attribute('Fields', min_version='21.4')
    retrieval_period = Attribute('Retrieval Period', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
