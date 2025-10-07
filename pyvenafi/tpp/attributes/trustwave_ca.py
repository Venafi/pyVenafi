from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class TrustwaveCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Trustwave CA"
    interval = Attribute('Interval', min_version='21.4')
    reseller_id = Attribute('Reseller ID', min_version='21.4')
    retrieval_period = Attribute('Retrieval Period', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
