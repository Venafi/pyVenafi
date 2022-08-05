from typing import List

from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def config_result(self) -> str:
        return ResultCodes.Config.get(self.code, 'Unknown')


class AttributeDefinition(PayloadModel):
    name: str = PayloadField(alias='Name')
    property: int = PayloadField(alias='Property')
    syntax: str = PayloadField(alias='Syntax')


class ClassDefinition(PayloadModel):
    containment_names: List[str] = PayloadField(alias='ContainmentNames')
    containment_sub_names: List[str] = PayloadField(alias='ContainmentSubNames')
    mandatory_names: List[str] = PayloadField(alias='MandatoryNames')
    name: str = PayloadField(alias='Name')
    naming_names: List[str] = PayloadField(alias='NamingNames')
    optional_names: List[str] = PayloadField(alias='OptionalNames')
    super_class_names: List[str] = PayloadField(alias='SuperClassNames')
