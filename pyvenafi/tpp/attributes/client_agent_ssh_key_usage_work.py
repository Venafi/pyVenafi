from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.client_agent_ssh_provisioning_work import ClientAgentSSHProvisioningWorkAttributes

class ClientAgentSSHKeyUsageWorkAttributes(ClientAgentSSHProvisioningWorkAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Agent SSH Key Usage Work"
    max_row_count = Attribute('Max Row Count', min_version='21.4')
