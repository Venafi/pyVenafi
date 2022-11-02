from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class SSHCertificateIssuanceFlowContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Certificate Issuance Flow Container"
