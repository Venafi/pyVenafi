from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningCSPEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=PropertyMeta):
	encryption_key_dn = Attribute('Encryption Key DN', min_version='20.2')
	signing_key_dn = Attribute('Signing Key DN', min_version='20.2')
