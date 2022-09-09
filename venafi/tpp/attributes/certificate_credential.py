from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.credential_base import CredentialBaseAttributes


class CertificateCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Credential"
    certificate = Attribute('Certificate')
