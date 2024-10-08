from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class CiscoCSMAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "CiscoCSM"
    create_chain_trustpoints = Attribute('Create Chain Trustpoints')
    create_new_trustpoint = Attribute('Create New Trustpoint')
    enable_credential = Attribute('Enable Credential')
    generate_new_key = Attribute('Generate New Key')
    key_created = Attribute('Key Created')
    key_pair_name = Attribute('Key Pair Name')
    trustpoint_name = Attribute('Trustpoint Name')
