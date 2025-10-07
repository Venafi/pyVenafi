from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class SANS(ObjectModel):
    name: str = ApiField(alias='Name')
    type_name: str = ApiField(alias='TypeName')

class PKI(ObjectModel):
    certificate_dn: str = ApiField(alias='CertificateDn')
    certificate_guid: str = ApiField(alias='CertificateGuid')
    pki_dn: str = ApiField(alias='PkiDn')
    pki_guid: str = ApiField(alias='PkiGuid')

class Certificate(ObjectModel):
    city: str = ApiField(alias='City')
    common_name: str = ApiField(alias='CommonName')
    country: str = ApiField(alias='Country')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_bit_size: str = ApiField(alias='KeyBitSize')
    organization: str = ApiField(alias='Organization')
    organizational_units: list[str] = ApiField(alias='OrganizationalUnits', default_factory=list)
    pkix_parameter_set: str = ApiField(alias='PkixParameterSet')
    sans: list[SANS] = ApiField(alias='Sans', default_factory=list)
    state: str = ApiField(alias='State')

class Installation(ObjectModel):
    credential_dn: str = ApiField(alias='CredentialDn')
    host: str = ApiField(alias='Host')
    port: str = ApiField(alias='Port')
