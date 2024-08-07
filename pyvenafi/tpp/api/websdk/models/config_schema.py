from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)
from pyvenafi.tpp.api.websdk.models.resultcodes import ResultCodes

# region Models
class Result(ObjectModel):
    code: int = ApiField()

    @property
    def config_result(self) -> str:
        return ResultCodes.Config.get(self.code, 'Unknown')

class AttributeDefinition(ObjectModel):
    name: str = ApiField(alias='Name')
    property: int = ApiField(alias='Property')
    syntax: str = ApiField(alias='Syntax')

class ClassDefinition(ObjectModel):
    containment_names: list[str] = ApiField(alias='ContainmentNames', default_factory=list)
    containment_sub_names: list[str] = ApiField(alias='ContainmentSubNames', default_factory=list)
    mandatory_names: list[str] = ApiField(alias='MandatoryNames', default_factory=list)
    name: str = ApiField(alias='Name')
    naming_names: list[str] = ApiField(alias='NamingNames', default_factory=list)
    optional_names: list[str] = ApiField(alias='OptionalNames', default_factory=list)
    super_class_names: list[str] = ApiField(alias='SuperClassNames', default_factory=list)
