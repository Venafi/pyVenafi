from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class LayoutRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Root"
    teams_template_code_signing_vault_id = Attribute('Teams Template Code Signing Vault Id', min_version='21.4')
    teams_template_ssh_vault_id = Attribute('Teams Template SSH Vault Id', min_version='21.4')
    teams_template_tls_vault_id = Attribute('Teams Template TLS Vault Id', min_version='21.4')
