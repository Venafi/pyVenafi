from venafi.properties.resultcodes import ResultCodes


class ConfigSchema:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class AttributeDefinition:
        def __init__(self, attr_dict: dict):
            if not isinstance(attr_dict, dict):
                attr_dict = {}

            self.name = attr_dict.get('Name')  # type: str
            self.syntax = attr_dict.get('Syntax')  # type: str

    class ClassDefinition:
        def __init__(self, def_dict: dict):
            if not isinstance(def_dict, dict):
                def_dict = {}

            self.containment_names = def_dict.get('ContainmentNames')  # type: list
            self.containment_sub_names = def_dict.get('ContainmentSubNames')  # type: list
            self.mandatory_names = def_dict.get('MandatoryNames')  # type: list
            self.name = def_dict.get('Name')  # type: str
            self.naming_names = def_dict.get('NamingNames')  # type: list
            self.optional_names = def_dict.get('OptionalNames')  # type: list
            self.super_class_names = def_dict.get('SuperClassNames')  # type: list
