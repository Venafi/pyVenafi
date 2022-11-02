from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CSPKeyContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "CSP Key Container"
    certificate_vault_id = Attribute('Certificate Vault Id')
    options = Attribute('Options')
    private_key_vault_id = Attribute('Private Key Vault Id')
    private_signing_key_vault_id = Attribute('Private Signing Key Vault Id')
