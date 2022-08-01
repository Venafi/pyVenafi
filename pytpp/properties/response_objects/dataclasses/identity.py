from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Identity(PayloadModel):
    full_name: str = PayloadField(alias='FullName')
    is_container: bool = PayloadField(alias='IsContainer')
    is_group: bool = PayloadField(alias='IsGroup')
    name: str = PayloadField(alias='Name')
    prefix: str = PayloadField(alias='Prefix')
    prefixed_name: str = PayloadField(alias='PrefixedName')
    prefixed_universal: str = PayloadField(alias='PrefixedUniversal')
    type: str = PayloadField(alias='Type')
    universal: str = PayloadField(alias='Universal')


class InvalidIdentity(PayloadModel):
    prefix: str = PayloadField(alias='Prefix')
    prefixed_name: str = PayloadField(alias='PrefixedName')
    prefixed_universal: str = PayloadField(alias='PrefixedUniversal')
    universal: str = PayloadField(alias='Universal')
