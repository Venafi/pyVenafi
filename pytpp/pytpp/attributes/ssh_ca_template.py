from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class SSHCATemplateAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH CA Template"
	allow_private_key_reuse = Attribute('Allow Private Key Reuse', min_version='21.3')
	allow_to_specify_certificate_identifier_on_request = Attribute('Allow To Specify Certificate Identifier On Request', min_version='21.2')
	allow_to_specify_extensions_on_request = Attribute('Allow To Specify Extensions On Request', min_version='21.2')
	allow_to_specify_force_command_on_request = Attribute('Allow To Specify Force Command On Request', min_version='21.2')
	allow_to_specify_principals_on_request = Attribute('Allow To Specify Principals On Request', min_version='21.2')
	allow_to_specify_source_addresses_on_request = Attribute('Allow To Specify Source Addresses On Request', min_version='21.2')
	allowed_custom_extensions = Attribute('Allowed Custom Extensions', min_version='21.3')
	allowed_extension = Attribute('Allowed Extension', min_version='21.2')
	allowed_forced_command_pattern = Attribute('Allowed Forced Command Pattern', min_version='21.2')
	allowed_principal_pattern = Attribute('Allowed Principal Pattern', min_version='21.2')
	allowed_private_key_algorithm = Attribute('Allowed Private Key Algorithm', min_version='21.2')
	allowed_source_address = Attribute('Allowed Source Address', min_version='21.2')
	certificate_container = Attribute('Certificate Container', min_version='21.2')
	certificate_identifier = Attribute('Certificate Identifier', min_version='21.2')
	certificate_type = Attribute('Certificate Type', min_version='21.2')
	extension = Attribute('Extension', min_version='21.2')
	fingerprint_sha256 = Attribute('Fingerprint SHA256', min_version='21.2')
	force_command = Attribute('Force Command', min_version='21.2')
	hash_algorithm = Attribute('Hash Algorithm', min_version='21.2')
	key_algorithm = Attribute('Key Algorithm', min_version='21.2')
	key_id_format = Attribute('Key ID Format', min_version='21.2')
	maximum_age = Attribute('Maximum Age', min_version='21.2')
	principal = Attribute('Principal', min_version='21.2')
	public_signing_key_vault_id = Attribute('Public Signing Key Vault Id', min_version='21.2')
	ssh_certificate_issuance_flow = Attribute('SSH Certificate Issuance Flow', min_version='21.2')
	signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='21.2')
	signing_key_dn = Attribute('Signing Key DN', min_version='21.2')
	source_address = Attribute('Source Address', min_version='21.2')
