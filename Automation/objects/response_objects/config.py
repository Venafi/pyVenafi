from enums.resultcodes import ResultCodes


class Config:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class Object:
        def __init__(self, object_dict: dict, api_type: str):
            if not isinstance(object_dict, dict):
                object_dict = {}

            if api_type.lower() == 'websdk':
                self.absolute_guid = object_dict.get('AbsoluteGUID')
                self.dn = object_dict.get('DN')
                self.guid = object_dict.get('GUID')
                self.config_id = object_dict.get('Id')
                self.name = object_dict.get('Name')
                self.parent = object_dict.get('Parent')
                self.revision = object_dict.get('Revision')
                self.type_name = object_dict.get('TypeName')

            elif api_type.lower() == 'aperture':
                self.absolute_guid = object_dict.get('parentPolicyGuid')
                self.dn = object_dict.get('dn')
                self.guid = object_dict.get('id')
                self.config_id = None
                self.name = object_dict.get('name')
                self.parent = object_dict.get('parent')
                self.revision = None
                self.type_name = object_dict.get('typeName')

    class Policy:
        def __init__(self, policy_dict: dict, api_type: str):
            if not isinstance(policy_dict, dict):
                policy_dict = {}

            if api_type.lower() == 'websdk':
                self.attribute_name = policy_dict.get('AttributeName')
                self.guid = policy_dict.get('GUID')
                self.property = policy_dict.get('Property')
                self.type_name = policy_dict.get('TypeName')
                self.value_list = policy_dict.get('ValueList')

            elif api_type.lower() == 'aperture':
                # not implemented yet
                pass

