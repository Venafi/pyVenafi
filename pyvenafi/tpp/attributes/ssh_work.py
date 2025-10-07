from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class SSHWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Work"
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    exclude_remote_mount_points = Attribute('Exclude Remote Mount Points', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    new_device_object_landing = Attribute('New Device Object Landing', min_version='21.4')
    remediation_interval = Attribute('Remediation Interval', min_version='21.4')
    remediation_schedule_type = Attribute('Remediation Schedule Type', min_version='21.4')
    remediation_start_time = Attribute('Remediation Start Time', min_version='21.4')
    ssh_scanner_service_path = Attribute('SSH Scanner Service Path', min_version='21.4')
    ssh_scanner_user_path = Attribute('SSH Scanner User Path', min_version='21.4')
    schedule_type = Attribute('Schedule Type', min_version='21.4')
    server_path_defaults_disabled = Attribute('Server Path Defaults Disabled', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    user_path_defaults_disabled = Attribute('User Path Defaults Disabled', min_version='21.4')
