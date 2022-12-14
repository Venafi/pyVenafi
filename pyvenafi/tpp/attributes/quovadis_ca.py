from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes


class QuoVadisCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "QuoVadis CA"
    api_credentials = Attribute('API Credentials')
    account_name = Attribute('Account Name')
    account_organization = Attribute('Account Organization')
    certificate_type = Attribute('Certificate Type', min_version='15.4')
    subscriber_email = Attribute('Subscriber Email')
    ui_credentials = Attribute('UI Credentials')
    web_service_url = Attribute('Web Service URL')
    web_ui_url = Attribute('Web UI URL')
