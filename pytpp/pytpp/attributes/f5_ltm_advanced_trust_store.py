from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class F5LTMAdvancedTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=PropertyMeta):
	certificate_name = Attribute('Certificate Name')
	ssh_port = Attribute('SSH Port')
