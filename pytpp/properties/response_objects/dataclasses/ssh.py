from typing import List
from datetime import datetime
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Response(PayloadModel):
    success: bool = PayloadField(alias='Success')
    error_code: int = PayloadField(alias='ErrorCode')
    error_message: str = PayloadField(alias='ErrorMessage')


class ConnectionResult(PayloadModel):
    device_guid: str = PayloadField(alias='DeviceGuid')
    error: str = PayloadField(alias='Error')
    success: bool = PayloadField(alias='Success')


class DeviceData(PayloadModel):
    dn: str = PayloadField(alias='Dn')
    device_guid: str = PayloadField(alias='DeviceGuid')
    host_name: str = PayloadField(alias='HostName')
    is_compliant: bool = PayloadField(alias='IsCompliant')
    type: str = PayloadField(alias='Type')


class KeyData(PayloadModel):
    active_from: datetime = PayloadField(alias='ActiveFrom')
    algorithm: str = PayloadField(alias='Algorithm')
    allowed_source_restriction: List[str] = PayloadField(alias='AllowedSourceRestriction')
    approver: List[str] = PayloadField(alias='Approver')
    comment: str = PayloadField(alias='Comment')
    denied_source_restriction: List[str] = PayloadField(alias='DeniedSourceRestriction')
    device_guid: str = PayloadField(alias='DeviceGuid')
    filepath: str = PayloadField(alias='Filepath')
    fingerprint_md5: str = PayloadField(alias='FingerprintMD5')
    fingerprint_sha256: str = PayloadField(alias='FingerprintSHA256')
    force_command: str = PayloadField(alias='ForceCommand')
    format: str = PayloadField(alias='Format')
    is_encrypted: bool = PayloadField(alias='IsEncrypted')
    key_id: int = PayloadField(alias='KeyId')
    keysetid: str = PayloadField(alias='Keysetid')
    last_used: datetime = PayloadField(alias='LastUsed')
    length: int = PayloadField(alias='Length')
    notes: str = PayloadField(alias='Notes')
    options: List[str] = PayloadField(alias='Options')
    process_error: str = PayloadField(alias='ProcessError')
    process_status: str = PayloadField(alias='ProcessStatus')
    reason: str = PayloadField(alias='Reason')
    rotation_stage: int = PayloadField(alias='RotationStage')
    type: str = PayloadField(alias='Type')
    username: str = PayloadField(alias='Username')
    violation_status: List[int] = PayloadField(alias='ViolationStatus')


class KeySetData(PayloadModel):
    access: str = PayloadField(alias='Access')
    algorithm: str = PayloadField(alias='Algorithm')
    fingerprint_md5: str = PayloadField(alias='FingerprintMd5')
    fingerprint_sha256: str = PayloadField(alias='FingerprintSha256')
    keyset_id: str = PayloadField(alias='Keysetid')
    last_rotation_date: datetime = PayloadField(alias='LastRotationDate')
    last_used: datetime = PayloadField(alias='LastUsed')
    length: int = PayloadField(alias='Length')
    private_keys: 'List[KeyData]' = PayloadField(alias='PrivateKeys')
    process_error: str = PayloadField(alias='ProcessError')
    process_status: str = PayloadField(alias='ProcessStatus')
    public_keys: 'List[KeyData]' = PayloadField(alias='PublicKeys')
    rotation_stage: int = PayloadField(alias='RotationStage')
    type: str = PayloadField(alias='Type')
    violation_status: list = PayloadField(alias='ViolationStatus')


class KeyUsageData(PayloadModel):
    alert: int = PayloadField(alias='Alert')
    authorized_key_id: int = PayloadField(alias='AuthorizedKeyId')
    client_name: str = PayloadField(alias='ClientName')
    fingerprint: str = PayloadField(alias='Fingerprint')
    key_usage_id: int = PayloadField(alias='KeyUsageId')
    keyset_id: str = PayloadField(alias='KeysetId')
    last_used: datetime = PayloadField(alias='LastUsed')
    private_key_id: int = PayloadField(alias='PrivateKeyId')
    server_account: str = PayloadField(alias='ServerAccount')
    server_name: str = PayloadField(alias='ServerName')
