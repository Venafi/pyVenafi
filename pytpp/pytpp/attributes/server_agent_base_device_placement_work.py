from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ServerAgentBaseDevicePlacementWorkAttributes(ClientWorkBaseAttributes, metaclass=PropertyMeta):
	device_object_location = Attribute('Device Object Location', min_version='20.1')
	device_share_mode = Attribute('Device Share Mode', min_version='20.1')
