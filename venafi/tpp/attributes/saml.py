from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class SAMLAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SAML"
    default_profile = Attribute('Default Profile', min_version='20.3')
    logout_url = Attribute('Logout Url', min_version='20.3')
