from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.server_agent_base_device_placement_work import ServerAgentBaseDevicePlacementWorkAttributes


class ServerAgentCertDevicePlacementWorkAttributes(ServerAgentBaseDevicePlacementWorkAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
