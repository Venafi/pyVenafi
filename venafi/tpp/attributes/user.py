from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.person import PersonAttributes


class UserAttributes(PersonAttributes, metaclass=IterableMeta):
    __config_class__ = "User"
    creation_date = Attribute('Creation Date')
    password = Attribute('Password')
