from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes


class AdaptableCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Adaptable Credential"
    credential_connector = Attribute('Credential Connector')
    credential_type = Attribute('Credential Type')
    option_1 = Attribute('Option 1')
    option_2 = Attribute('Option 2')
    password_1 = Attribute('Password 1')
    text_field_1 = Attribute('Text Field 1')
    text_field_2 = Attribute('Text Field 2')
    text_field_3 = Attribute('Text Field 3')
    text_field_4 = Attribute('Text Field 4')
    text_field_5 = Attribute('Text Field 5')
