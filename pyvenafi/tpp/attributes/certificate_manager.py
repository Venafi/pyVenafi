from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class CertificateManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Manager"
    cdp_aia_verification_disabled = Attribute('CDP AIA Verification Disabled', min_version='21.4')
    certificate_api_todo_timeout = Attribute('Certificate API ToDo Timeout', min_version='21.4')
    certificate_retrieve_cache = Attribute('Certificate Retrieve Cache', min_version='22.4')
    escalation_notice_interval = Attribute('Escalation Notice Interval', min_version='21.4')
    escalation_notice_start = Attribute('Escalation Notice Start', min_version='21.4')
    expiration_notice_interval = Attribute('Expiration Notice Interval', min_version='21.4')
    expiration_notice_start = Attribute('Expiration Notice Start', min_version='21.4')
    maximum_threads = Attribute('Maximum Threads', min_version='21.4')
    minimum_threads = Attribute('Minimum Threads', min_version='21.4')
    renewal_window = Attribute('Renewal Window', min_version='21.4')
    renewal_window_event = Attribute('Renewal Window Event', min_version='21.4')
    revocation_check_disabled = Attribute('Revocation Check Disabled', min_version='21.4')
    service_module_classes = Attribute('Service Module Classes', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    trust_store_management_disabled = Attribute('Trust Store Management Disabled', min_version='21.4')
