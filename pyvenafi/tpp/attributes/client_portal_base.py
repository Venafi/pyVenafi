from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class ClientPortalBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Client Portal Base"
    client_field_mapping = Attribute('Client Field Mapping', min_version='21.4')
    client_portal_access_enabled = Attribute('Client Portal Access Enabled', min_version='21.4')
