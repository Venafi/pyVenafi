from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.device import DeviceAttributes


class SSHManualInstallKeyDeviceAttributes(DeviceAttributes, metaclass=PropertyMeta):
	ssh_manual_install_key_contact_email = Attribute('SSH Manual Install Key Contact Email', min_version='18.3')
	ssh_manual_install_key_location = Attribute('SSH Manual Install Key Location', min_version='18.3')
	ssh_manual_install_key_notes = Attribute('SSH Manual Install Key Notes', min_version='18.3')
	ssh_manual_install_key_owner = Attribute('SSH Manual Install Key Owner', min_version='18.3')
