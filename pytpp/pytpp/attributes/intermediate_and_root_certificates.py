from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class IntermediateandRootCertificatesAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	cdp_aia_verification_enabled_on_creation = Attribute('CDP AIA Verification Enabled On Creation')
