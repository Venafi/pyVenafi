from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from typing import List, Dict
from datetime import datetime

"""
    "access": "auto-user-53@auto-user-53-128-0-0-18-30005 → many",
    "accessAndName": {
        "mainText": "auto-user-53@auto-user-53-128-0-0-18-30005 → many",
        "subText": null,
        "link": "sshKeyset/details/0000D72EC33C33BA03CA9DAA41C0EA9B36DAF175"
    },
    "algorithm": "ssh-rsa",
    "fingerprintMD5": "89:f0:26:62:47:a3:1d:3a:bd:14:28:be:fe:86:18:d0",
    "fingerprintSHA256": "PASzCaK/qlWPyv0COry+9IN4INO7AnXdtal/hbIrUDQ",
    "guid": "0000D72EC33C33BA03CA9DAA41C0EA9B36DAF175",
    "hostKeyDevices": 0,
    "isUnmatched": false,
    "keyLength": "2048",
    "keysetType": 2,
    "keyType": {
        "mainText": "ssh-rsa",
        "subText": "2048",
        "link": null
    "lastRotationDate": null,
    "lastUsedDate": null,
    "lastUsedDateMin": null,
    "needsToBeProvisioned": false,
    "nistCodes": [],
    "privateKeysCount": 1,
    "publicKeysCount": 4,
    "risks": [],
    "rotationScheduled": false,
    "rotationError": false,
    "status": [16777216],
    "trustedDevices": 0,
    "trustId": "0000D72EC33C33BA03CA9DAA41C0EA9B36DAF175",
    "unknownPassphrase": false
    "unmatchedTrustId": null,
"""

class TextLink(ObjectModel):
    link: str = ApiField(alias='link')
    main_text: str = ApiField(alias='mainText')
    sub_text: str = ApiField(alias='subText')


class SSHKeyDetails(ObjectModel):
    access: str = ApiField(alias='access')
    accessAndName: TextLink = ApiField(alias='accessAndName')
    algorithm: str = ApiField(alias='algorithm')
    fingerprint_md5: str = ApiField(alias='fingerprintMD5')
    fingerprint_sha256: str = ApiField(alias='fingerprintSHA256')
    guid: str = ApiField(alias='guid')
    host_key_devices: int = ApiField(alias='hostKeyDevices')
    is_unmatched: bool = ApiField(alias='isUnmatched')
    key_length: str = ApiField(alias='keyLength')
    keyset_type: int = ApiField(alias='keysetType')
    key_type: TextLink = ApiField(alias='keyType')
    last_rotation_date: datetime = ApiField(alias='lastRotationDate')
    last_used_date: datetime = ApiField(alias='lastUsedDate')
    last_used_date_min: datetime = ApiField(alias='lastUsedDateMin')
    needs_to_be_provisioned: bool = ApiField(alias='needsToBeProvisioned')
    nist_codes: List[int] = ApiField(alias='nistCodes', default_factory=list)
    private_keys_count: int = ApiField(alias='privateKeysCount')
    public_keys_count: int = ApiField(alias='publicKeysCount')
    risks: List[str] = ApiField(alias='risks', default_factory=list)
    rotation_scheduled: bool = ApiField(alias='rotationScheduled')
    rotation_error: bool = ApiField(alias='rotationError')
    status: List[int] = ApiField(alias='status', default_factory=list)
    trusted_devices: int = ApiField(alias='trustedDevices')
    trust_id: str = ApiField(alias='trustId')
    unknown_passphrase: bool = ApiField(alias='unknownPassphrase')
    unmatched_trust_id: str = ApiField(alias='unmatchedTrustId')

