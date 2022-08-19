from __future__ import annotations
from typing import List
from datetime import datetime
from pytpp.api.api_base import OutputModel, ApiField


class SshWebResponse(OutputModel):
    success: bool = ApiField(alias='Success')
    error_code: int = ApiField(alias='ErrorCode')
    error_message: str = ApiField(alias='ErrorMessage')


class ConnectionResult(OutputModel):
    device_guid: str = ApiField(alias='DeviceGuid')
    error: str = ApiField(alias='Error')
    success: bool = ApiField(alias='Success')


class DeviceData(OutputModel):
    dn: str = ApiField(alias='Dn')
    device_guid: str = ApiField(alias='DeviceGuid')
    host_name: str = ApiField(alias='HostName')
    is_compliant: bool = ApiField(alias='IsCompliant')
    type: str = ApiField(alias='Type')


class KeyData(OutputModel):
    active_from: datetime = ApiField(alias='ActiveFrom')
    algorithm: str = ApiField(alias='Algorithm')
    allowed_source_restriction: List[str] = ApiField(alias='AllowedSourceRestriction', default_factory=list)
    approver: List[str] = ApiField(alias='Approver', default_factory=list)
    comment: str = ApiField(alias='Comment')
    denied_source_restriction: List[str] = ApiField(alias='DeniedSourceRestriction', default_factory=list)
    device_guid: str = ApiField(alias='DeviceGuid')
    filepath: str = ApiField(alias='Filepath')
    fingerprint_md5: str = ApiField(alias='FingerprintMD5')
    fingerprint_sha256: str = ApiField(alias='FingerprintSHA256')
    force_command: str = ApiField(alias='ForceCommand')
    format: str = ApiField(alias='Format')
    is_encrypted: bool = ApiField(alias='IsEncrypted')
    key_id: int = ApiField(alias='KeyId')
    keysetid: str = ApiField(alias='KeysetId')
    last_used: datetime = ApiField(alias='LastUsed')
    length: int = ApiField(alias='Length')
    notes: str = ApiField(alias='Notes')
    options: List[str] = ApiField(alias='Options', default_factory=list)
    process_error: str = ApiField(alias='ProcessError')
    process_status: str = ApiField(alias='ProcessStatus')
    reason: str = ApiField(alias='Reason')
    rotation_stage: int = ApiField(alias='RotationStage')
    type: str = ApiField(alias='Type')
    username: str = ApiField(alias='Username')
    violation_status: List[int] = ApiField(alias='ViolationStatus', default_factory=list)


class KeySetData(OutputModel):
    access: str = ApiField(alias='Access')
    algorithm: str = ApiField(alias='Algorithm')
    fingerprint_md5: str = ApiField(alias='FingerprintMD5')
    fingerprint_sha256: str = ApiField(alias='FingerprintSHA256')
    keyset_id: str = ApiField(alias='KeysetId')
    last_rotation_date: datetime = ApiField(alias='LastRotationDate')
    last_used: datetime = ApiField(alias='LastUsed')
    length: int = ApiField(alias='Length')
    private_keys: List[KeyData] = ApiField(alias='PrivateKeys', default_factory=list)
    process_error: str = ApiField(alias='ProcessError')
    process_status: str = ApiField(alias='ProcessStatus')
    public_keys: List[KeyData] = ApiField(alias='PublicKeys', default_factory=list)
    rotation_stage: int = ApiField(alias='RotationStage')
    type: str = ApiField(alias='Type')
    violation_status: list = ApiField(alias='ViolationStatus')


class KeyUsageData(OutputModel):
    alert: int = ApiField(alias='Alert')
    authorized_key_id: int = ApiField(alias='AuthorizedKeyId')
    client_name: str = ApiField(alias='ClientName')
    fingerprint: str = ApiField(alias='Fingerprint')
    key_usage_id: int = ApiField(alias='KeyUsageId')
    keyset_id: str = ApiField(alias='KeysetId')
    last_used: datetime = ApiField(alias='LastUsed')
    private_key_id: int = ApiField(alias='PrivateKeyId')
    server_account: str = ApiField(alias='ServerAccount')
    server_name: str = ApiField(alias='ServerName')
