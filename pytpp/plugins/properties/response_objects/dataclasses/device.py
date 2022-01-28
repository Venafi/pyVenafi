from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Device:
    guid: str
    name: str
    dn: str
    environment: str
    is_scanned: bool
    is_agent: bool
    interface: str
    platform: str
    state: str
    trusted_users: int
    trusted_root_users: int
    server_access: int
    root_server_access: int
    custom_fields: dict
    scan_status: str
    last_discovery: datetime
    connection_errors: List[str]
    is_write_allowed: bool
    has_failed_authorization_attempts: bool
