from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class GSKTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	fips_key = Attribute('Fips Key', min_version='15.2')
	key_store = Attribute('Key Store', min_version='15.2')
	key_store_credential = Attribute('Key Store Credential', min_version='15.2')
	stash_password = Attribute('Stash Password', min_version='15.2')
