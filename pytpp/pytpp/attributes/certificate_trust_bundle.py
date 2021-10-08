from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CertificateTrustBundleAttributes(TopAttributes, metaclass=PropertyMeta):
	excluded_certificates = Attribute('Excluded Certificates')
	included_certificates = Attribute('Included Certificates')
	is_match = Attribute('Is Match')
