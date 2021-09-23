from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportTrustAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=PropertyMeta):
	discoverydn = Attribute('DiscoveryDN')
	grouping = Attribute('Grouping')
	options = Attribute('Options')
	trustedca = Attribute('TrustedCA')
	untrustedca = Attribute('UntrustedCA')
