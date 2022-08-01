from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Permissions(PayloadModel):
    delete: bool = PayloadField(alias='Delete')
    discover: bool = PayloadField(alias='Discover')
    manage: bool = PayloadField(alias='Manage')
    read: bool = PayloadField(alias='Read')
    revoke: bool = PayloadField(alias='Revoke')
