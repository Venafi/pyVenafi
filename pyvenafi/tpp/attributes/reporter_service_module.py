from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class ReporterServiceModuleAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Reporter Service Module"
    host = Attribute('Host', min_version='21.4')
    log_delivery = Attribute('Log Delivery', min_version='21.4')
    max_running_reports = Attribute('Max Running Reports', min_version='21.4')
    render_options = Attribute('Render Options', min_version='21.4')
    report_execution_timeout = Attribute('Report Execution Timeout', min_version='21.4')
    report_max_source_record_count = Attribute('Report Max Source Record Count', min_version='21.4')
    smtp_credentials = Attribute('SMTP Credentials', min_version='21.4')
    secure = Attribute('Secure', min_version='21.4')
    sender = Attribute('Sender', min_version='21.4')
