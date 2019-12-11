from properties.resultcodes import ResultCodes


class Metadata:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.metadata_result = ResultCodes.Metadata.get(code, 'Unknown')

    class Item:
        def __init__(self, item_dict: dict):
            if not isinstance(item_dict, dict):
                item_dict = {}

            self.allowed_characters = item_dict.get('AllowedCharacters')
            self.allowed_values = item_dict.get('AllowedValues')
            self.category = item_dict.get('Category')
            self.date_only = item_dict.get('DateOnly')
            self.default_values = item_dict.get('DefaultValues')
            self.display_after = item_dict.get('DisplayAfter')
            self.dn = item_dict.get('DN')
            self.error_message = item_dict.get('ErrorMessage')
            self.guid = item_dict.get('Guid')
            self.help = item_dict.get('Help')
            self.localization_table = item_dict.get('LocalizationTable')
            self.localized_help = item_dict.get('LocalizedHelp')
            self.localized_label = item_dict.get('LocalizedLabel')
            self.localized_set = item_dict.get('LocalizedSet')
            self.mandatory = item_dict.get('Mandatory')
            self.name = item_dict.get('Name')
            self.mask = item_dict.get('Mask')
            self.maximum_length = item_dict.get('MaximumLength')
            self.minimum_length = item_dict.get('MinimumLength')
            self.policyable = item_dict.get('Policyable')
            self.regular_expression = item_dict.get('RegularExpression')
            self.render_hidden = item_dict.get('RenderHidden')
            self.render_read_only = item_dict.get('RenderReadOnly')
            self.single = item_dict.get('Single')
            self.time_only = item_dict.get('TimeOnly')
            self.type = item_dict.get('Type')

    class Data:
        def __init__(self, data_dict: dict):
            if not isinstance(data_dict, dict):
                data_dict = {}

            self.key = Metadata.Item(data_dict.get('Key'))
            self.value = data_dict.get('Value')

    class PolicyItem:
        def __init__(self, policy_item_dict: dict):
            if not isinstance(policy_item_dict, dict):
                policy_item_dict = {}

            self.key = policy_item_dict.get('Key')
            self.value = [Metadata.Item(value) for value in policy_item_dict.get('Value')]
