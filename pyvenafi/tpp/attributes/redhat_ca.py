from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from pyvenafi.tpp.attributes.proxy import ProxyAttributes

class RedhatCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "Redhat CA"
    agent_port = Attribute('Agent Port', min_version='21.4')
    agent_url_surffix = Attribute('Agent URL Surffix', min_version='21.4')
    end_entity_port = Attribute('End Entity Port', min_version='21.4')
    end_entity_url_surffix = Attribute('End Entity URL Surffix', min_version='21.4')
    use_profile = Attribute('Use Profile', min_version='21.4')
