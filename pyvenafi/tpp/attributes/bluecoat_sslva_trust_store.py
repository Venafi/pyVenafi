from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class BlueCoatSSLVATrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "BlueCoat SSLVA Trust Store"
    create_lists = Attribute('Create Lists')
    key_store = Attribute('Key Store')
