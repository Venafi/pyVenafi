from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes

class GoogleCloudCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Google Cloud CA"
    certificate_authority_id = Attribute('Certificate Authority ID', min_version='21.4')
    google_project_name = Attribute('Google Project Name', min_version='22.3')
    region = Attribute('Region', min_version='21.4')
