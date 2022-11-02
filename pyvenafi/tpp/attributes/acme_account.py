from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class ACMEAccountAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "ACME Account"
    account_key_hash = Attribute('Account Key Hash')
    certificate_location_dn = Attribute('Certificate Location DN')
    internet_email_address = Attribute('Internet EMail Address')
    json_web_key = Attribute('JSON Web Key')
    public_key_vault_id = Attribute('Public Key Vault Id')
    status = Attribute('Status')
