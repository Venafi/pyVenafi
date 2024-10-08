from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class IntermediateandRootCertificatesAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Intermediate and Root Certificates"
    cdp_aia_verification_enabled_on_creation = Attribute('CDP AIA Verification Enabled On Creation', min_version='21.4')
