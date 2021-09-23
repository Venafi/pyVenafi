from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.password_credential import PasswordCredentialAttributes


class CyberArkPasswordCredentialAttributes(PasswordCredentialAttributes, metaclass=PropertyMeta):
	account_name = Attribute('Account Name', min_version='19.3')
	application_id = Attribute('Application ID', min_version='19.3')
	folder = Attribute('Folder', min_version='19.3')
	safe = Attribute('Safe', min_version='19.3')
