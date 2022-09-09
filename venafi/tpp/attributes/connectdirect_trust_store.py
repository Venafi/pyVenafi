from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class ConnectDirectTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "ConnectDirect Trust Store"
    key_store = Attribute('Key Store')
    key_store_credential = Attribute('Key Store Credential')
    node_name = Attribute('Node Name')
    protocol = Attribute('Protocol')
