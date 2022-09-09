from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class LogHeartbeatAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Heartbeat"
    event = Attribute('Event')
    rule = Attribute('Rule')
    timeout = Attribute('Timeout')
