from pytpp.properties.resultcodes import ResultCodes


class ConfigSchema:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.config_result = ResultCodes.Config.get(code, 'Unknown')

    class AttributeDefinition:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.name = response_object.get('Name')  # type: str
            self.syntax = response_object.get('Syntax')  # type: str

    class ClassDefinition:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.containment_names = response_object.get('ContainmentNames')  # type: list
            self.containment_sub_names = response_object.get('ContainmentSubNames')  # type: list
            self.mandatory_names = response_object.get('MandatoryNames')  # type: list
            self.name = response_object.get('Name')  # type: str
            self.naming_names = response_object.get('NamingNames')  # type: list
            self.optional_names = response_object.get('OptionalNames')  # type: list
            self.super_class_names = response_object.get('SuperClassNames')  # type: list
