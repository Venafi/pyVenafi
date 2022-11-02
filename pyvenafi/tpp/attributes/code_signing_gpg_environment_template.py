from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes


class CodeSigningGPGEnvironmentTemplateAttributes(CodeSigningEnvironmentTemplateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing GPG Environment Template"
    authentication_key_algorithm = Attribute('Authentication Key Algorithm')
    encryption_key_algorithm = Attribute('Encryption Key Algorithm')
    internet_email_address = Attribute('Internet EMail Address')
    is_issuer = Attribute('Is Issuer')
    key_container_dn = Attribute('Key Container DN')
    key_storage_location = Attribute('Key Storage Location')
    max_uses = Attribute('Max Uses')
    real_name = Attribute('Real Name')
    signing_key_algorithm = Attribute('Signing Key Algorithm')
    validity_period = Attribute('Validity Period')
