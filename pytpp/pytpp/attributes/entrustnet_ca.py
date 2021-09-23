from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class EntrustNETCAAttributes(HTTPCABaseAttributes, metaclass=PropertyMeta):
	allow_reissue = Attribute('Allow Reissue', min_version='16.4')
	certificate_block = Attribute('Certificate Block')
	certificate_transparency = Attribute('Certificate Transparency', min_version='18.4')
	enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='18.4')
	interval = Attribute('Interval', min_version='15.4')
	organization = Attribute('Organization')
	retrieval_period = Attribute('Retrieval Period', min_version='15.4')
	use_default_organization = Attribute('Use Default Organization', min_version='18.2')
	username_credential = Attribute('Username Credential')
	web_service_url = Attribute('Web Service URL')
