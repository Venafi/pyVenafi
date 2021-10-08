from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportAnalyticsAttributes(ReportBaseAttributes, metaclass=PropertyMeta):
	options = Attribute('Options', min_version='17.1')
