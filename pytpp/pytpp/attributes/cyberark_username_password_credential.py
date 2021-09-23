from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.username_password_credential import UsernamePasswordCredentialAttributes


class CyberArkUsernamePasswordCredentialAttributes(UsernamePasswordCredentialAttributes, metaclass=PropertyMeta):
	account_name = Attribute('Account Name', min_version='17.2')
	application_id = Attribute('Application ID', min_version='17.2')
	folder = Attribute('Folder', min_version='17.2')
	safe = Attribute('Safe', min_version='17.2')
	username = Attribute('Username', min_version='17.2')
