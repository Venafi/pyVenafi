from pytpp.attributes._helper import PropertyMeta, Attribute


class ReportFilterBaseAttributes(metaclass=PropertyMeta):
	address = Attribute('Address')
	discoverydn = Attribute('DiscoveryDN')
	grouping = Attribute('Grouping')
	longrunning = Attribute('LongRunning', min_version='16.4')
	policydn = Attribute('PolicyDN')
	reporton = Attribute('ReportOn')
	selectedcontacts = Attribute('SelectedContacts')
