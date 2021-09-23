from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CSPKeyContainerAttributes(TopAttributes, metaclass=PropertyMeta):
	certificate_vault_id = Attribute('Certificate Vault Id', min_version='19.2')
	options = Attribute('Options', min_version='19.2')
	private_key_vault_id = Attribute('Private Key Vault Id', min_version='19.2')
	private_signing_key_vault_id = Attribute('Private Signing Key Vault Id', min_version='19.2')
