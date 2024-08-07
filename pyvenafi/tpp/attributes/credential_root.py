from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class CredentialRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Credential Root"
    escalation_notice_interval = Attribute('Escalation Notice Interval', min_version='21.4')
    escalation_notice_start = Attribute('Escalation Notice Start', min_version='21.4')
    expiration_notice_interval = Attribute('Expiration Notice Interval', min_version='21.4')
    expiration_notice_start = Attribute('Expiration Notice Start', min_version='21.4')
    protection_key = Attribute('Protection Key', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
