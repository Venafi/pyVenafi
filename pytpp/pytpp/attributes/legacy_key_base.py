from pytpp.attributes._helper import PropertyMeta, Attribute


class LegacyKeyBaseAttributes(metaclass=PropertyMeta):
	algorithm = Attribute('Algorithm')
	approver = Attribute('Approver')
	key_bit_strength = Attribute('Key Bit Strength')
	key_vault_id = Attribute('Key Vault Id')
	protection_key = Attribute('Protection Key')
