from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes

class CreateKeyActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Create Key Action"
    algorithm = Attribute('Algorithm', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    key_usage = Attribute('Key Usage', min_version='24.1')
    pkix_parameter_set = Attribute('PKIX Parameter Set')
    vault_owner = Attribute('Vault Owner', min_version='21.4')
