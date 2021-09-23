from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.key_base import KeyBaseAttributes


class SecretKeyAttributes(KeyBaseAttributes, metaclass=PropertyMeta):
	secret_key_renewal_flow = Attribute('Secret Key Renewal Flow', min_version='20.2')
