from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Permissions(PayloadModel):
    delete: bool = PayloadField(alias='Delete', default=None)
    discover: bool = PayloadField(alias='Discover', default=None)
    manage: bool = PayloadField(alias='Manage', default=None)
    read: bool = PayloadField(alias='Read', default=None)
    revoke: bool = PayloadField(alias='Revoke', default=None)
