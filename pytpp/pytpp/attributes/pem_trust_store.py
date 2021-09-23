from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class PEMTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	key_store = Attribute('Key Store')
