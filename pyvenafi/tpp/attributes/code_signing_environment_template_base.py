from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class CodeSigningEnvironmentTemplateBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Template Base"
    environment_template_update_flow_dn = Attribute('Environment Template Update Flow DN', min_version='21.4')
    flow_instance_macro = Attribute('Flow Instance Macro', min_version='21.4')
    key_use_authentication = Attribute('Key Use Authentication', min_version='21.4')
    key_use_flow_dn = Attribute('Key Use Flow DN', min_version='21.4')
    naming_pattern = Attribute('Naming Pattern', min_version='21.4')
    per_user = Attribute('Per User', min_version='21.4')
    require_justification = Attribute('Require Justification', min_version='21.4')
    user_key_import = Attribute('User Key Import', min_version='21.4')
    visible_to = Attribute('Visible To', min_version='21.4')
