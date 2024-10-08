from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.username_password_credential import UsernamePasswordCredentialAttributes

class CyberArkUsernamePasswordCredentialAttributes(UsernamePasswordCredentialAttributes, metaclass=IterableMeta):
    __config_class__ = "CyberArk Username Password Credential"
    account_name = Attribute('Account Name', min_version='21.4')
    application_id = Attribute('Application ID', min_version='21.4')
    folder = Attribute('Folder', min_version='21.4')
    safe = Attribute('Safe', min_version='21.4')
    username = Attribute('Username', min_version='21.4')
