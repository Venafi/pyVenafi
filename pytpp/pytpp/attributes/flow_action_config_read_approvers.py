from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.flow_action_approver_base import FlowActionApproverBaseAttributes


class FlowActionConfigReadApproversAttributes(FlowActionApproverBaseAttributes, metaclass=PropertyMeta):
	attribute_name = Attribute('Attribute Name', min_version='19.2')
	object_dn = Attribute('Object DN', min_version='19.2')
	policy_read = Attribute('Policy Read', min_version='19.2')
	use_administrators_as_fallback_approvers = Attribute('Use Administrators as Fallback Approvers', min_version='20.2')
