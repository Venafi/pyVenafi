from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class AgentCertificateBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Agent Certificate Base"
    certificate_scanner_capi = Attribute('Certificate Scanner CAPI', min_version='21.4')
    certificate_scanner_map = Attribute('Certificate Scanner Map', min_version='21.4')
    certificate_scanner_path = Attribute('Certificate Scanner Path', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    digest = Attribute('Digest', min_version='21.4')
    exclude_remote_mount_points = Attribute('Exclude Remote Mount Points', min_version='21.4')
    expiration = Attribute('Expiration', min_version='21.4')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled', min_version='21.4')
    log_threshold = Attribute('Log Threshold', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    maximum_threads = Attribute('Maximum Threads', min_version='21.4')
