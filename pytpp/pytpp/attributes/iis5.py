from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class IIS5Attributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	site_id = Attribute('Site Id')
