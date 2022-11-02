from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class GroupAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Group"
    assets = Attribute('Assets')
    closed_group = Attribute('Closed Group')
    foreign_security_principal = Attribute('Foreign Security Principal')
    full_name = Attribute('Full Name')
    group_membership = Attribute('Group Membership')
    member = Attribute('Member')
    owner = Attribute('Owner')
    products = Attribute('Products')
    suggested_member = Attribute('Suggested Member')
    team_member_added_by = Attribute('Team Member Added By')
    team_member_added_on = Attribute('Team Member Added On')
