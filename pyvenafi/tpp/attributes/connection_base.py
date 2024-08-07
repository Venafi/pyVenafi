from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class ConnectionBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Connection Base"
    concurrent_connection_limit = Attribute('Concurrent Connection Limit', min_version='21.4')
    connection_method = Attribute('Connection Method', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    enforce_known_host = Attribute('Enforce Known Host', min_version='21.4')
    global_sudo = Attribute('Global sudo', min_version='21.4')
    host = Attribute('Host', min_version='21.4')
    last_known_fingerprint = Attribute('Last Known Fingerprint', min_version='21.4')
    last_known_key_type = Attribute('Last Known Key Type', min_version='21.4')
    port = Attribute('Port', min_version='21.4')
    remote_server_type = Attribute('Remote Server Type', min_version='21.4')
    secondary_credential = Attribute('Secondary Credential', min_version='21.4')
    sudo_password_delay = Attribute('Sudo Password Delay', min_version='21.4')
    temp_directory = Attribute('Temp Directory', min_version='21.4')
    terminal_columns = Attribute('Terminal Columns', min_version='21.4')
    terminal_rows = Attribute('Terminal Rows', min_version='21.4')
    terminal_type = Attribute('Terminal Type', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    trusted_fingerprint = Attribute('Trusted Fingerprint', min_version='21.4')
    trusted_key_type = Attribute('Trusted Key Type', min_version='21.4')
