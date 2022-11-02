from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningGPGEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing GPG Environment"
    authentication_key_algorithm = Attribute('Authentication Key Algorithm')
    authentication_key_dn = Attribute('Authentication Key DN')
    encryption_key_algorithm = Attribute('Encryption Key Algorithm')
    encryption_key_dn = Attribute('Encryption Key DN')
    internet_email_address = Attribute('Internet EMail Address')
    is_issuer = Attribute('Is Issuer')
    issuer_environment_dn = Attribute('Issuer Environment DN')
    issuer_key_dn = Attribute('Issuer Key DN')
    key_storage_location = Attribute('Key Storage Location')
    max_uses = Attribute('Max Uses')
    real_name = Attribute('Real Name')
    signing_key_algorithm = Attribute('Signing Key Algorithm')
    signing_key_dn = Attribute('Signing Key DN')
    validity_period = Attribute('Validity Period')
