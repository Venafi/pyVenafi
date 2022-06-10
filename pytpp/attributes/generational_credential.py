from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class GenerationalCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    last = Attribute('Last')
    visibility = Attribute('Visibility')
