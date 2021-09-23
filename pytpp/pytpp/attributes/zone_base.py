from pytpp.attributes._helper import PropertyMeta, Attribute


class ZoneBaseAttributes(metaclass=PropertyMeta):
	address_range = Attribute('Address Range')
	window_end = Attribute('Window End')
	window_start = Attribute('Window Start')
	zone_contact = Attribute('Zone Contact')
	zone_description = Attribute('Zone Description')
