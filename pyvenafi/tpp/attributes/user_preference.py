from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class UserPreferenceAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "User Preference"
    console_timeout = Attribute('Console Timeout')
    user_preferences = Attribute('User Preferences')
