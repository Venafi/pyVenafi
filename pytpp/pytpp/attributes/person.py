from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class PersonAttributes(TopAttributes, metaclass=PropertyMeta):
	full_name = Attribute('Full Name')
	given_name = Attribute('Given Name')
	group_membership = Attribute('Group Membership')
	internet_email_address = Attribute('Internet EMail Address')
	language = Attribute('Language')
	surname = Attribute('Surname')
