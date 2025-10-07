from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes

class CodeSigningDotNetEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing DotNet Environment"
    signing_key_dn = Attribute('Signing Key DN', min_version='21.4')
