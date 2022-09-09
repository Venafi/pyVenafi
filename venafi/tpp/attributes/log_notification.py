from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class LogNotificationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Notification"
    log_channel = Attribute('Log Channel')
    rule = Attribute('Rule')
