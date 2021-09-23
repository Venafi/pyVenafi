from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class VamSCA6000Attributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	key_list_path = Attribute('Key List Path')
	sca6000_utility_path = Attribute('SCA6000 Utility Path')
