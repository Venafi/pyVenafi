from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ACMEChallengeAttributes(TopAttributes, metaclass=PropertyMeta):
	acme_challenge_token = Attribute('ACME Challenge Token', min_version='21.2')
	acme_challenge_validated_on = Attribute('ACME Challenge Validated On', min_version='21.2')
	status = Attribute('Status', min_version='21.2')
	type = Attribute('Type', min_version='21.2')
