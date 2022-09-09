from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class SSHCertificateIssuanceFlowContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Certificate Issuance Flow Container"
