from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class EncryptionDriverAttributes(DriverBaseAttributes, metaclass=PropertyMeta):
	encryption_data = Attribute('Encryption Data')
