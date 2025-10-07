from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.organization import OrganizationAttributes

class PolicyAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Policy"
    certificate_origin = Attribute('Certificate Origin', min_version='21.4')
    log_view_server = Attribute('Log View Server', min_version='21.4')
    master_preferences = Attribute('Master Preferences', min_version='21.4')
    scep_ca_ident = Attribute('Scep CA Ident', min_version='21.4')
    scep_certificate_authority = Attribute('Scep Certificate Authority', min_version='21.4')
    scep_challenge_password = Attribute('Scep Challenge Password', min_version='21.4')
    scep_encryption_ra_certificate = Attribute('Scep Encryption RA Certificate', min_version='21.4')
    scep_intune_application_id = Attribute('Scep Intune Application Id', min_version='21.4')
    scep_intune_application_secret = Attribute('Scep Intune Application Secret', min_version='21.4')
    scep_intune_tenant_name = Attribute('Scep Intune Tenant Name', min_version='21.4')
    scep_ra_certificate = Attribute('Scep RA Certificate', min_version='21.4')
    scep_selection_rule = Attribute('Scep Selection Rule', min_version='21.4')
    scep_signing_ra_certificate = Attribute('Scep Signing RA Certificate', min_version='21.4')
