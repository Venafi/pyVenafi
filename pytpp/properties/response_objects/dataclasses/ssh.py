from typing import List
from datetime import datetime
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Response(PayloadModel):
    success: bool = PayloadField(alias='Success', default=None)
    error_code: int = PayloadField(alias='ErrorCode', default=None)
    error_message: str = PayloadField(alias='ErrorMessage', default=None)


class ConnectionResult(PayloadModel):
    device_guid: str = PayloadField(alias='DeviceGuid', default=None)
    error: str = PayloadField(alias='Error', default=None)
    success: bool = PayloadField(alias='Success', default=None)


class DeviceData(PayloadModel):
    dn: str = PayloadField(alias='Dn', default=None)
    device_guid: str = PayloadField(alias='DeviceGuid', default=None)
    host_name: str = PayloadField(alias='HostName', default=None)
    is_compliant: bool = PayloadField(alias='IsCompliant', default=None)
    type: str = PayloadField(alias='Type', default=None)


class KeyData(PayloadModel):
    active_from: datetime = PayloadField(alias='ActiveFrom', default=None)
    algorithm: str = PayloadField(alias='Algorithm', default=None)
    allowed_source_restriction: List[str] = PayloadField(alias='AllowedSourceRestriction', default=None)
    approver: List[str] = PayloadField(alias='Approver', default=None)
    comment: str = PayloadField(alias='Comment', default=None)
    denied_source_restriction: List[str] = PayloadField(alias='DeniedSourceRestriction', default=None)
    device_guid: str = PayloadField(alias='DeviceGuid', default=None)
    filepath: str = PayloadField(alias='Filepath', default=None)
    forced_command: str = PayloadField(alias='ForcedCommand', default=None)
    format: str = PayloadField(alias='Format', default=None)
    is_encrypted: bool = PayloadField(alias='IsEncrypted', default=None)
    key_id: int = PayloadField(alias='KeyId', default=None)
    keysetid: str = PayloadField(alias='Keysetid', default=None)
    last_used: datetime = PayloadField(alias='LastUsed', default=None)
    length: int = PayloadField(alias='Length', default=None)
    notes: str = PayloadField(alias='Notes', default=None)
    options: List[str] = PayloadField(alias='Options', default=None)
    process_error: str = PayloadField(alias='ProcessError', default=None)
    process_status: str = PayloadField(alias='ProcessStatus', default=None)
    reason: str = PayloadField(alias='Reason', default=None)
    rotation_stage: int = PayloadField(alias='RotationStage', default=None)
    type: str = PayloadField(alias='Type', default=None)
    username: str = PayloadField(alias='Username', default=None)
    violation_status: List[int] = PayloadField(alias='ViolationStatus', default=None)


class KeySetData(PayloadModel):
    access: str = PayloadField(alias='Access', default=None)
    algorithm: str = PayloadField(alias='Algorithm', default=None)
    fingerprint_md5: str = PayloadField(alias='FingerprintMd5', default=None)
    fingerprint_sha256: str = PayloadField(alias='FingerprintSha256', default=None)
    keysetid: str = PayloadField(alias='Keysetid', default=None)
    last_rotation_date: datetime = PayloadField(alias='LastRotationDate', default=None)
    last_used: datetime = PayloadField(alias='LastUsed', default=None)
    length: int = PayloadField(alias='Length', default=None)
    private_keys: 'List[KeyData]' = PayloadField(alias='PrivateKeys', default=None)
    process_error: str = PayloadField(alias='ProcessError', default=None)
    process_status: str = PayloadField(alias='ProcessStatus', default=None)
    public_keys: 'List[KeyData]' = PayloadField(alias='PublicKeys', default=None)
    rotation_stage: int = PayloadField(alias='RotationStage', default=None)
    type: str = PayloadField(alias='Type', default=None)
    violation_status: list = PayloadField(alias='ViolationStatus', default=None)


class KeyUsageData(PayloadModel):
    alert: int = PayloadField(alias='Alert', default=None)
    authorized_key_id: int = PayloadField(alias='AuthorizedKeyId', default=None)
    client_name: str = PayloadField(alias='ClientName', default=None)
    fingerprint: str = PayloadField(alias='Fingerprint', default=None)
    key_usage_id: int = PayloadField(alias='KeyUsageId', default=None)
    keyset_id: str = PayloadField(alias='KeysetId', default=None)
    last_used: datetime = PayloadField(alias='LastUsed', default=None)
    private_key_id: int = PayloadField(alias='PrivateKeyId', default=None)
    server_account: str = PayloadField(alias='ServerAccount', default=None)
    server_name: str = PayloadField(alias='ServerName', default=None)
