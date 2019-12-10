from properties.resultcodes import ResultCodes


class Credential:
    class Result:
        def __init__(self, code):
            self.code = code
            self.credential_result = ResultCodes.Credential.get(code, 'Unknown')

    class CredentialInfo:
        def __init__(self, cred_info_dict: dict):
            if not isinstance(cred_info_dict, dict):
                cred_info_dict = {}

            self.class_name = cred_info_dict.get('ClassName')
            self.full_name = cred_info_dict.get('FullName')

    class NameTypeValue:
        def __init__(self, ntv_dict):
            self.name = ntv_dict.get('Name')
            self.type = ntv_dict.get('Type')
            self.value = ntv_dict.get('Value')
