from typing import List
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Response(PayloadModel):
    success: bool = PayloadField(alias='Success', default=None)
    error_code: int = PayloadField(alias='ErrorCode', default=None)
    error_message: str = PayloadField(alias='ErrorMessage', default=None)


class ProcessingDetails(PayloadModel):
    status: str = PayloadField(alias='Status', default=None)
    status_description: str = PayloadField(alias='StatusDescription', default=None)


class CertificateDetails(PayloadModel):
    ca_fingerprint_sha256: str = PayloadField(alias='CaFingerprintSha256', default=None)
    certificate_fingerprint_sha256: str = PayloadField(alias='CertificateFingerprintSha256', default=None)
    certificate_type: str = PayloadField(alias='CertificateType', default=None)
    extensions: dict = PayloadField(alias='Extensions', default=None)
    key_id: str = PayloadField(alias='KeyId', default=None)
    key_type: str = PayloadField(alias='KeyType', default=None)
    principals: List[str] = PayloadField(alias='Principals', default=None)
    public_key_fingerprint_sha256: str = PayloadField(alias='PublicKeyFingerprintSha256', default=None)
    serial_number: str = PayloadField(alias='SerialNumber', default=None)
    valid_from: int = PayloadField(alias='ValidFrom', default=None)
    valid_to: int = PayloadField(alias='ValidTo', default=None)


class RequestDetails(PayloadModel):
    originating_ip: str = PayloadField(alias='OriginatingIp', default=None)
    requested_by: str = PayloadField(alias='RequestedBy', default=None)


class APIClient(PayloadModel):
    allowed_to_request_certificate_identifier: bool = PayloadField(alias='AllowedToRequestCertificateIdentifier', default=None)
    allowed_to_request_extensions: bool = PayloadField(alias='AllowedToRequestExtensions', default=None)
    allowed_to_request_force_command: bool = PayloadField(alias='AllowedToRequestForceCommand', default=None)
    allowed_to_request_principals: bool = PayloadField(alias='AllowedToRequestPrincipals', default=None)
    allowed_to_request_source_addresses: bool = PayloadField(alias='AllowedToRequestSourceAddresses', default=None)


class Certificate(PayloadModel):
    allowed_private_key_algorithms: List[str] = PayloadField(alias='AllowedPrivateKeyAlgorithms', default=None)
    allowed_private_key_reuse: bool = PayloadField(alias='AllowedPrivateKeyReuse', default=None)
    certificate_destination_dn: str = PayloadField(alias='CertificateDestinationDn', default=None)
    default_private_key_algorithm: str = PayloadField(alias='DefaultPrivateKeyAlgorithm', default=None)
    signature_hashing_algorithm: str = PayloadField(alias='SignatureHashingAlgorithm', default=None)
    type: str = PayloadField(alias='Type', default=None)
    validity_period: str = PayloadField(alias='ValidityPeriod', default=None)


class CAKeyPair(PayloadModel):
    created_on: str = PayloadField(alias='CreatedOn', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    fingerprint_sha256: str = PayloadField(alias='FingerprintSha256', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    key_algorithm: str = PayloadField(alias='KeyAlgorithm', default=None)
    name: str = PayloadField(alias='Name', default=None)
    public_key_data: str = PayloadField(alias='PublicKeyData', default=None)
