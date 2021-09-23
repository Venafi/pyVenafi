from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class VamCaviumAttributes(ApplicationBaseAttributes, metaclass=PropertyMeta):
	cavium_utility_path = Attribute('Cavium Utility Path')
	key_list_path = Attribute('Key List Path')
