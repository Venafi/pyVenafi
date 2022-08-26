from __future__ import annotations
from pytpp.api.api_base import ApiField, ObjectModel
from typing import Optional


class Object(ObjectModel):
    absolute_guid: str = ApiField(alias='parentPolicyGuid')
    dn: str = ApiField(alias='dn')
    guid: str = ApiField(alias='id')
    config_id: Optional[int] = ApiField()
    name: str = ApiField(alias='name')
    parent: str = ApiField(alias='parentDn')
    revision: Optional[int] = ApiField()
    type_name: str = ApiField(alias='typeName')
