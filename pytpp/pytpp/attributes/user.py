from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.person import PersonAttributes


class UserAttributes(PersonAttributes, metaclass=PropertyMeta):
	creation_date = Attribute('Creation Date')
	password = Attribute('Password')
