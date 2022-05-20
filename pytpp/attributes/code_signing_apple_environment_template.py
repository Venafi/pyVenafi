from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes


class CodeSigningAppleEnvironmentTemplateAttributes(CodeSigningEnvironmentTemplateBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Apple Environment Template"
	cn_pattern = Attribute('CN Pattern', min_version='21.2')
	certificate_authority = Attribute('Certificate Authority', min_version='22.1')
	certificate_container_dn = Attribute('Certificate Container DN', min_version='21.2')
	key_container_dn = Attribute('Key Container DN', min_version='21.2')
	key_storage_location = Attribute('Key Storage Location', min_version='21.2')
	max_uses = Attribute('Max Uses', min_version='21.2')
	validity_period = Attribute('Validity Period', min_version='21.2')
