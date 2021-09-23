from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportExpirationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=PropertyMeta):
	options = Attribute('Options')
