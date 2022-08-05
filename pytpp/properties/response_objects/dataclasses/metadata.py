from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import List


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def metadata_result(self) -> str:
        return ResultCodes.Metadata.get(self.code, 'Unknown')


class Item(PayloadModel):
    allowed_characters: str = PayloadField(alias='AllowedCharacters')
    allowed_values: str = PayloadField(alias='AllowedValues')
    category: str = PayloadField(alias='Category')
    classes: list = PayloadField(alias='Classes')
    config_attribute: str = PayloadField(alias='ConfigAttribute')
    date_only: bool = PayloadField(alias='DateOnly')
    default_values: str = PayloadField(alias='DefaultValues')
    display_after: str = PayloadField(alias='DisplayAfter')
    dn: str = PayloadField(alias='Dn')
    error_message: str = PayloadField(alias='ErrorMessage')
    guid: str = PayloadField(alias='Guid')
    help: str = PayloadField(alias='Help')
    label: str = PayloadField(alias='Label')
    localization_table: str = PayloadField(alias='LocalizationTable')
    localized_help: str = PayloadField(alias='LocalizedHelp')
    localized_label: str = PayloadField(alias='LocalizedLabel')
    localized_set: str = PayloadField(alias='LocalizedSet')
    mandatory: bool = PayloadField(alias='Mandatory')
    name: str = PayloadField(alias='Name')
    mask: str = PayloadField(alias='Mask')
    maximum_length: int = PayloadField(alias='MaximumLength')
    minimum_length: int = PayloadField(alias='MinimumLength')
    policyable: bool = PayloadField(alias='Policyable')
    regular_expression: str = PayloadField(alias='RegularExpression')
    render_hidden: bool = PayloadField(alias='RenderHidden')
    render_read_only: bool = PayloadField(alias='RenderReadOnly')
    single: bool = PayloadField(alias='Single')
    time_only: bool = PayloadField(alias='TimeOnly')
    type: int = PayloadField(alias='Type')


class Data(PayloadModel):
    key: Item = PayloadField(alias='Key')
    value: List[str] = PayloadField(alias='Value')


class PolicyItem(PayloadModel):
    key: str = PayloadField(alias='Key')
    value: List[Item] = PayloadField(alias='Value')
