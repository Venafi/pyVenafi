from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class SSHAutomaticRotationTriggerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Automatic Rotation Trigger"
