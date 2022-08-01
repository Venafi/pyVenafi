from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from properties.resultcodes import ResultCodes
from typing import Optional


class Result(PayloadModel):
    code: int = PayloadField(default=None)

    @property
    def config_result(self):
        return ResultCodes.Config.get(self.code, 'Unknown')


class NameValues(PayloadModel):
    name: str = PayloadField(alias='Name')
    values: list = PayloadField(alias='Values')


class Object(PayloadModel):
    absolute_guid: str = PayloadField(alias='AbsoluteGUID')
    dn: str = PayloadField(alias='DN')
    guid: str = PayloadField(alias='GUID')
    config_id: Optional[int] = PayloadField(alias='Id')
    name: str = PayloadField(alias='Name')
    parent: str = PayloadField(alias='Parent')
    revision: Optional[int] = PayloadField(alias='Revision')
    type_name: str = PayloadField(alias='TypeName')


class Policy(PayloadModel):
    attribute_name: str = PayloadField(alias='AttributeName')
    guid: str = PayloadField(alias='GUID')
    property: str = PayloadField(alias='Property')
    type_name: str = PayloadField(alias='TypeName')
    value_list: list = PayloadField(alias='ValueList')
