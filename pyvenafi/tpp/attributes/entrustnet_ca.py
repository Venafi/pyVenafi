from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class EntrustNETCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "EntrustNET CA"
    allow_reissue = Attribute('Allow Reissue', min_version='21.4')
    certificate_block = Attribute('Certificate Block', min_version='21.4')
    certificate_transparency = Attribute('Certificate Transparency', min_version='21.4')
    enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    organization = Attribute('Organization', min_version='21.4')
    retrieval_period = Attribute('Retrieval Period', min_version='21.4')
    use_default_organization = Attribute('Use Default Organization', min_version='21.4')
    username_credential = Attribute('Username Credential', min_version='21.4')
    web_service_url = Attribute('Web Service URL', min_version='21.4')
