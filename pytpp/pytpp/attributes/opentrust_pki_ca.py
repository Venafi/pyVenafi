from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class OpenTrustPKICAAttributes(HTTPCABaseAttributes, metaclass=PropertyMeta):
	connector_type = Attribute('Connector Type')
	fields = Attribute('Fields')
	retrieval_period = Attribute('Retrieval Period')
	web_service_url = Attribute('Web Service URL')
