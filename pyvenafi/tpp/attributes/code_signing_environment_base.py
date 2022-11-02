from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningEnvironmentBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Base"
    friendly_name = Attribute('Friendly Name', min_version='20.1')
    ip_address_restriction = Attribute('IP Address Restriction', min_version='20.1')
    key_time_constraint = Attribute('Key Time Constraint', min_version='21.2')
    key_use_authentication = Attribute('Key Use Authentication', min_version='20.1')
    key_use_flow_dn = Attribute('Key Use Flow DN', min_version='20.1')
    per_user = Attribute('Per User', min_version='20.3')
    related_items_deleted_along_with_this_environment = Attribute('Related Items Deleted Along With This Environment', min_version='22.2')
    require_justification = Attribute('Require Justification', min_version='20.1')
    status = Attribute('Status', min_version='20.3')
    template_dn = Attribute('Template DN', min_version='20.1')
    user_key_import = Attribute('User Key Import', min_version='20.3')
