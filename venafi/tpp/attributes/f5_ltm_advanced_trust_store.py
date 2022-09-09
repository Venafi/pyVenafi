from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class F5LTMAdvancedTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "F5 LTM Advanced Trust Store"
    certificate_name = Attribute('Certificate Name')
    ssh_port = Attribute('SSH Port')
    use_rest_api = Attribute('Use REST API', min_version='22.1')
