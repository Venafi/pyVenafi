from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportEntitlementAttributes(ReportBaseAttributes, metaclass=PropertyMeta):
	options = Attribute('Options')
	policydn = Attribute('PolicyDN', min_version='16.1')
