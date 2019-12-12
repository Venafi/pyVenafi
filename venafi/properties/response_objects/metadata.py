from properties.resultcodes import ResultCodes


class Metadata:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.metadata_result = ResultCodes.Metadata.get(code, 'Unknown')

    class Item:
        def __init__(self, item_dict: dict):
            if not isinstance(item_dict, dict):
                item_dict = {}

            self.allowed_characters = item_dict.get('AllowedCharacters')  # type: str
            self.allowed_values = item_dict.get('AllowedValues')  # type: str
            self.category = item_dict.get('Category')  # type: str
            self.date_only = item_dict.get('DateOnly')  # type: bool
            self.default_values = item_dict.get('DefaultValues')  # type: str
            self.display_after = item_dict.get('DisplayAfter')  # type: str
            self.dn = item_dict.get('DN')  # type: str
            self.error_message = item_dict.get('ErrorMessage')  # type: str
            self.guid = item_dict.get('Guid')  # type: str
            self.help = item_dict.get('Help')  # type: str
            self.localization_table = item_dict.get('LocalizationTable')  # type: str
            self.localized_help = item_dict.get('LocalizedHelp')  # type: str
            self.localized_label = item_dict.get('LocalizedLabel')  # type: str
            self.localized_set = item_dict.get('LocalizedSet')  # type: str
            self.mandatory = item_dict.get('Mandatory')  # type: bool
            self.name = item_dict.get('Name')  # type: str
            self.mask = item_dict.get('Mask')  # type: str
            self.maximum_length = item_dict.get('MaximumLength')  # type: int
            self.minimum_length = item_dict.get('MinimumLength')  # type: int
            self.policyable = item_dict.get('Policyable')  # type: bool
            self.regular_expression = item_dict.get('RegularExpression')  # type: str
            self.render_hidden = item_dict.get('RenderHidden')  # type: bool
            self.render_read_only = item_dict.get('RenderReadOnly')  # type: bool
            self.single = item_dict.get('Single')  # type: bool
            self.time_only = item_dict.get('TimeOnly')  # type: bool
            self.type = item_dict.get('Type')  # type: int

    class Data:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}

            self.key = Metadata.Item(data_dict.get('Key'))
            self.value = data_dict.get('Value')  # type: list

    class PolicyItem:
        def __init__(self, policy_item_dict: dict):
            if not isinstance(policy_item_dict, dict):
                policy_item_dict = {}

            self.key = policy_item_dict.get('Key')  # type: str
            self.value = [Metadata.Item(value) for value in policy_item_dict.get('Value')]
