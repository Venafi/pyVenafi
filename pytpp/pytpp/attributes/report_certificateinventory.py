from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateInventoryAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=PropertyMeta):
	grouping = Attribute('Grouping')
	options = Attribute('Options')
	policydn = Attribute('PolicyDN')
