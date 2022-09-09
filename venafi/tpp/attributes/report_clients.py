from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportClientsAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Clients"
