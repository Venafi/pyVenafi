from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ACMEAuthorizationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "ACME Authorization"
    acme_auth_id_type = Attribute('ACME Auth ID Type', min_version='21.4')
    acme_auth_id_value = Attribute('ACME Auth ID Value', min_version='21.4')
    acme_challenge_dn = Attribute('ACME Challenge DN', min_version='21.4')
    acme_challenge_token = Attribute('ACME Challenge Token', min_version='21.4')
    acme_challenge_validated_on = Attribute('ACME Challenge Validated On', min_version='21.4')
    acme_expires = Attribute('ACME Expires', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
