from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Preference(PayloadModel):
    id: int = PayloadField(alias='Id', default=None)
    universal: str = PayloadField(alias='Universal', default=None)
    product: str = PayloadField(alias='Product', default=None)
    category: str = PayloadField(alias='Category', default=None)
    name: str = PayloadField(alias='Name', default=None)
    value: str = PayloadField(alias='Value', default=None)
    locked: bool = PayloadField(alias='Locked', default=None)
