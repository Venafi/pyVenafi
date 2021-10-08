from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class WorkflowRootAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	approval_reason = Attribute('Approval Reason')
	approver_not_found_expiration = Attribute('Approver Not Found Expiration', min_version='16.2')
	expiration_days = Attribute('Expiration Days')
