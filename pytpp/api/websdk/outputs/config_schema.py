from typing import List

from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField


class Result(OutputModel):
    code: int = ApiField()

    @property
    def config_result(self) -> str:
        return ResultCodes.Config.get(self.code, 'Unknown')


class AttributeDefinition(OutputModel):
    name: str = ApiField(alias='Name')
    property: int = ApiField(alias='Property')
    syntax: str = ApiField(alias='Syntax')


class ClassDefinition(OutputModel):
    containment_names: List[str] = ApiField(alias='ContainmentNames')
    containment_sub_names: List[str] = ApiField(alias='ContainmentSubNames')
    mandatory_names: List[str] = ApiField(alias='MandatoryNames')
    name: str = ApiField(alias='Name')
    naming_names: List[str] = ApiField(alias='NamingNames')
    optional_names: List[str] = ApiField(alias='OptionalNames')
    super_class_names: List[str] = ApiField(alias='SuperClassNames')
