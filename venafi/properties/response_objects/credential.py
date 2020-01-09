from venafi.properties.resultcodes import ResultCodes


class Credential:
    class Result:
        def __init__(self, code):
            self.code = code  # type: int
            self.credential_result = ResultCodes.Credential.get(code, 'Unknown')

    class CredentialInfo:
        def __init__(self, cred_info_dict: dict):
            if not isinstance(cred_info_dict, dict):
                cred_info_dict = {}

            self.class_name = cred_info_dict.get('ClassName')  # type: str
            self.full_name = cred_info_dict.get('FullName')  # type: str

    class NameTypeValue:
        def __init__(self, ntv_dict):
            self.name = ntv_dict.get('Name')  # type: str
            self.type = ntv_dict.get('Type')  # type: str
            self.value = ntv_dict.get('Value')  # type: str
