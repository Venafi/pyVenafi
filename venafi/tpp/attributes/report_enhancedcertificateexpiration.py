from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportEnhancedCertificateExpirationAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:EnhancedCertificateExpiration"
    debug_file = Attribute('Debug File')
    grouping = Attribute('Grouping')
    options = Attribute('Options')
