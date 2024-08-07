from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class ClientAgentSSHDiscoveryWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Agent SSH Discovery Work"
    clear_cache_timestamp = Attribute('Clear Cache Timestamp', min_version='21.4')
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    exclude_remote_mount_points = Attribute('Exclude Remote Mount Points', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    log_threshold = Attribute('Log Threshold', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    minimize_resource_use = Attribute('Minimize Resource Use', min_version='21.4')
    new_device_object_landing = Attribute('New Device Object Landing', min_version='21.4')
    ssh_scanner_service_path = Attribute('SSH Scanner Service Path', min_version='21.4')
    ssh_scanner_user_path = Attribute('SSH Scanner User Path', min_version='21.4')
    schedule_type = Attribute('Schedule Type', min_version='21.4')
    server_path_defaults_disabled = Attribute('Server Path Defaults Disabled', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    user_path_defaults_disabled = Attribute('User Path Defaults Disabled', min_version='21.4')
