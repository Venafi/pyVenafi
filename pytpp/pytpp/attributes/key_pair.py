from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.key_base import KeyBaseAttributes


class KeyPairAttributes(KeyBaseAttributes, metaclass=PropertyMeta):
	created_by = Attribute('Created By', min_version='20.3')
	key_pair_renewal_flow = Attribute('Key Pair Renewal Flow', min_version='20.2')
	original_creation_date = Attribute('Original Creation Date', min_version='20.2')
	public_key_vault_id = Attribute('Public Key Vault Id', min_version='20.2')
