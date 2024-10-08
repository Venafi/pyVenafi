from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ACMEOrderAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "ACME Order"
    acme_authorization_dn = Attribute('ACME Authorization DN', min_version='21.4')
    acme_expires = Attribute('ACME Expires', min_version='21.4')
    acme_not_after = Attribute('ACME Not After', min_version='21.4')
    acme_not_before = Attribute('ACME Not Before', min_version='21.4')
    csr_vault_id = Attribute('CSR Vault Id', min_version='21.4')
    certificate = Attribute('Certificate', min_version='21.4')
    error = Attribute('Error', min_version='21.4')
    identifier = Attribute('Identifier', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
