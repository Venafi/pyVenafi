from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.organization import OrganizationAttributes


class IdentityRootAttributes(OrganizationAttributes, metaclass=PropertyMeta):
	authentication_scheme = Attribute('Authentication Scheme')
	identity_cache_timeout = Attribute('Identity Cache Timeout', min_version='16.2')
