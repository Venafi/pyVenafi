from pytpp.api.api_base import OutputModel, ApiField
from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


class Result(OutputModel):
    code: int = ApiField()

    @property
    def config_result(self):
        return ResultCodes.Config.get(self.code, 'Unknown')


class NameValues(OutputModel, Generic[T]):
    name: str = ApiField(alias='Name')
    values: List[T] = ApiField(alias='Values')


class Object(OutputModel):
    absolute_guid: str = ApiField(alias='AbsoluteGUID')
    dn: str = ApiField(alias='DN')
    guid: str = ApiField(alias='GUID')
    config_id: Optional[int] = ApiField(alias='Id')
    name: str = ApiField(alias='Name')
    parent: str = ApiField(alias='Parent')
    revision: Optional[int] = ApiField(alias='Revision')
    type_name: str = ApiField(alias='TypeName')


class Policy(OutputModel):
    attribute_name: str = ApiField(alias='AttributeName')
    guid: str = ApiField(alias='GUID')
    property: str = ApiField(alias='Property')
    type_name: str = ApiField(alias='TypeName')
    value_list: List[str] = ApiField(alias='ValueList')
