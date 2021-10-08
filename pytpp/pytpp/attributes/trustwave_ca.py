from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class TrustwaveCAAttributes(HTTPCABaseAttributes, metaclass=PropertyMeta):
	interval = Attribute('Interval')
	reseller_id = Attribute('Reseller ID')
	retrieval_period = Attribute('Retrieval Period')
	web_service_url = Attribute('Web Service URL')
