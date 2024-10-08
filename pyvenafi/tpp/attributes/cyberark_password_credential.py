from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.password_credential import PasswordCredentialAttributes

class CyberArkPasswordCredentialAttributes(PasswordCredentialAttributes, metaclass=IterableMeta):
    __config_class__ = "CyberArk Password Credential"
    account_name = Attribute('Account Name', min_version='21.4')
    application_id = Attribute('Application ID', min_version='21.4')
    folder = Attribute('Folder', min_version='21.4')
    safe = Attribute('Safe', min_version='21.4')
