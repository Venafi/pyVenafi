from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import List


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    metadata_result: str = PayloadField(alias='MetadataResult', default=None)


class Item(PayloadModel):
    allowed_characters: str = PayloadField(alias='AllowedCharacters', default=None)
    allowed_values: str = PayloadField(alias='AllowedValues', default=None)
    category: str = PayloadField(alias='Category', default=None)
    classes: list = PayloadField(alias='Classes', default=None)
    config_attribute: str = PayloadField(alias='ConfigAttribute', default=None)
    date_only: bool = PayloadField(alias='DateOnly', default=None)
    default_values: str = PayloadField(alias='DefaultValues', default=None)
    display_after: str = PayloadField(alias='DisplayAfter', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    error_message: str = PayloadField(alias='ErrorMessage', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    help: str = PayloadField(alias='Help', default=None)
    label: str = PayloadField(alias='Label', default=None)
    localization_table: str = PayloadField(alias='LocalizationTable', default=None)
    localized_help: str = PayloadField(alias='LocalizedHelp', default=None)
    localized_label: str = PayloadField(alias='LocalizedLabel', default=None)
    localized_set: str = PayloadField(alias='LocalizedSet', default=None)
    mandatory: bool = PayloadField(alias='Mandatory', default=None)
    name: str = PayloadField(alias='Name', default=None)
    mask: str = PayloadField(alias='Mask', default=None)
    maximum_length: int = PayloadField(alias='MaximumLength', default=None)
    minimum_length: int = PayloadField(alias='MinimumLength', default=None)
    policyable: bool = PayloadField(alias='Policyable', default=None)
    regular_expression: str = PayloadField(alias='RegularExpression', default=None)
    render_hidden: bool = PayloadField(alias='RenderHidden', default=None)
    render_read_only: bool = PayloadField(alias='RenderReadOnly', default=None)
    single: bool = PayloadField(alias='Single', default=None)
    time_only: bool = PayloadField(alias='TimeOnly', default=None)
    type: int = PayloadField(alias='Type', default=None)


class Data(PayloadModel):
    key: 'Item' = PayloadField(alias='Key', default=None)
    value: list = PayloadField(alias='Value', default=None)


class PolicyItem(PayloadModel):
    key: str = PayloadField(alias='Key', default=None)
    value: 'List[Item]' = PayloadField(alias='Value', default=None)
