from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class PaloAltoNetworkFWTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	lock_config = Attribute('Lock Config', min_version='15.1')
