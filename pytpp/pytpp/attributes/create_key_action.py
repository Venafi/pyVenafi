from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class CreateKeyActionAttributes(FlowActionBaseAttributes, metaclass=PropertyMeta):
	algorithm = Attribute('Algorithm', min_version='20.2')
	key_storage_location = Attribute('Key Storage Location', min_version='20.2')
	vault_owner = Attribute('Vault Owner', min_version='20.2')
