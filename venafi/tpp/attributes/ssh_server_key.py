from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.ssh_key import SSHKeyAttributes
from venafi.tpp.attributes.validation_base import ValidationBaseAttributes


class SSHServerKeyAttributes(SSHKeyAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Server Key"
    network_validation_disabled = Attribute('Network Validation Disabled')
