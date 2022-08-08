from properties.response_objects.dataclasses._base import PayloadField, PayloadModel

class Identity(PayloadModel):
    full_name: str = PayloadField(alias='fullName')
    is_container: bool = PayloadField(alias='isContainer')
    is_group: bool = PayloadField(alias='isGroup')
    name: str = PayloadField(alias='name')
    prefix: str = PayloadField(alias='prefix')
    prefixed_name: str = PayloadField(alias='prefixedName')
    prefixed_universal: str = PayloadField(alias='id')
    type: int = PayloadField(default=0, alias='type')
    universal: str = PayloadField(alias='universal')

    @property
    def is_user(self):
        return self.type & 1 == 1

    @property
    def is_security_group(self):
        return self.type & 2 == 2

    @property
    def is_distribution_group(self):
        return self.type & 8 == 8
