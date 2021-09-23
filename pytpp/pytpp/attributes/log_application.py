from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogApplicationAttributes(TopAttributes, metaclass=PropertyMeta):
	configuration = Attribute('Configuration')
	log_application_id = Attribute('Log Application ID')
	log_application_name = Attribute('Log Application Name')
	log_application_schema_en = Attribute('Log Application Schema EN')
