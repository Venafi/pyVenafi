from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class DigiCertCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "DigiCert CA"
    api_credentials = Attribute('API Credentials', min_version='21.4')
    api_key = Attribute('API Key', min_version='21.4')
    account_number = Attribute('Account Number', min_version='21.4')
    account_organization = Attribute('Account Organization', min_version='21.4')
    allow_reissue = Attribute('Allow Reissue', min_version='21.4')
    certificate_transparency = Attribute('Certificate Transparency', min_version='21.4')
    division = Attribute('Division', min_version='21.4')
    ev_allowed = Attribute('EV Allowed', min_version='21.4')
    ev_enabled = Attribute('EV Enabled', min_version='21.4')
    manual_approval = Attribute('Manual Approval', min_version='21.4')
    organizational_unit = Attribute('Organizational Unit', min_version='21.4')
    profile_id = Attribute('Profile ID', min_version='21.4')
    renewal_window = Attribute('Renewal Window', min_version='21.4')
    san_enabled = Attribute('SAN Enabled', min_version='21.4')
    uc_allowed = Attribute('UC Allowed', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='22.2')
    wildcard_allowed = Attribute('Wildcard Allowed', min_version='21.4')
