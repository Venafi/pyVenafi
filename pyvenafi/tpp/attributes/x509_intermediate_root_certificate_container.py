from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes

class X509IntermediateRootCertificateContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 Intermediate Root Certificate Container"
