from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class ClientCertificateDiscoveryWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Certificate Discovery Work"
    certificate_location_dn = Attribute('Certificate Location DN', min_version='21.4')
    certificate_scanner_capi = Attribute('Certificate Scanner CAPI', min_version='21.4')
    certificate_scanner_map = Attribute('Certificate Scanner Map', min_version='21.4')
    certificate_scanner_native = Attribute('Certificate Scanner Native', min_version='21.4')
    certificate_scanner_native_stores = Attribute('Certificate Scanner Native Stores', min_version='21.4')
    certificate_scanner_path = Attribute('Certificate Scanner Path', min_version='21.4')
    clear_cache_timestamp = Attribute('Clear Cache Timestamp', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    device_location_dn = Attribute('Device Location DN', min_version='21.4')
    discovery_container = Attribute('Discovery Container', min_version='21.4')
    exclude_remote_mount_points = Attribute('Exclude Remote Mount Points', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    log_threshold = Attribute('Log Threshold', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    minimize_resource_use = Attribute('Minimize Resource Use', min_version='21.4')
    naming_pattern = Attribute('Naming Pattern', min_version='21.4')
    placement_rule = Attribute('Placement Rule', min_version='21.4')
    placement_summary = Attribute('Placement Summary', min_version='21.4')
    schedule_type = Attribute('Schedule Type', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    treat_unknown_roots_as_self_signed = Attribute('Treat Unknown Roots As Self Signed', min_version='21.4')
