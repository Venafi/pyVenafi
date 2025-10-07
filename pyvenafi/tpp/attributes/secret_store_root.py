from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class SecretStoreRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Secret Store Root"
    certificate_protection_key = Attribute('Certificate Protection Key', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    driver_name = Attribute('Driver Name', min_version='21.4')
    non_authoritative_classes = Attribute('Non-Authoritative Classes', min_version='21.4')
    pkcs8_association = Attribute('PKCS8 Association', min_version='21.4')
    x509certificate_association = Attribute('X509Certificate Association', min_version='21.4')
