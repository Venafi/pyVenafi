from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Identity(PayloadModel):
    full_name: str = PayloadField(alias='FullName', default=None)
    is_container: bool = PayloadField(alias='IsContainer', default=None)
    is_group: bool = PayloadField(alias='IsGroup', default=None)
    name: str = PayloadField(alias='Name', default=None)
    prefix: str = PayloadField(alias='Prefix', default=None)
    prefixed_name: str = PayloadField(alias='PrefixedName', default=None)
    prefixed_universal: str = PayloadField(alias='PrefixedUniversal', default=None)
    type: str = PayloadField(alias='Type', default=None)
    universal: str = PayloadField(alias='Universal', default=None)


class InvalidIdentity(PayloadModel):
    prefix: str = PayloadField(alias='Prefix', default=None)
    prefixed_name: str = PayloadField(alias='PrefixedName', default=None)
    prefixed_universal: str = PayloadField(alias='PrefixedUniversal', default=None)
    universal: str = PayloadField(alias='Universal', default=None)
