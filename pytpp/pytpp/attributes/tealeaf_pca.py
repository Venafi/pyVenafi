from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class TealeafPCAAttributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	file_validation_disabled = Attribute('File Validation Disabled')
	install_path = Attribute('Install Path')
