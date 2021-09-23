from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHUserKeyAttributes(ReportBaseAttributes, metaclass=PropertyMeta):
	options = Attribute('Options')
