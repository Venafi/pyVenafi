from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.x509_certificate import X509CertificateAttributes


class X509ServerCertificateAttributes(X509CertificateAttributes, metaclass=PropertyMeta):
	pass