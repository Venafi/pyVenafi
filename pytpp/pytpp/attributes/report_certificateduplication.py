from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateDuplicationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=PropertyMeta):
	options = Attribute('Options', min_version='19.3')
	policydn = Attribute('PolicyDN', min_version='19.3')
