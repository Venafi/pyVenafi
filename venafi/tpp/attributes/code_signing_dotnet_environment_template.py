from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes


class CodeSigningDotNetEnvironmentTemplateAttributes(CodeSigningEnvironmentTemplateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing DotNet Environment Template"
    key_container_dn = Attribute('Key Container DN', min_version='20.2')
    key_storage_location = Attribute('Key Storage Location', min_version='20.2')
    max_uses = Attribute('Max Uses', min_version='20.2')
    signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='20.2')
    validity_period = Attribute('Validity Period', min_version='20.2')