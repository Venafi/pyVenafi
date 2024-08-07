from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes

class CodeSigningCSPEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing CSP Environment"
    encryption_key_dn = Attribute('Encryption Key DN', min_version='21.4')
    signing_key_dn = Attribute('Signing Key DN', min_version='21.4')
