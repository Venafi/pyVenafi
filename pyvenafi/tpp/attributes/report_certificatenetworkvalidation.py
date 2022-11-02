from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateNetworkValidationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:CertificateNetworkValidation"
    certificateslimit = Attribute('CertificatesLimit')
    grouping = Attribute('Grouping')
    options = Attribute('Options')
    policydn = Attribute('PolicyDN')
