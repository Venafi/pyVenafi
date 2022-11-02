from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.person import PersonAttributes


class UserAttributes(PersonAttributes, metaclass=IterableMeta):
    __config_class__ = "User"
    creation_date = Attribute('Creation Date')
    password = Attribute('Password')
