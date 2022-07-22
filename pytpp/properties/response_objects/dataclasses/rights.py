from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Rights(PayloadModel):
    checksum: str = PayloadField(alias='Checksum', default=None)
    is_container: bool = PayloadField(alias='IsContainer', default=None)
    is_group: bool = PayloadField(alias='IsGroup', default=None)
    object: str = PayloadField(alias='Object', default=None)
    principal: str = PayloadField(alias='Principal', default=None)
    rights: str = PayloadField(alias='Rights', default=None)
    sub_system: str = PayloadField(alias='SubSystem', default=None)
