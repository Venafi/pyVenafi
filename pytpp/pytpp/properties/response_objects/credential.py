from pytpp.properties.resultcodes import ResultCodes


class Credential:
    class Result:
        def __init__(self, code):
            self.code = code  # type: int
            self.credential_result = ResultCodes.Credential.get(code, 'Unknown')

    class CredentialInfo:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.class_name = response_object.get('ClassName')  # type: str
            self.full_name = response_object.get('FullName')  # type: str

    class NameTypeValue:
        def __init__(self, response_object):
            self.name = response_object.get('Name')  # type: str
            self.type = response_object.get('Type')  # type: str
            self.value = response_object.get('Value')  # type: str
