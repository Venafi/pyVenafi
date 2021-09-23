from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class VamSunimpAttributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	key_list_path = Attribute('Key List Path')
	key_store_credential = Attribute('Key Store Credential')
	key_store_name = Attribute('Key Store Name')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	sca6000_utility_path = Attribute('SCA6000 Utility Path')
	sunimp_utility_path = Attribute('Sunimp Utility Path')
