from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class UserPreferenceAttributes(TopAttributes, metaclass=PropertyMeta):
	console_timeout = Attribute('Console Timeout')
	user_preferences = Attribute('User Preferences')
