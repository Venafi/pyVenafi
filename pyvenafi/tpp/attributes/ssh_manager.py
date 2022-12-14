from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class SSHManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Manager"
    escalation_notice_interval = Attribute('Escalation Notice Interval')
    escalation_notice_start = Attribute('Escalation Notice Start')
    expiration_notice_interval = Attribute('Expiration Notice Interval')
    expiration_notice_start = Attribute('Expiration Notice Start')
    renewal_window = Attribute('Renewal Window')
    renewal_window_event = Attribute('Renewal Window Event')
