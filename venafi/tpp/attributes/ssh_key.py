from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.agent_base import AgentBaseAttributes
from venafi.tpp.attributes.driver_base import DriverBaseAttributes
from venafi.tpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from venafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes


class SSHKeyAttributes(AgentBaseAttributes, DriverBaseAttributes, LegacyKeyBaseAttributes, MonitoringBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Key"
    public_key_vault_id = Attribute('Public Key Vault Id')
