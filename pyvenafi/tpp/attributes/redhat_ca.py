from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from pyvenafi.tpp.attributes.proxy import ProxyAttributes


class RedhatCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "Redhat CA"
    agent_port = Attribute('Agent Port')
    agent_url_surffix = Attribute('Agent URL Surffix')
    end_entity_port = Attribute('End Entity Port')
    end_entity_url_surffix = Attribute('End Entity URL Surffix')
    use_profile = Attribute('Use Profile')
