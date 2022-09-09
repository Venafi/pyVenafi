from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class AssociateKeyExpirationActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Associate Key Expiration Action"
