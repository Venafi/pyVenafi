from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.plugins.properties.response_objects.dataclasses import device


def Device(response_object: dict):
    if not isinstance(response_object, dict):
        response_object = {}
    return device.Device(
        guid=response_object.get('guid'),
        name=response_object.get('name'),
        dn=response_object.get('dn'),
        environment=response_object.get('environment'),
        is_scanned=response_object.get('isScanned'),
        is_agent=response_object.get('isAgent'),
        interface=response_object.get('interface'),
        platform=response_object.get('platform'),
        state=response_object.get('state'),
        trusted_users=response_object.get('trustedUsers'),
        trusted_root_users=response_object.get('trustedRootUsers'),
        server_access=response_object.get('serverAccess'),
        root_server_access=response_object.get('rootServerAccess'),
        custom_fields=response_object.get('customFields'),
        scan_status=response_object.get('scanStatus'),
        last_discovery=from_date_string(response_object.get('lastDiscovery')),
        connection_errors=response_object.get('connectionErrors'),
        is_write_allowed=response_object.get('isWriteAllowed'),
        has_failed_authorization_attempts=response_object.get('hasFailedAuthorizationAttempts'),

    )
