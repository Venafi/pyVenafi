from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import List


class SANS(PayloadModel):
    name: str = PayloadField(alias='Name')
    typename: str = PayloadField(alias='Typename')


class PKI(PayloadModel):
    certificate_dn: str = PayloadField(alias='CertificateDn')
    certificate_guid: str = PayloadField(alias='CertificateGuid')
    pki_dn: str = PayloadField(alias='PkiDn')
    pki_guid: str = PayloadField(alias='PkiGuid')


class Certificate(PayloadModel):
    city: str = PayloadField(alias='City')
    common_name: str = PayloadField(alias='CommonName')
    country: str = PayloadField(alias='Country')
    key_algorithm: str = PayloadField(alias='KeyAlgorithm')
    key_bit_size: str = PayloadField(alias='KeyBitSize')
    organization: str = PayloadField(alias='Organization')
    organizational_units: List[str] = PayloadField(alias='OrganizationalUnits')
    sans: List[SANS] = PayloadField(alias='Sans')
    state: str = PayloadField(alias='State')


class Installation(PayloadModel):
    credential_dn: str = PayloadField(alias='CredentialDn')
    host: str = PayloadField(alias='Host')
