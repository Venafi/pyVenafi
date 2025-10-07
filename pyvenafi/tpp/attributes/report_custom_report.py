from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes

class ReportCustomReportAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Custom Report"
    custom_report_data_type = Attribute('Custom Report: Data Type', min_version='21.4')
    custom_report_entity_type = Attribute('Custom Report: Entity Type', min_version='21.4')
    custom_report_filter = Attribute('Custom Report: Filter', min_version='21.4')
    custom_report_order_by = Attribute('Custom Report: Order By', min_version='21.4')
    custom_report_owner = Attribute('Custom Report: Owner', min_version='21.4')
    custom_report_personalized = Attribute('Custom Report: Personalized', min_version='21.4')
    custom_report_selected_field = Attribute('Custom Report: Selected Field', min_version='21.4')
    custom_report_sort_descending = Attribute('Custom Report: Sort Descending', min_version='21.4')
    error_message = Attribute('Error Message', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
    summary = Attribute('Summary', min_version='21.4')
