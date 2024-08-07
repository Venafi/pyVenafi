from __future__ import annotations

from datetime import datetime

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class SshWebResponse(ObjectModel):
    success: bool = ApiField(alias='Success')
    error_code: int = ApiField(alias='ErrorCode')
    error_message: str = ApiField(alias='ErrorMessage')

class ConnectionResult(ObjectModel):
    device_guid: str = ApiField(alias='DeviceGuid')
    error: str = ApiField(alias='Error')
    success: bool = ApiField(alias='Success')

class DeviceData(ObjectModel):
    dn: str = ApiField(alias='Dn')
    device_guid: str = ApiField(alias='DeviceGuid')
    host_name: str = ApiField(alias='HostName')
    is_compliant: bool = ApiField(alias='IsCompliant')
    type: str = ApiField(alias='Type')

class KeyData(ObjectModel):
    active_from: datetime = ApiField(alias='ActiveFrom')
    algorithm: str = ApiField(alias='Algorithm')
    allowed_source_restriction: list[str] = ApiField(alias='AllowedSourceRestriction', default_factory=list)
    approver: list[str] = ApiField(alias='Approver', default_factory=list)
    comment: str = ApiField(alias='Comment')
    denied_source_restriction: list[str] = ApiField(alias='DeniedSourceRestriction', default_factory=list)
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
    options: list[str] = ApiField(alias='Options', default_factory=list)
    process_error: str = ApiField(alias='ProcessError')
    process_status: str = ApiField(alias='ProcessStatus')
    reason: str = ApiField(alias='Reason')
    rotation_stage: int = ApiField(alias='RotationStage')
    type: str = ApiField(alias='Type')
    username: str = ApiField(alias='Username')
    violation_status: list[int] = ApiField(alias='ViolationStatus', default_factory=list)

class KeySetData(ObjectModel):
    access: str = ApiField(alias='Access')
    algorithm: str = ApiField(alias='Algorithm')
    fingerprint_md5: str = ApiField(alias='FingerprintMD5')
    fingerprint_sha256: str = ApiField(alias='FingerprintSHA256')
    keyset_id: str = ApiField(alias='KeysetId')
    last_rotation_date: datetime = ApiField(alias='LastRotationDate')
    last_used: datetime = ApiField(alias='LastUsed')
    length: int = ApiField(alias='Length')
    private_keys: list[KeyData] = ApiField(alias='PrivateKeys', default_factory=list)
    process_error: str = ApiField(alias='ProcessError')
    process_status: str = ApiField(alias='ProcessStatus')
    public_keys: list[KeyData] = ApiField(alias='PublicKeys', default_factory=list)
    rotation_stage: int = ApiField(alias='RotationStage')
    type: str = ApiField(alias='Type')
    violation_status: list = ApiField(alias='ViolationStatus')

class KeyUsageData(ObjectModel):
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

class SshDeviceFilter(ObjectModel):
    device_names: list[str] = ApiField(alias='DeviceNames', default_factory=list)
    is_compliant: bool = ApiField(alias='IsCompliant')
    type: str = ApiField(alias='Type')

class LogData(ObjectModel):
    log_record: str = ApiField(alias='LogRecord')
    log_utc_epoch_date: int = ApiField(alias='LogUtcEpochDate')

class KeySetFilter(ObjectModel):
    algorithm: list[str] = ApiField(alias='Algorithm')
    authorized_key_comment: list[str] = ApiField(alias='AuthorizedKeyComment')
    device_guids: list[str] = ApiField(alias='DeviceGuids')
    fingerprints_md5: list[str] = ApiField(alias='FingerprintsMD5')
    fingerprints_sha256: list[str] = ApiField(alias='FingerprintsSHA256')
    last_used: datetime = ApiField(alias='LastUsed')
    length: list[int] = ApiField(alias='Length')
    max_key_length: int = ApiField(alias='MaxKeyLength')
    process_statuses: list[int] = ApiField(alias='ProcessStatuses')
    type: str = ApiField(alias='Type')
    usage_filter_type: str = ApiField(alias='UsageFilterType')
    usernames: list[str] = ApiField(alias='Usernames')
    violation_statuses: list[int] = ApiField(alias='ViolationStatuses')

class KeyUsageFilter(ObjectModel):
    client_name: list[str] = ApiField(alias='ClientName')
    server_account: list[str] = ApiField(alias='ServerAccount')
    server_name: list[str] = ApiField(alias='ServerName')
    alert: list[int] = ApiField(alias='Alert')
