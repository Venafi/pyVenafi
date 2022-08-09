from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import Optional


class Object(PayloadModel):
    absolute_guid: str = PayloadField(alias='parentPolicyGuid')
    dn: str = PayloadField(alias='dn')
    guid: str = PayloadField(alias='id')
    config_id: Optional[int] = PayloadField()
    name: str = PayloadField(alias='name')
    parent: str = PayloadField(alias='parentDn')
    revision: Optional[int] = PayloadField()
    type_name: str = PayloadField(alias='typeNam')
