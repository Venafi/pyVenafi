from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class SAMLAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SAML"
    default_profile = Attribute('Default Profile')
    logout_url = Attribute('Logout Url')
