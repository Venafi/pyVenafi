from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_driver_base import CredentialDriverBaseAttributes


class CyberArkCredentialsDriverAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CyberArk Credentials Driver"
	scim_server_url = Attribute('SCIM Server URL', min_version='19.3')
	scim_server_user = Attribute('SCIM Server User', min_version='19.3')
	use_proxy = Attribute('Use Proxy', min_version='18.1')
	web_service_url = Attribute('Web Service URL', min_version='17.2')
	web_service_user = Attribute('Web Service User', min_version='17.2')
