from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class CodeSignPreApprovalActionAttributes(FlowActionBaseAttributes, metaclass=PropertyMeta):
	stage_identifier = Attribute('Stage Identifier', min_version='20.2')
