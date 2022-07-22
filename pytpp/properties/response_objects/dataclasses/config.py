from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from properties.resultcodes import ResultCodes
from typing import Optional


class Result(PayloadModel):
    code: int = PayloadField(default=None)

    @property
    def config_result(self):
        return ResultCodes.Config.get(self.code, 'Unknown')


class NameValues(PayloadModel):
    name: str = PayloadField(alias='Name', default=None)
    values: list = PayloadField(alias='Values', default=None)


class Object(PayloadModel):
    absolute_guid: str = PayloadField(alias='AbsoluteGUID', default=None)
    dn: str = PayloadField(alias='DN', default=None)
    guid: str = PayloadField(alias='GUID', default=None)
    config_id: Optional[int] = PayloadField(alias='Id', default=None)
    name: str = PayloadField(alias='Name', default=None)
    parent: str = PayloadField(alias='Parent', default=None)
    revision: Optional[int] = PayloadField(alias='Revision', default=None)
    type_name: str = PayloadField(alias='TypeName', default=None)


class Policy(PayloadModel):
    attribute_name: str = PayloadField(alias='AttributeName', default=None)
    guid: str = PayloadField(alias='GUID', default=None)
    property: str = PayloadField(alias='Property', default=None)
    type_name: str = PayloadField(alias='TypeName', default=None)
    value_list: list = PayloadField(alias='ValueList', default=None)
