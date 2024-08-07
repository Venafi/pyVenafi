from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes

class ApplicationBaseAttributes(
    ConnectionBaseAttributes,
    DriverBaseAttributes,
    ValidationBaseAttributes,
    metaclass=IterableMeta
):
    __config_class__ = "Application Base"
    adaptable_workflow_approvers = Attribute('Adaptable Workflow Approvers')
    adaptable_workflow_reference_id = Attribute('Adaptable Workflow Reference ID')
    adaptable_workflow_stage = Attribute('Adaptable Workflow Stage')
    agent_validate_now = Attribute('Agent Validate Now')
    approver = Attribute('Approver')
    certificate = Attribute('Certificate')
    certificate_file = Attribute('Certificate File')
    certificate_installed = Attribute('Certificate Installed')
    created_by = Attribute('Created By')
    discovered_by_dn = Attribute('Discovered By DN')
    discovered_on = Attribute('Discovered On')
    file_owner_group = Attribute('File Owner: Group')
    file_owner_user = Attribute('File Owner: User')
    file_permissions_enabled = Attribute('File Permissions Enabled')
    file_permissions_group = Attribute('File Permissions: Group')
    file_permissions_user = Attribute('File Permissions: User')
    grouping_id = Attribute('Grouping Id')
    in_error = Attribute('In Error')
    in_process = Attribute('In Process')
    key_encryption_algorithm = Attribute('Key Encryption Algorithm')
    key_store_vault_id = Attribute('Key Store Vault Id')
    last_pushed_by = Attribute('Last Pushed By')
    last_pushed_on = Attribute('Last Pushed On')
    placement_id = Attribute('Placement Id')
    private_key_password_credential = Attribute('Private Key Password Credential')
    remote_one_to_many_generation = Attribute('Remote One To Many Generation')
    restart_application = Attribute('Restart Application')
    stage = Attribute('Stage')
    status = Attribute('Status')
    ticket_dn = Attribute('Ticket DN')
