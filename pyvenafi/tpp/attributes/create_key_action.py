from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class CreateKeyActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Create Key Action"
    algorithm = Attribute('Algorithm', min_version='20.2')
    key_storage_location = Attribute('Key Storage Location', min_version='20.2')
    vault_owner = Attribute('Vault Owner', min_version='20.2')
