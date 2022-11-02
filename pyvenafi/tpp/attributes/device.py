from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.ssh_device_base import SshDeviceBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes


class DeviceAttributes(ConnectionBaseAttributes, SshDeviceBaseAttributes, TopAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Device"
    agentless_discovery_stage = Attribute('Agentless Discovery Stage')
    agentless_discovery_status = Attribute('Agentless Discovery Status')
    allow_agentless_discovery_and_remediation = Attribute('Allow Agentless Discovery and Remediation')
    approver = Attribute('Approver')
    bulk_provisioning_dn = Attribute('Bulk Provisioning Dn')
    bulk_provisioning_stage = Attribute('Bulk Provisioning Stage')
    bulk_provisioning_status = Attribute('Bulk Provisioning Status')
    client_id = Attribute('Client ID')
    client_machine_id = Attribute('Client Machine ID')
    cloud_instance_id = Attribute('Cloud Instance ID')
    cloud_region = Attribute('Cloud Region')
    cloud_service = Attribute('Cloud Service')
    created_by = Attribute('Created By')
    deny_multiple_authentication_failures = Attribute('Deny Multiple Authentication Failures')
    disabled_on = Attribute('Disabled On')
    discovered_by_dn = Attribute('Discovered By DN')
    jump_server_dn = Attribute('Jump Server DN')
    last_attempt_to_get_client_subsystem_record = Attribute('Last Attempt To Get Client Subsystem Record')
    last_discovery_date = Attribute('Last Discovery Date')
    last_discovery_planned = Attribute('Last Discovery Planned')
    last_discovery_platform_version = Attribute('Last Discovery Platform Version')
    last_file_operations_platform_version = Attribute('Last File Operations Platform Version')
    location = Attribute('Location')
    manual_approval = Attribute('Manual Approval')
    maximum_authorizations_per_keyset = Attribute('Maximum Authorizations Per Keyset')
    onboard_discovery_dn = Attribute('Onboard Discovery Dn')
    onboard_discovery_stage = Attribute('Onboard Discovery Stage')
    onboard_discovery_status = Attribute('Onboard Discovery Status')
    onboard_discovery_to_do = Attribute('Onboard Discovery To Do')
    placement_job_dn = Attribute('Placement Job Dn')
    previous_connection_credential_hash = Attribute('Previous Connection Credential Hash')
    privilege_elevation_command = Attribute('Privilege Elevation Command')
    protection_key = Attribute('Protection Key')
    required_sync_confirmation = Attribute('Required Sync Confirmation')
    ssh_key_encryption = Attribute('SSH Key Encryption')
    status = Attribute('Status')
    system_owned_keys = Attribute('System Owned Keys')
