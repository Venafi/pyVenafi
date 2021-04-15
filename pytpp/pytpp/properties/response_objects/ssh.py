from typing import List
from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string


class SSH:
    class Response:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.success = response_object.get('Success')  # type: bool
            self.error_code = response_object.get('ErrorCode')  # type: int
            self.error_message = ResultCodes.SSHErrorCodes.get(self.error_code, 'Unknown') if self.error_code else None  # type: str

    class ConnectionResult:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.device_guid = response_object.get('DeviceGuid')  # type: str
            self.error = response_object.get('Error')  # type: str
            self.success = response_object.get('Success')  # type: bool

    class DeviceData:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.dn = response_object.get('DN')  # type: str
            self.device_guid = response_object.get('DeviceGuid')  # type: str
            self.host_name = response_object.get('HostName')  # type: str
            self.is_compliant = response_object.get('IsCompliant')  # type: bool
            self.type = response_object.get('Type')  # type: str

    class KeyData:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
                
            self.active_from = from_date_string(response_object.get('ActiveFrom'))
            self.algorithm = response_object.get('Algorithm')  # type: str
            self.allowed_source_restriction = response_object.get('AllowedSourceRestriction')  # type: List[str]
            self.approver = response_object.get('Approver')  # type: List[str]
            self.denied_source_restriction = response_object.get('DeniedSourceRestriction')  # type: List[str]
            self.device_guid = response_object.get('DeviceGuid')  # type: str
            self.filepath = response_object.get('Filepath')  # type: str
            self.forced_command = response_object.get('ForcedCommand')  # type: str
            self.format = response_object.get('Format')  # type: str
            self.is_encrypted = response_object.get('IsEncrypted')  # type: bool
            self.key_id = response_object.get('KeyId')  # type: int
            self.keysetid = response_object.get('Keysetid')  # type: str
            self.last_used = from_date_string(response_object.get('Last Used'))
            self.length = response_object.get('Length')  # type: int
            self.notes = response_object.get('Notes')  # type: str
            self.options = response_object.get('Options')  # type: List[str]
            self.process_error = response_object.get('ProcessError')  # type: str
            self.process_status = response_object.get('ProcessStatus')  # type: str
            self.reason = response_object.get('Reason')  # type: str
            self.rotation_stage = response_object.get('RotationStage')  # type: int
            self.type = response_object.get('Type')  # type: str
            self.username = response_object.get('Username')  # type: str
            self.violation_status = response_object.get('ViolationStatus')  # type: List[int]
            
    class KeySetData:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
                
            self.access = response_object.get('Access')  # type: str
            self.algorithm = response_object.get('Algorithm')  # type: str
            self.fingerprint_md5 = response_object.get('FingerprintMD5')  # type: str
            self.fingerprint_sha256 = response_object.get('FingerprintSHA256')  # type: str
            self.keysetid = response_object.get('Keysetid')  # type: str
            self.last_rotation_date = from_date_string(response_object.get('LastRotationDate'))
            self.last_used = from_date_string(response_object.get('Last Used')) 
            self.length = response_object.get('Length')  # type: int
            self.private_keys = [SSH.KeyData(data) for data in response_object.get('PrivateKeys')]
            self.process_error = response_object.get('ProcessError')  # type: str
            self.process_status = response_object.get('ProcessStatus')  # type: str
            self.public_keys = [SSH.KeyData(data) for data in response_object.get('PublicKeys')]
            self.rotation_stage = response_object.get('RotationStage')  # type: int
            self.type = response_object.get('Type')  # type: str
            self.username = response_object.get('Username')  # type: str
            self.violation_status = response_object.get('ViolationStatus')  # type: list

    class KeyUsageData:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.alert = response_object.get('Alert')
            self.authorized_key_id = response_object.get('AuthorizedKeyId')
            self.client_name = response_object.get('ClientName')
            self.fingerprint = response_object.get('Fingerprint')
            self.key_usage_id = response_object.get('KeyUsageId')
            self.keyset_id = response_object.get('KeysetId')
            self.last_used = response_object.get('LastUsed')
            self.private_key_id = response_object.get('PrivateKeyId')
            self.server_account = response_object.get('ServerAccount')
            self.server_name = response_object.get('ServerName')
