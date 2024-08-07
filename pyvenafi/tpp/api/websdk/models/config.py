from __future__ import annotations

from typing import (
    Generic,
    Optional,
    TypeVar,
)

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)
from pyvenafi.tpp.api.websdk.models.resultcodes import ResultCodes

T = TypeVar('T')

# region Models
# region Outputs
class Result(ObjectModel):
    code: int = ApiField()

    @property
    def config_result(self):
        return ResultCodes.Config.get(self.code, 'Unknown')

class NameValues(ObjectModel, Generic[T]):
    name: str = ApiField(alias='Name')
    values: list[T] = ApiField(alias='Values', default_factory=list)

class Object(ObjectModel):
    absolute_guid: str = ApiField(alias='AbsoluteGUID')
    config_id: Optional[int] = ApiField(alias='Id')
    disabled: bool = ApiField(alias='Disabled')
    dn: str = ApiField(alias='DN')
    guid: str = ApiField(alias='GUID')
    id: int = ApiField(alias='Id')
    in_error: bool = ApiField(alias='InError')
    name: str = ApiField(alias='Name')
    parent: str = ApiField(alias='Parent')
    properties: int = ApiField(alias='Properties')
    revision: Optional[int] = ApiField(alias='Revision')
    type_name: str = ApiField(alias='TypeName')

    def __str__(self):
        return self.dn

class Policy(ObjectModel):
    attribute_name: str = ApiField(alias='AttributeName')
    guid: str = ApiField(alias='GUID')
    property: str = ApiField(alias='Property')
    type_name: str = ApiField(alias='TypeName')
    value_list: list[str] = ApiField(alias='ValueList', default_factory=list)

class ClassDefinition(ObjectModel):
    property: int = ApiField(alias='Property')
    name: str = ApiField(alias='Name')
    super_class_names: list[str] = ApiField(alias='SuperClassNames')
    containment_names: list[str] = ApiField(alias="ContainmentNames")
    containment_sub_names: list[str] = ApiField(alias="ContainmentSubNames")
    naming_names: list[str] = ApiField(alias="NamingNames")
    mandatory_names: list[str] = ApiField(alias="MandatoryNames")
    optional_names: list[str] = ApiField(alias="OptionalNames")
    optional_names_ex: list[str] = ApiField(alias="OptionalNamesEx")
    mandatories_names_ex: list[str] = ApiField(alias="MandatoriesNamesEx")

class AttributeDefinition(ObjectModel):
    syntax: int = ApiField(alias='Syntax')
    property: int = ApiField(alias='Property')
    name: str = ApiField(alias='Name')

# endregion Outputs


# region Inputs
class NameAttribute(ObjectModel, Generic[T]):
    name: str = ApiField(alias='Name')
    value: T = ApiField(alias='Value')
# endregion Inputs
# endregion Models
