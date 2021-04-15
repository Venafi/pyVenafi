from pytpp.properties.resultcodes import ResultCodes


class Metadata:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.metadata_result = ResultCodes.Metadata.get(code, 'Unknown')

    class Item:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allowed_characters = response_object.get('AllowedCharacters')  # type: str
            self.allowed_values = response_object.get('AllowedValues')  # type: str
            self.category = response_object.get('Category')  # type: str
            self.classes = response_object.get('Classes')  # type: list
            self.configAttribute = response_object.get('ConfigAttribute')  # type: str
            self.date_only = response_object.get('DateOnly')  # type: bool
            self.default_values = response_object.get('DefaultValues')  # type: str
            self.display_after = response_object.get('DisplayAfter')  # type: str
            self.dn = response_object.get('DN')  # type: str
            self.error_message = response_object.get('ErrorMessage')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.help = response_object.get('Help')  # type: str
            self.label = response_object.get('Label')  # type: str
            self.localization_table = response_object.get('LocalizationTable')  # type: str
            self.localized_help = response_object.get('LocalizedHelp')  # type: str
            self.localized_label = response_object.get('LocalizedLabel')  # type: str
            self.localized_set = response_object.get('LocalizedSet')  # type: str
            self.mandatory = response_object.get('Mandatory')  # type: bool
            self.name = response_object.get('Name')  # type: str
            self.mask = response_object.get('Mask')  # type: str
            self.maximum_length = response_object.get('MaximumLength')  # type: int
            self.minimum_length = response_object.get('MinimumLength')  # type: int
            self.policyable = response_object.get('Policyable')  # type: bool
            self.regular_expression = response_object.get('RegularExpression')  # type: str
            self.render_hidden = response_object.get('RenderHidden')  # type: bool
            self.render_read_only = response_object.get('RenderReadOnly')  # type: bool
            self.single = response_object.get('Single')  # type: bool
            self.time_only = response_object.get('TimeOnly')  # type: bool
            self.type = response_object.get('Type')  # type: int

    class Data:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key = Metadata.Item(response_object.get('Key'))
            self.value = response_object.get('Value')  # type: list

    class PolicyItem:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key = response_object.get('Key')  # type: str
            self.value = [Metadata.Item(value) for value in response_object.get('Value')]
