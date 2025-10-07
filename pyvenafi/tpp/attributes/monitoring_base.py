from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class MonitoringBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Monitoring Base"
    creation_date = Attribute('Creation Date', min_version='21.4')
    escalation_notice_interval = Attribute('Escalation Notice Interval', min_version='21.4')
    escalation_notice_start = Attribute('Escalation Notice Start', min_version='21.4')
    expiration_notice_interval = Attribute('Expiration Notice Interval', min_version='21.4')
    expiration_notice_start = Attribute('Expiration Notice Start', min_version='21.4')
    last_notification = Attribute('Last Notification', min_version='21.4')
    notes = Attribute('Notes', min_version='21.4')
    notification_disabled = Attribute('Notification Disabled', min_version='21.4')
    notified_on = Attribute('Notified On', min_version='24.1')
    validity_period = Attribute('Validity Period', min_version='21.4')
