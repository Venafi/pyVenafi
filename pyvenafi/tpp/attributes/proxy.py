from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ProxyAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Proxy"
    bypass_proxy_on_local = Attribute('Bypass Proxy on Local', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    proxy_credential = Attribute('Proxy Credential', min_version='21.4')
    proxy_host = Attribute('Proxy Host', min_version='21.4')
    proxy_port = Attribute('Proxy Port', min_version='21.4')
    proxy_use_host_configuration = Attribute('Proxy Use Host Configuration', min_version='21.4')
