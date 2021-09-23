from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class BlueCoatSSLVATrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	create_lists = Attribute('Create Lists')
	key_store = Attribute('Key Store')
