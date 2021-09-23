from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ClientGroupBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	assigned_work = Attribute('Assigned Work')
	client_portal_access_identity = Attribute('Client Portal Access Identity', min_version='15.2')
	fixed_members = Attribute('Fixed Members')
	in_error = Attribute('In Error')
	rank = Attribute('Rank')
	rule = Attribute('Rule')
	status = Attribute('Status')
