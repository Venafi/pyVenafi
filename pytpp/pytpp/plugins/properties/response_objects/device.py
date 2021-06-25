from pytpp.tools.helpers.date_converter import from_date_string
from typing import List

class Device:
    def __init__(self, response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        self.guid = response_object.get('guid') # type: str
        self.name = response_object.get('name') # type: str
        self.dn = response_object.get('dn') # type: str
        self.environment = response_object.get('environment')
        self.is_scanned = response_object.get('isScanned')  # type: bool
        self.is_agent = response_object.get('isAgent')  # type: bool
        self.interface = response_object.get('interface')  # type: str
        self.platform = response_object.get('platform')  # type: str
        self.state = response_object.get('state')  # type: str
        self.trusted_users = response_object.get('trustedUsers')  # type: int
        self.trusted_root_users = response_object.get('trustedRootUsers')  # type: int
        self.server_access = response_object.get('serverAccess')  # type: int
        self.root_server_access = response_object.get('rootServerAccess')  # type: int
        self.custom_fields = response_object.get('customFields')
        self.scan_status = response_object.get('scanStatus')  # type: str
        self.last_discovery = from_date_string(response_object.get('lastDiscovery'))
        self.connection_errors = response_object.get('connectionErrors')  # type: List[str]
        self.is_write_allowed = response_object.get('isWriteAllowed')  # type: bool
        self.has_failed_authorization_attempts = response_object.get('hasFailedAuthorizationAttempts')  # type: bool



