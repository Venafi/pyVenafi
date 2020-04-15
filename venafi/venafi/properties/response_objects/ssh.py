from typing import List
from venafi.properties.resultcodes import ResultCodes
from venafi.tools.helpers.date_converter import from_date_string


class SSH:
    class Response:
        def __init__(self, resp_obj: dict):
            if not isinstance(resp_obj, dict):
                resp_obj = {}

            self.success = resp_obj.get('Success')  # type: bool
            self.error_code = resp_obj.get('ErrorCode')  # type: int
            self.error_message = ResultCodes.SSHErrorCodes.get(self.error_code, 'Unknown') if self.error_code else None  # type: str

    class ConnectionResult:
        def __init__(self, connection_result_dict: dict):
            if not isinstance(connection_result_dict, dict):
                connection_result_dict = {}

            self.device_guid = connection_result_dict.get('DeviceGuid')  # type: str
            self.error = connection_result_dict.get('Error')  # type: str
            self.success = connection_result_dict.get('Success')  # type: bool

    class DeviceData:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}

            self.dn = data_dict.get('DN')  # type: str
            self.device_guid = data_dict.get('DeviceGuid')  # type: str
            self.host_name = data_dict.get('HostName')  # type: str
            self.is_compliant = data_dict.get('IsCompliant')  # type: bool
            self.type = data_dict.get('Type')  # type: str

    class KeyData:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}
                
            self.active_from = from_date_string(data_dict.get('ActiveFrom'))
            self.algorithm = data_dict.get('Algorithm')  # type: str
            self.allowed_source_restriction = data_dict.get('AllowedSourceRestriction')  # type: List[str]
            self.approver = data_dict.get('Approver')  # type: List[str]
            self.denied_source_restriction = data_dict.get('DeniedSourceRestriction')  # type: List[str]
            self.device_guid = data_dict.get('DeviceGuid')  # type: str
            self.filepath = data_dict.get('Filepath')  # type: str
            self.forced_command = data_dict.get('ForcedCommand')  # type: str
            self.format = data_dict.get('Format')  # type: str
            self.is_encrypted = data_dict.get('IsEncrypted')  # type: bool
            self.key_id = data_dict.get('KeyId')  # type: int
            self.keysetid = data_dict.get('Keysetid')  # type: str
            self.last_used = from_date_string(data_dict.get('Last Used'))
            self.length = data_dict.get('Length')  # type: int
            self.notes = data_dict.get('Notes')  # type: str
            self.options = data_dict.get('Options')  # type: List[str]
            self.process_error = data_dict.get('ProcessError')  # type: str
            self.process_status = data_dict.get('ProcessStatus')  # type: str
            self.reason = data_dict.get('Reason')  # type: str
            self.rotation_stage = data_dict.get('RotationStage')  # type: int
            self.type = data_dict.get('Type')  # type: str
            self.username = data_dict.get('Username')  # type: str
            self.violation_status = data_dict.get('ViolationStatus')  # type: List[int]
            
    class KeySetData:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}
                
            self.access = data_dict.get('Access')  # type: str
            self.algorithm = data_dict.get('Algorithm')  # type: str
            self.fingerprint_md5 = data_dict.get('FingerprintMD5')  # type: str
            self.fingerprint_sha256 = data_dict.get('FingerprintSHA256')  # type: str
            self.keysetid = data_dict.get('Keysetid')  # type: str
            self.last_rotation_date = from_date_string(data_dict.get('LastRotationDate'))
            self.last_used = from_date_string(data_dict.get('Last Used')) 
            self.length = data_dict.get('Length')  # type: int
            self.private_keys = [SSH.KeyData(data) for data in data_dict.get('PrivateKeys')]
            self.process_error = data_dict.get('ProcessError')  # type: str
            self.process_status = data_dict.get('ProcessStatus')  # type: str
            self.public_keys = [SSH.KeyData(data) for data in data_dict.get('PublicKeys')]
            self.rotation_stage = data_dict.get('RotationStage')  # type: int
            self.type = data_dict.get('Type')  # type: str
            self.username = data_dict.get('Username')  # type: str
            self.violation_status = data_dict.get('ViolationStatus')  # type: list

    class KeyUsageData:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}

            self.alert = data_dict.get('Alert')
            self.authorized_key_id = data_dict.get('AuthorizedKeyId')
            self.client_name = data_dict.get('ClientName')
            self.fingerprint = data_dict.get('Fingerprint')
            self.key_usage_id = data_dict.get('KeyUsageId')
            self.keyset_id = data_dict.get('KeysetId')
            self.last_used = data_dict.get('LastUsed')
            self.private_key_id = data_dict.get('PrivateKeyId')
            self.server_account = data_dict.get('ServerAccount')
            self.server_name = data_dict.get('ServerName')
