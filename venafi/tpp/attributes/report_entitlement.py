from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportEntitlementAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Entitlement"
    options = Attribute('Options')
    policydn = Attribute('PolicyDN', min_version='16.1')
