from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportAssessorAttributes(ReportBaseAttributes, metaclass=PropertyMeta):
	jobdn = Attribute('JobDN')
	options = Attribute('Options')
