from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import List


class PKI(PayloadModel):
    certificate_dn: str = PayloadField(alias='CertificateDn', default=None)
    certificate_guid: str = PayloadField(alias='CertificateGuid', default=None)
    pki_dn: str = PayloadField(alias='PkiDn', default=None)
    pki_guid: str = PayloadField(alias='PkiGuid', default=None)


class Certificate(PayloadModel):
    city: str = PayloadField(alias='City', default=None)
    common_name: str = PayloadField(alias='CommonName', default=None)
    country: str = PayloadField(alias='Country', default=None)
    key_algorithm: str = PayloadField(alias='KeyAlgorithm', default=None)
    key_bit_size: str = PayloadField(alias='KeyBitSize', default=None)
    organization: str = PayloadField(alias='Organization', default=None)
    organizational_units: List[str] = PayloadField(alias='OrganizationalUnits', default=None)
    sans: 'List[SANS]' = PayloadField(alias='Sans', default=None)
    state: str = PayloadField(alias='State', default=None)


class Installation(PayloadModel):
    credential_dn: str = PayloadField(alias='CredentialDn', default=None)
    host: str = PayloadField(alias='Host', default=None)


class SANS(PayloadModel):
    name: str = PayloadField(alias='Name', default=None)
    typename: str = PayloadField(alias='Typename', default=None)
