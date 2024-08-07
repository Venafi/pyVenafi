from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class PersonAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Person"
    full_name = Attribute('Full Name', min_version='21.4')
    given_name = Attribute('Given Name', min_version='21.4')
    group_membership = Attribute('Group Membership', min_version='21.4')
    internet_email_address = Attribute('Internet EMail Address', min_version='21.4')
    language = Attribute('Language', min_version='21.4')
    surname = Attribute('Surname', min_version='21.4')
