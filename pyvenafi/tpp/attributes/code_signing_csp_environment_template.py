from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes

class CodeSigningCSPEnvironmentTemplateAttributes(CodeSigningEnvironmentTemplateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing CSP Environment Template"
    encryption_key_algorithm = Attribute('Encryption Key Algorithm', min_version='21.4')
    key_container_dn = Attribute('Key Container DN', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    max_uses = Attribute('Max Uses', min_version='21.4')
    signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='21.4')
    validity_period = Attribute('Validity Period', min_version='21.4')
