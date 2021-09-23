from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.ssh_key import SSHKeyAttributes
from pytpp.attributes.validation_base import ValidationBaseAttributes


class SSHServerKeyAttributes(SSHKeyAttributes, ValidationBaseAttributes, metaclass=PropertyMeta):
	network_validation_disabled = Attribute('Network Validation Disabled')
