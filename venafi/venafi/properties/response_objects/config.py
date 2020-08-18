from venafi.properties.resultcodes import ResultCodes


class Config:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class NameValues:
        def __init__(self, response_object: dict, api_type: str):
            if not isinstance(response_object, dict):
                response_object = {}

            if api_type.lower() == 'websdk':
                self.name = response_object.get('Name')  # type: str
                self.values = response_object.get('Values')  # type: list

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class Object:
        def __init__(self, response_object: dict, api_type: str):
            if not isinstance(response_object, dict):
                response_object = {}

            if api_type.lower() == 'websdk':
                self.absolute_guid = response_object.get('AbsoluteGUID')  # type: str
                self.dn = response_object.get('DN')  # type: str
                self.guid = response_object.get('GUID')  # type: str
                self.config_id = response_object.get('Id')  # type: int
                self.name = response_object.get('Name')  # type: str
                self.parent = response_object.get('Parent')  # type: str
                self.revision = response_object.get('Revision')  # type: int
                self.type_name = response_object.get('TypeName')  # type: str

            elif api_type.lower() == 'aperture':
                self.absolute_guid = response_object.get('parentPolicyGuid')  # type: str
                self.dn = response_object.get('dn')  # type: str
                self.guid = response_object.get('id')  # type: str
                self.config_id = None
                self.name = response_object.get('name')  # type: str
                self.parent = response_object.get('parentDn')  # type: str
                self.revision = None
                self.type_name = response_object.get('typeName')  # type: str

    class Policy:
        def __init__(self, response_object: dict, api_type: str):
            if not isinstance(response_object, dict):
                response_object = {}

            if api_type.lower() == 'websdk':
                self.attribute_name = response_object.get('AttributeName')  # type: str
                self.guid = response_object.get('GUID')  # type: str
                self.property = response_object.get('Property')  # type: str
                self.type_name = response_object.get('TypeName')  # type: str
                self.value_list = response_object.get('ValueList')  # type: list

            elif api_type.lower() == 'aperture':
                # not implemented yet
                pass

