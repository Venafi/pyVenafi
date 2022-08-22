from __future__ import annotations
from pytpp.api.api_base import ApiField, OutputModel


class Identity(OutputModel):
    full_name: str = ApiField(alias='fullName')
    is_container: bool = ApiField(alias='isContainer')
    is_group: bool = ApiField(alias='isGroup')
    name: str = ApiField(alias='name')
    prefix: str = ApiField(alias='prefix')
    prefixed_name: str = ApiField(alias='prefixedName')
    prefixed_universal: str = ApiField(alias='id')
    type: int = ApiField(default=0, alias='type')
    universal: str = ApiField(alias='universal')

    @property
    def is_user(self):
        return self.type & 1 == 1

    @property
    def is_security_group(self):
        return self.type & 2 == 2

    @property
    def is_distribution_group(self):
        return self.type & 8 == 8
