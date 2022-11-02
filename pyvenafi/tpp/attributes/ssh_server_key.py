from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.ssh_key import SSHKeyAttributes


class SSHServerKeyAttributes(SSHKeyAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Server Key"
    network_validation_disabled = Attribute('Network Validation Disabled')
