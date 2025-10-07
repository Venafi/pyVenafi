from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes

class CodeSigningKeyPairEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Key Pair Environment"
    key_algorithm = Attribute('Key Algorithm', min_version='21.4')
    key_dn = Attribute('Key DN', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    key_usage = Attribute('Key Usage', min_version='23.3')
    max_uses = Attribute('Max Uses', min_version='21.4')
    validity_period = Attribute('Validity Period', min_version='21.4')
