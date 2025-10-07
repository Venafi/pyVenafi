from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ClientGroupBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Group Base"
    assigned_work = Attribute('Assigned Work', min_version='21.4')
    client_portal_access_identity = Attribute('Client Portal Access Identity', min_version='21.4')
    fixed_members = Attribute('Fixed Members', min_version='21.4')
    in_error = Attribute('In Error', min_version='21.4')
    rank = Attribute('Rank', min_version='21.4')
    rule = Attribute('Rule', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
