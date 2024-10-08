from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class JuniperSASAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Juniper SAS"
    external_port = Attribute('External Port')
    file_validation_disabled = Attribute('File Validation Disabled')
    internal_port = Attribute('Internal Port')
    network_validation_disabled = Attribute('Network Validation Disabled')
    reassign_ports = Attribute('Reassign Ports')
    vlan_port = Attribute('Vlan Port')
