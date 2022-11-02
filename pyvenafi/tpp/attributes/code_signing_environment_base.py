from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningEnvironmentBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Base"
    friendly_name = Attribute('Friendly Name')
    ip_address_restriction = Attribute('IP Address Restriction')
    key_time_constraint = Attribute('Key Time Constraint')
    key_use_authentication = Attribute('Key Use Authentication')
    key_use_flow_dn = Attribute('Key Use Flow DN')
    per_user = Attribute('Per User')
    related_items_deleted_along_with_this_environment = Attribute('Related Items Deleted Along With This Environment')
    require_justification = Attribute('Require Justification')
    status = Attribute('Status')
    template_dn = Attribute('Template DN')
    user_key_import = Attribute('User Key Import')
