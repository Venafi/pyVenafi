from properties.resultcodes import ResultCodes


class SecretStore:
    class Result:
        def __init__(self, code):
            self.code = code  # type: int
            self.secret_store_result = ResultCodes.SecretStore.get(code, 'Unknown')

    class TypedNameValues:
        def __init__(self, type_name_value_dict: dict):
            if not isinstance(type_name_value_dict, dict):
                type_name_value_dict = {}

            self.name= type_name_value_dict.get('Name')  # type: str
            self.type = type_name_value_dict.get('Type')  # type: str
            self.value = type_name_value_dict.get('Value')  # type: str
