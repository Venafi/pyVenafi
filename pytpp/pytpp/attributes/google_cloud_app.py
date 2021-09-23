from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class GoogleCloudAppAttributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	file_validation_disabled = Attribute('File Validation Disabled', min_version='20.2')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='20.2')
	target_proxy_name = Attribute('Target Proxy Name', min_version='20.2')
	target_proxy_type = Attribute('Target Proxy Type', min_version='20.2')
	target_resource = Attribute('Target Resource', min_version='20.2')
	timeout = Attribute('Timeout', min_version='20.2')
