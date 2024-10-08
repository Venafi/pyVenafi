from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class LogApplicationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Application"
    configuration = Attribute('Configuration')
    customization_data = Attribute('Customization Data')
    log_application_id = Attribute('Log Application ID')
    log_application_name = Attribute('Log Application Name')
    log_application_schema_en = Attribute('Log Application Schema EN')
