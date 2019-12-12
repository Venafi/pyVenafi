from properties.resultcodes import ResultCodes


class Config:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class NameValues:
        def __init__(self, name_values_dict: dict, api_type: str):
            if not isinstance(name_values_dict, dict):
                name_values_dict = {}

            if api_type.lower() == 'websdk':
                self.name = name_values_dict.get('Name')  # type: str
                self.values = name_values_dict.get('Values')  # type: list

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass


    class Object:
        def __init__(self, object_dict: dict, api_type: str):
            if not isinstance(object_dict, dict):
                object_dict = {}

            if api_type.lower() == 'websdk':
                self.absolute_guid = object_dict.get('AbsoluteGUID')  # type: str
                self.dn = object_dict.get('DN')  # type: str
                self.guid = object_dict.get('GUID')  # type: str
                self.config_id = object_dict.get('Id')  # type: int
                self.name = object_dict.get('Name')  # type: str
                self.parent = object_dict.get('Parent')  # type: str
                self.revision = object_dict.get('Revision')  # type: int
                self.type_name = object_dict.get('TypeName')  # type: str

            elif api_type.lower() == 'aperture':
                self.absolute_guid = object_dict.get('parentPolicyGuid')  # type: str
                self.dn = object_dict.get('dn')  # type: str
                self.guid = object_dict.get('id')  # type: str
                self.config_id = None
                self.name = object_dict.get('name')  # type: str
                self.parent = object_dict.get('parent')  # type: str
                self.revision = None
                self.type_name = object_dict.get('typeName')  # type: str

    class Policy:
        def __init__(self, policy_dict: dict, api_type: str):
            if not isinstance(policy_dict, dict):
                policy_dict = {}

            if api_type.lower() == 'websdk':
                self.attribute_name = policy_dict.get('AttributeName')  # type: str
                self.guid = policy_dict.get('GUID')  # type: str
                self.property = policy_dict.get('Property')  # type: str
                self.type_name = policy_dict.get('TypeName')  # type: str
                self.value_list = policy_dict.get('ValueList')  # type: list

            elif api_type.lower() == 'aperture':
                # not implemented yet
                pass

