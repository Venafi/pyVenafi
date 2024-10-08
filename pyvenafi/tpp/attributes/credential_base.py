from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class CredentialBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Credential Base"
    escalation_notice_interval = Attribute('Escalation Notice Interval')
    escalation_notice_start = Attribute('Escalation Notice Start')
    expiration = Attribute('Expiration')
    expiration_notice_interval = Attribute('Expiration Notice Interval')
    expiration_notice_start = Attribute('Expiration Notice Start')
    last_notification = Attribute('Last Notification')
    notified_on = Attribute('Notified On')
    protection_key = Attribute('Protection Key')
    shared = Attribute('Shared')
    vault_id = Attribute('Vault Id')
