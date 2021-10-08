from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class JKSTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	key_store = Attribute('Key Store')
	key_store_credential = Attribute('Key Store Credential')
	store_type = Attribute('Store Type')
