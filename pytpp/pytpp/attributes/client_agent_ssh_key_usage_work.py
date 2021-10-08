from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.client_agent_ssh_provisioning_work import ClientAgentSSHProvisioningWorkAttributes


class ClientAgentSSHKeyUsageWorkAttributes(ClientAgentSSHProvisioningWorkAttributes, metaclass=PropertyMeta):
	max_row_count = Attribute('Max Row Count')
