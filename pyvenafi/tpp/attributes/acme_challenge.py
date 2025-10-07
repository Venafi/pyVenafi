from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ACMEChallengeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "ACME Challenge"
    acme_challenge_token = Attribute('ACME Challenge Token', min_version='21.4')
    acme_challenge_validated_on = Attribute('ACME Challenge Validated On', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
    type = Attribute('Type', min_version='21.4')
