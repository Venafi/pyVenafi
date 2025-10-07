from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class QuoVadisCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "QuoVadis CA"
    api_credentials = Attribute('API Credentials', min_version='21.4')
    account_name = Attribute('Account Name', min_version='21.4')
    account_organization = Attribute('Account Organization', min_version='21.4')
    certificate_type = Attribute('Certificate Type', min_version='21.4')
    subscriber_email = Attribute('Subscriber Email', min_version='21.4')
    ui_credentials = Attribute('UI Credentials', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
    web_ui_url = Attribute('Web UI URL', min_version='21.4')
