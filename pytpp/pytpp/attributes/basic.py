from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class BasicAttributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	certificate_file = Attribute('Certificate File', min_version='15.2')
	network_validation_disabled = Attribute('Network Validation Disabled')
