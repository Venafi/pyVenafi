from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class FlowActionApproverBaseAttributes(FlowActionBaseAttributes, metaclass=PropertyMeta):
	minimum_approvers = Attribute('Minimum Approvers', min_version='19.2')
