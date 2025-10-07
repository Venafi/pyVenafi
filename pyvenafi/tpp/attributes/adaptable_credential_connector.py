from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.credential_driver_base import CredentialDriverBaseAttributes

class AdaptableCredentialConnectorAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Adaptable Credential Connector"
    credential = Attribute('Credential', min_version='21.4')
    powershell_script = Attribute('PowerShell Script', min_version='21.4')
    powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
