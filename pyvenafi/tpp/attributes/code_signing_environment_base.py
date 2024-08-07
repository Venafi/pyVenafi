from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class CodeSigningEnvironmentBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Base"
    change_management_comment = Attribute('Change Management Comment')
    change_management_entry = Attribute('Change Management Entry')
    change_management_flow_identifier = Attribute('Change Management Flow Identifier')
    change_management_status = Attribute('Change Management Status')
    friendly_name = Attribute('Friendly Name')
    ip_address_restriction = Attribute('IP Address Restriction')
    key_time_constraint = Attribute('Key Time Constraint')
    key_use_authentication = Attribute('Key Use Authentication')
    key_use_flow_dn = Attribute('Key Use Flow DN')
    per_user = Attribute('Per User')
    prevent_use_of_expired_environment = Attribute('Prevent Use Of Expired Environment')
    related_items_deleted_along_with_this_environment = Attribute('Related Items Deleted Along With This Environment')
    require_justification = Attribute('Require Justification')
    status = Attribute('Status')
    status_message = Attribute('Status Message')
    template_dn = Attribute('Template DN')
    user_key_import = Attribute('User Key Import')
