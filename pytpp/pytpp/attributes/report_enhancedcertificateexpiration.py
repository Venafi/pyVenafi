from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportEnhancedCertificateExpirationAttributes(ReportBaseAttributes, metaclass=PropertyMeta):
	debug_file = Attribute('Debug File')
	grouping = Attribute('Grouping')
	options = Attribute('Options')
