from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class SSHCertificateCreateCertificateActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Certificate Create Certificate Action"
