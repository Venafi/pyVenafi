from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class AdaptableAppAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Adaptable App"
    allow_push_without_private_key = Attribute('Allow Push Without Private Key', min_version='21.4')
    certificate_name = Attribute('Certificate Name', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    installation_status = Attribute('Installation Status', min_version='21.4')
    log_debug = Attribute('Log Debug', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    option_1 = Attribute('Option 1', min_version='21.4')
    option_2 = Attribute('Option 2', min_version='21.4')
    pbes2_algorithm = Attribute('PBES2 Algorithm', min_version='21.4')
    pk_credential = Attribute('PK Credential', min_version='21.4')
    password_1 = Attribute('Password 1', min_version='21.4')
    powershell_script = Attribute('PowerShell Script', min_version='21.4')
    powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='21.4')
    retry_after_script_hash_mismatch = Attribute('Retry After Script Hash Mismatch', min_version='21.4')
    script_execution_timeout = Attribute('Script Execution Timeout', min_version='21.4')
    script_hash_mismatch_error = Attribute('Script Hash Mismatch Error', min_version='21.4')
    secondary_credential = Attribute('Secondary Credential', min_version='21.4')
    text_field_1 = Attribute('Text Field 1', min_version='21.4')
    text_field_2 = Attribute('Text Field 2', min_version='21.4')
    text_field_3 = Attribute('Text Field 3', min_version='21.4')
    text_field_4 = Attribute('Text Field 4', min_version='21.4')
    text_field_5 = Attribute('Text Field 5', min_version='21.4')
