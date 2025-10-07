from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.organization import OrganizationAttributes

class IdentityRootAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Identity Root"
    authentication_scheme = Attribute('Authentication Scheme', min_version='21.4')
    identity_cache_timeout = Attribute('Identity Cache Timeout', min_version='21.4')
