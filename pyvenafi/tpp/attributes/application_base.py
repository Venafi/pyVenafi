from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes

class ApplicationBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Application Base"
    adaptable_workflow_approvers = Attribute('Adaptable Workflow Approvers', min_version='21.4')
    adaptable_workflow_reference_id = Attribute('Adaptable Workflow Reference ID', min_version='21.4')
    adaptable_workflow_stage = Attribute('Adaptable Workflow Stage', min_version='21.4')
    agent_validate_now = Attribute('Agent Validate Now', min_version='21.4')
    approver = Attribute('Approver', min_version='21.4')
    certificate = Attribute('Certificate', min_version='21.4')
    certificate_file = Attribute('Certificate File', min_version='21.4')
    certificate_installed = Attribute('Certificate Installed', min_version='21.4')
    created_by = Attribute('Created By', min_version='21.4')
    discovered_by_dn = Attribute('Discovered By DN', min_version='21.4')
    discovered_on = Attribute('Discovered On', min_version='21.4')
    file_owner_group = Attribute('File Owner: Group', min_version='21.4')
    file_owner_user = Attribute('File Owner: User', min_version='21.4')
    file_permissions_enabled = Attribute('File Permissions Enabled', min_version='21.4')
    file_permissions_group = Attribute('File Permissions: Group', min_version='21.4')
    file_permissions_user = Attribute('File Permissions: User', min_version='21.4')
    grouping_id = Attribute('Grouping Id', min_version='21.4')
    in_error = Attribute('In Error', min_version='21.4')
    in_process = Attribute('In Process', min_version='21.4')
    key_encryption_algorithm = Attribute('Key Encryption Algorithm', min_version='21.4')
    key_store_vault_id = Attribute('Key Store Vault Id', min_version='21.4')
    last_pushed_by = Attribute('Last Pushed By', min_version='21.4')
    last_pushed_on = Attribute('Last Pushed On', min_version='21.4')
    placement_id = Attribute('Placement Id', min_version='23.3')
    private_key_password_credential = Attribute('Private Key Password Credential', min_version='21.4')
    remote_one_to_many_generation = Attribute('Remote One To Many Generation', min_version='21.4')
    restart_application = Attribute('Restart Application', min_version='21.4')
    stage = Attribute('Stage', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
    ticket_dn = Attribute('Ticket DN', min_version='21.4')
