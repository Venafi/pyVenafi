from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.x509_certificate import X509CertificateAttributes


class X509UserCertificateAttributes(X509CertificateAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 User Certificate"
