from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.server_agent_base_device_placement_work import ServerAgentBaseDevicePlacementWorkAttributes


class ServerAgentSSHDevicePlacementWorkAttributes(ServerAgentBaseDevicePlacementWorkAttributes, metaclass=IterableMeta):
    __config_class__ = "Server Agent SSH Device Placement Work"
