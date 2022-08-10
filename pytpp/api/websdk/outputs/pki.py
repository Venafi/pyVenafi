from pytpp.api.api_base import OutputModel, ApiField
from typing import List


class SANS(OutputModel):
    name: str = ApiField(alias='Name')
    typename: str = ApiField(alias='Typename')


class PKI(OutputModel):
    certificate_dn: str = ApiField(alias='CertificateDn')
    certificate_guid: str = ApiField(alias='CertificateGuid')
    pki_dn: str = ApiField(alias='PkiDn')
    pki_guid: str = ApiField(alias='PkiGuid')


class Certificate(OutputModel):
    city: str = ApiField(alias='City')
    common_name: str = ApiField(alias='CommonName')
    country: str = ApiField(alias='Country')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_bit_size: str = ApiField(alias='KeyBitSize')
    organization: str = ApiField(alias='Organization')
    organizational_units: List[str] = ApiField(alias='OrganizationalUnits')
    sans: List[SANS] = ApiField(alias='Sans')
    state: str = ApiField(alias='State')


class Installation(OutputModel):
    credential_dn: str = ApiField(alias='CredentialDn')
    host: str = ApiField(alias='Host')
