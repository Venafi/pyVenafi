from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class LayoutRootAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	teams_template_code_signing_vault_id = Attribute('Teams Template Code Signing Vault Id', min_version='20.1')
	teams_template_ssh_vault_id = Attribute('Teams Template SSH Vault Id', min_version='20.1')
	teams_template_tls_vault_id = Attribute('Teams Template TLS Vault Id', min_version='20.1')
