from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class AgentSSHBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Agent SSH Base"
    credential = Attribute('Credential', min_version='21.4')
    exclude_remote_mount_points = Attribute('Exclude Remote Mount Points', min_version='21.4')
    expiration = Attribute('Expiration', min_version='21.4')
    file_scan_disabled = Attribute('File Scan Disabled', min_version='21.4')
    log_threshold = Attribute('Log Threshold', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    min_filesize = Attribute('Min Filesize', min_version='21.4')
    port_validation_disabled = Attribute('Port Validation Disabled', min_version='21.4')
    ssh_scanner_service_path = Attribute('SSH Scanner Service Path', min_version='21.4')
    ssh_scanner_user_path = Attribute('SSH Scanner User Path', min_version='21.4')
    sshd_filename_filter = Attribute('SSHd Filename Filter', min_version='21.4')
    sshd_max_filesize = Attribute('SSHd Max Filesize', min_version='21.4')
    server_path_defaults_disabled = Attribute('Server Path Defaults Disabled', min_version='21.4')
    upload_private_keys_disabled = Attribute('Upload Private Keys Disabled', min_version='21.4')
    user_path_defaults_disabled = Attribute('User Path Defaults Disabled', min_version='21.4')
