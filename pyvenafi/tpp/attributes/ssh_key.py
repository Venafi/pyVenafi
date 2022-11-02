from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.agent_base import AgentBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from pyvenafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes
from pyvenafi.tpp.attributes.device import DeviceAttributes


class SSHKeyAttributes(AgentBaseAttributes, DriverBaseAttributes, LegacyKeyBaseAttributes, MonitoringBaseAttributes, DeviceAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Key"
    public_key_vault_id = Attribute('Public Key Vault Id')
