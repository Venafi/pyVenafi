from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogSNMPAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log SNMP"
    community = Attribute('Community', min_version='21.4')
    message_body = Attribute('Message Body', min_version='21.4')
    snmp_authentication_password = Attribute('SNMP Authentication Password', min_version='21.4')
    snmp_authentication_protocol = Attribute('SNMP Authentication Protocol', min_version='21.4')
    snmp_engine_id = Attribute('SNMP Engine ID', min_version='21.4')
    snmp_privacy_password = Attribute('SNMP Privacy Password', min_version='21.4')
    snmp_privacy_protocol = Attribute('SNMP Privacy Protocol', min_version='21.4')
    snmp_username = Attribute('SNMP Username', min_version='21.4')
    snmp_v3_mode = Attribute('SNMP V3 Mode', min_version='21.4')
    snmp_version = Attribute('SNMP Version', min_version='21.4')
    target = Attribute('Target', min_version='21.4')
    trap_oid = Attribute('Trap OID', min_version='21.4')
