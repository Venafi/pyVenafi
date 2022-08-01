from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Rights(PayloadModel):
    checksum: str = PayloadField(alias='Checksum')
    is_container: bool = PayloadField(alias='IsContainer')
    is_group: bool = PayloadField(alias='IsGroup')
    object: str = PayloadField(alias='Object')
    principal: str = PayloadField(alias='Principal')
    rights: str = PayloadField(alias='Rights')
    sub_system: str = PayloadField(alias='SubSystem')
