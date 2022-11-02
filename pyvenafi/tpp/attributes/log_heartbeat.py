from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LogHeartbeatAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Heartbeat"
    event = Attribute('Event')
    rule = Attribute('Rule')
    timeout = Attribute('Timeout')
