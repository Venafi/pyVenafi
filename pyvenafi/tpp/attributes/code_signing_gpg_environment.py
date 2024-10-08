from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes

class CodeSigningGPGEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing GPG Environment"
    authentication_key_algorithm = Attribute('Authentication Key Algorithm', min_version='21.4')
    authentication_key_dn = Attribute('Authentication Key DN', min_version='21.4')
    encryption_key_algorithm = Attribute('Encryption Key Algorithm', min_version='21.4')
    encryption_key_dn = Attribute('Encryption Key DN', min_version='21.4')
    internet_email_address = Attribute('Internet EMail Address', min_version='21.4')
    is_issuer = Attribute('Is Issuer', min_version='22.3')
    issuer_environment_dn = Attribute('Issuer Environment DN', min_version='22.3')
    issuer_key_dn = Attribute('Issuer Key DN', min_version='21.4')
    key_storage_location = Attribute('Key Storage Location', min_version='21.4')
    max_uses = Attribute('Max Uses', min_version='21.4')
    real_name = Attribute('Real Name', min_version='21.4')
    signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='21.4')
    signing_key_dn = Attribute('Signing Key DN', min_version='21.4')
    validity_period = Attribute('Validity Period', min_version='21.4')
