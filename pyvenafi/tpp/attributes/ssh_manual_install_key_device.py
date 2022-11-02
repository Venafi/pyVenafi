from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.device import DeviceAttributes


class SSHManualInstallKeyDeviceAttributes(DeviceAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Manual Install Key Device"
    ssh_manual_install_key_contact_email = Attribute('SSH Manual Install Key Contact Email')
    ssh_manual_install_key_location = Attribute('SSH Manual Install Key Location')
    ssh_manual_install_key_notes = Attribute('SSH Manual Install Key Notes')
    ssh_manual_install_key_owner = Attribute('SSH Manual Install Key Owner')
