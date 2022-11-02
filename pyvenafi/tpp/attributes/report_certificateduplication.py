from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateDuplicationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:CertificateDuplication"
    options = Attribute('Options', min_version='19.3')
    policydn = Attribute('PolicyDN', min_version='19.3')
