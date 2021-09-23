from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.flow_action_approver_base import FlowActionApproverBaseAttributes


class FlowActionDirectApproversAttributes(FlowActionApproverBaseAttributes, metaclass=PropertyMeta):
	direct_approver = Attribute('Direct Approver', min_version='19.2')
