from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class SSHManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Manager"
    escalation_notice_interval = Attribute('Escalation Notice Interval', min_version='21.4')
    escalation_notice_start = Attribute('Escalation Notice Start', min_version='21.4')
    expiration_notice_interval = Attribute('Expiration Notice Interval', min_version='21.4')
    expiration_notice_start = Attribute('Expiration Notice Start', min_version='21.4')
    renewal_window = Attribute('Renewal Window', min_version='21.4')
    renewal_window_event = Attribute('Renewal Window Event', min_version='21.4')
