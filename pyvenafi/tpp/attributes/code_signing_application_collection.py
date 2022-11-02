from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningApplicationCollectionAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Application Collection"
    code_signing_application_dn = Attribute('Code Signing Application DN')
