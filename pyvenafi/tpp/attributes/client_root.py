from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class ClientRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Root"
    client_enrollment_anonymous_allowed = Attribute('Client Enrollment Anonymous Allowed', min_version='21.4')
    client_enrollment_default_owner = Attribute('Client Enrollment Default Owner', min_version='21.4')
    client_enrollment_secret_allowed = Attribute('Client Enrollment Secret Allowed', min_version='21.4')
    client_enrollment_secret_dn = Attribute('Client Enrollment Secret DN', min_version='21.4')
    client_portal_signing_certificate = Attribute('Client Portal Signing Certificate', min_version='21.4')
    client_trust_certificate_dn = Attribute('Client Trust Certificate DN', min_version='21.4')
    client_trust_update = Attribute('Client Trust Update', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    driver_name = Attribute('Driver Name', min_version='21.4')
    environment_variables = Attribute('Environment Variables', min_version='21.4')
    identity_variables = Attribute('Identity Variables', min_version='21.4')
    mac_ignore_list = Attribute('MAC Ignore List', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
    rolling_code_tolerance = Attribute('Rolling Code Tolerance', min_version='21.4')
    rule = Attribute('Rule', min_version='21.4')
    trust_level = Attribute('Trust Level', min_version='21.4')
