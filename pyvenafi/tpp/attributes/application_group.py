from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class ApplicationGroupAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Application Group"
    certificate = Attribute('Certificate')
    common_data_location = Attribute('Common Data Location')
    common_data_vault_id = Attribute('Common Data Vault Id')
    enrollment_application_dn = Attribute('Enrollment Application DN')
    primary_application_dn = Attribute('Primary Application DN')
    private_key_stub_vault_id = Attribute('Private Key Stub Vault Id')
