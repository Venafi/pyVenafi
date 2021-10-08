from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ClientAgentDevicePlacementWorkAttributes(ClientWorkBaseAttributes, metaclass=PropertyMeta):
	device_object_location = Attribute('Device Object Location')
	ssh_device_object_location = Attribute('SSH Device Object Location', min_version='15.2')
	ssl_device_object_location = Attribute('SSL Device Object Location', min_version='15.2')
