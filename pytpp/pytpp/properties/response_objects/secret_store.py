from pytpp.properties.resultcodes import ResultCodes


class SecretStore:
    class Result:
        def __init__(self, code):
            self.code = code  # type: int
            self.secret_store_result = ResultCodes.SecretStore.get(code, 'Unknown')

    class TypedNameValues:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.name= response_object.get('Name')  # type: str
            self.type = response_object.get('Type')  # type: str
            self.value = response_object.get('Value')  # type: str
