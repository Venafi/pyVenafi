from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes


class GoogleCloudCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Google Cloud CA"
    certificate_authority_id = Attribute('Certificate Authority ID')
    google_project_name = Attribute('Google Project Name')
    region = Attribute('Region')
