from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class SSHAutomaticRotationTriggerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Automatic Rotation Trigger"
