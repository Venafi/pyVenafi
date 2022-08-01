from typing import List
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Response(PayloadModel):
    success: bool = PayloadField(alias='Success')
    error_code: int = PayloadField(alias='ErrorCode')
    error_message: str = PayloadField(alias='ErrorMessage')


class ProcessingDetails(PayloadModel):
    status: str = PayloadField(alias='Status')
    status_description: str = PayloadField(alias='StatusDescription')


class CertificateDetails(PayloadModel):
    ca_fingerprint_sha256: str = PayloadField(alias='CaFingerprintSha256')
    certificate_fingerprint_sha256: str = PayloadField(alias='CertificateFingerprintSha256')
    certificate_type: str = PayloadField(alias='CertificateType')
    extensions: dict = PayloadField(alias='Extensions')
    key_id: str = PayloadField(alias='KeyId')
    key_type: str = PayloadField(alias='KeyType')
    principals: List[str] = PayloadField(alias='Principals')
    public_key_fingerprint_sha256: str = PayloadField(alias='PublicKeyFingerprintSha256')
    serial_number: str = PayloadField(alias='SerialNumber')
    valid_from: int = PayloadField(alias='ValidFrom')
    valid_to: int = PayloadField(alias='ValidTo')


class RequestDetails(PayloadModel):
    originating_ip: str = PayloadField(alias='OriginatingIp')
    requested_by: str = PayloadField(alias='RequestedBy')


class APIClient(PayloadModel):
    allowed_to_request_certificate_identifier: bool = PayloadField(alias='AllowedToRequestCertificateIdentifier')
    allowed_to_request_extensions: bool = PayloadField(alias='AllowedToRequestExtensions')
    allowed_to_request_force_command: bool = PayloadField(alias='AllowedToRequestForceCommand')
    allowed_to_request_principals: bool = PayloadField(alias='AllowedToRequestPrincipals')
    allowed_to_request_source_addresses: bool = PayloadField(alias='AllowedToRequestSourceAddresses')


class Certificate(PayloadModel):
    allowed_private_key_algorithms: List[str] = PayloadField(alias='AllowedPrivateKeyAlgorithms')
    allowed_private_key_reuse: bool = PayloadField(alias='AllowedPrivateKeyReuse')
    certificate_destination_dn: str = PayloadField(alias='CertificateDestinationDn')
    default_private_key_algorithm: str = PayloadField(alias='DefaultPrivateKeyAlgorithm')
    signature_hashing_algorithm: str = PayloadField(alias='SignatureHashingAlgorithm')
    type: str = PayloadField(alias='Type')
    validity_period: str = PayloadField(alias='ValidityPeriod')


class CAKeyPair(PayloadModel):
    created_on: str = PayloadField(alias='CreatedOn')
    dn: str = PayloadField(alias='Dn')
    fingerprint_sha256: str = PayloadField(alias='FingerprintSha256')
    guid: str = PayloadField(alias='Guid')
    key_algorithm: str = PayloadField(alias='KeyAlgorithm')
    name: str = PayloadField(alias='Name')
    public_key_data: str = PayloadField(alias='PublicKeyData')
