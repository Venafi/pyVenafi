from properties.resultcodes import ResultCodes


class ConfigSchema:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class AttributeDefinition:
        def __init__(self, attr_dict: dict):
            if not isinstance(attr_dict, dict):
                attr_dict = {}

            self.name = attr_dict.get('Name')
            self.syntax = attr_dict.get('Syntax')

    class ClassDefinition:
        def __init__(self, def_dict: dict):
            if not isinstance(def_dict, dict):
                def_dict = {}

            self.containment_names = def_dict.get('ContainmentNames')
            self.containment_sub_names = def_dict.get('ContainmentSubNames')
            self.mandatory_names = def_dict.get('MandatoryNames')
            self.name = def_dict.get('Name')
            self.naming_names = def_dict.get('NamingNames')
            self.optional_names = def_dict.get('OptionalNames')
            self.super_class_names = def_dict.get('SuperClassNames')
