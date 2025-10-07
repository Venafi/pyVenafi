from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.person import PersonAttributes

class UserAttributes(PersonAttributes, metaclass=IterableMeta):
    __config_class__ = "User"
    creation_date = Attribute('Creation Date', min_version='21.4')
    password = Attribute('Password', min_version='21.4')
