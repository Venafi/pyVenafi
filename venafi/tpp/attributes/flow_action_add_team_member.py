from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class FlowActionAddTeamMemberAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Action Add Team Member"
