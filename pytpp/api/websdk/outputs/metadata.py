from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField
from typing import List


class Result(OutputModel):
    code: int = ApiField()

    @property
    def metadata_result(self) -> str:
        return ResultCodes.Metadata.get(self.code, 'Unknown')


class Item(OutputModel):
    allowed_characters: str = ApiField(alias='AllowedCharacters')
    allowed_values: str = ApiField(alias='AllowedValues')
    category: str = ApiField(alias='Category')
    classes: list = ApiField(alias='Classes')
    config_attribute: str = ApiField(alias='ConfigAttribute')
    date_only: bool = ApiField(alias='DateOnly')
    default_values: str = ApiField(alias='DefaultValues')
    display_after: str = ApiField(alias='DisplayAfter')
    dn: str = ApiField(alias='Dn')
    error_message: str = ApiField(alias='ErrorMessage')
    guid: str = ApiField(alias='Guid')
    help: str = ApiField(alias='Help')
    label: str = ApiField(alias='Label')
    localization_table: str = ApiField(alias='LocalizationTable')
    localized_help: str = ApiField(alias='LocalizedHelp')
    localized_label: str = ApiField(alias='LocalizedLabel')
    localized_set: str = ApiField(alias='LocalizedSet')
    mandatory: bool = ApiField(alias='Mandatory')
    name: str = ApiField(alias='Name')
    mask: str = ApiField(alias='Mask')
    maximum_length: int = ApiField(alias='MaximumLength')
    minimum_length: int = ApiField(alias='MinimumLength')
    policyable: bool = ApiField(alias='Policyable')
    regular_expression: str = ApiField(alias='RegularExpression')
    render_hidden: bool = ApiField(alias='RenderHidden')
    render_read_only: bool = ApiField(alias='RenderReadOnly')
    single: bool = ApiField(alias='Single')
    time_only: bool = ApiField(alias='TimeOnly')
    type: int = ApiField(alias='Type')


class Data(OutputModel):
    key: Item = ApiField(alias='Key')
    value: List[str] = ApiField(alias='Value')


class PolicyItem(OutputModel):
    key: str = ApiField(alias='Key')
    value: List[Item] = ApiField(alias='Value')
