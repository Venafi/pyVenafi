from pytpp.properties.resultcodes import ResultCodes


class Config:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class NameValues:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.name = response_object.get('Name')  # type: str
            self.values = response_object.get('Values')  # type: list


    class Object:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.absolute_guid = response_object.get('AbsoluteGUID')  # type: str
            self.dn = response_object.get('DN')  # type: str
            self.guid = response_object.get('GUID')  # type: str
            self.config_id = response_object.get('Id')  # type: int
            self.name = response_object.get('Name')  # type: str
            self.parent = response_object.get('Parent')  # type: str
            self.revision = response_object.get('Revision')  # type: int
            self.type_name = response_object.get('TypeName')  # type: str

    class Policy:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.attribute_name = response_object.get('AttributeName')  # type: str
            self.guid = response_object.get('GUID')  # type: str
            self.property = response_object.get('Property')  # type: str
            self.type_name = response_object.get('TypeName')  # type: str
            self.value_list = response_object.get('ValueList')  # type: list
