from pytpp.attributes._helper import PropertyMeta, Attribute


class DiscoveryStatisticsAttributes(metaclass=PropertyMeta):
	certificates_found = Attribute('Certificates Found')
	completed_scans = Attribute('Completed Scans')
	connect_succeeded = Attribute('Connect Succeeded')
	keys_found = Attribute('Keys Found')
