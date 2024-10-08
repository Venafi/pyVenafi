from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.ssh_device_base import SshDeviceBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes

class DeviceAttributes(
    ConnectionBaseAttributes,
    SshDeviceBaseAttributes,
    TopAttributes,
    ValidationBaseAttributes,
    metaclass=IterableMeta
):
    __config_class__ = "Device"
    adaptable_script_max_file_size = Attribute('Adaptable Script Max File Size')
    agentless_discovery_stage = Attribute('Agentless Discovery Stage')
    agentless_discovery_status = Attribute('Agentless Discovery Status')
    allow_adaptable_discovery = Attribute('Allow Adaptable Discovery')
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
    log_debug = Attribute('Log Debug')
    manual_approval = Attribute('Manual Approval')
    maximum_authorizations_per_keyset = Attribute('Maximum Authorizations Per Keyset')
    oauth_token_application_id = Attribute('OAuth Token Application Id')
    oauth_token_credential = Attribute('OAuth Token Credential')
    oauth_token_scope = Attribute('OAuth Token Scope')
    onboard_discovery_dn = Attribute('Onboard Discovery Dn')
    onboard_discovery_stage = Attribute('Onboard Discovery Stage')
    onboard_discovery_status = Attribute('Onboard Discovery Status')
    onboard_discovery_to_do = Attribute('Onboard Discovery To Do')
    pbes2_algorithm = Attribute('PBES2 Algorithm')
    placement_id = Attribute('Placement Id')
    placement_job_dn = Attribute('Placement Job Dn')
    powershell_script = Attribute('PowerShell Script')
    powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id')
    previous_connection_credential_hash = Attribute('Previous Connection Credential Hash')
    privilege_elevation_command = Attribute('Privilege Elevation Command')
    progress = Attribute('Progress')
    protection_key = Attribute('Protection Key')
    required_sync_confirmation = Attribute('Required Sync Confirmation')
    restricted_pbes2_algorithms = Attribute('Restricted PBES2 Algorithms')
    ssh_key_encryption = Attribute('SSH Key Encryption')
    script_execution_timeout = Attribute('Script Execution Timeout')
    status = Attribute('Status')
    system_owned_keys = Attribute('System Owned Keys')
    text_field_1 = Attribute('Text Field 1')
    text_field_10 = Attribute('Text Field 10')
    text_field_11 = Attribute('Text Field 11')
    text_field_12 = Attribute('Text Field 12')
    text_field_2 = Attribute('Text Field 2')
    text_field_3 = Attribute('Text Field 3')
    text_field_4 = Attribute('Text Field 4')
    text_field_5 = Attribute('Text Field 5')
    text_field_6 = Attribute('Text Field 6')
    text_field_7 = Attribute('Text Field 7')
    text_field_8 = Attribute('Text Field 8')
    text_field_9 = Attribute('Text Field 9')
