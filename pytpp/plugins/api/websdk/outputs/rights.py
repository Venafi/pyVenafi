from pytpp.api.api_base import ApiField, OutputModel


class Rights(OutputModel):
    checksum: str = ApiField(alias='Checksum')
    is_container: bool = ApiField(alias='IsContainer')
    is_group: bool = ApiField(alias='IsGroup')
    object: str = ApiField(alias='Object')
    principal: str = ApiField(alias='Principal')
    rights: str = ApiField(alias='Rights')
    sub_system: str = ApiField(alias='SubSystem')
