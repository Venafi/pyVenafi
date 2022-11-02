from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes


class HydrantIdv2CAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "HydrantIdv2 CA"
    api_credentials = Attribute('API Credentials', min_version='22.3')
