from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class LogRootAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	log_application_container = Attribute('Log Application Container')
