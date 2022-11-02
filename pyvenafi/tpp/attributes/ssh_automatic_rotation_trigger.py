from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.ssh_manager import SSHManagerAttributes


class SSHAutomaticRotationTriggerAttributes(SSHManagerAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Automatic Rotation Trigger"
