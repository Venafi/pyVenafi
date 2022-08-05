from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from typing import Literal

ProductType = Literal[
    'CodeSign Protect',
    'Client Protect',
    'Platform',
    'SSH Protect',
    'TLS Protect',
]


class Preference(PayloadModel):
    id: int = PayloadField(alias='Id')
    universal: str = PayloadField(alias='Universal')
    product: str = PayloadField(alias='Product')
    category: str = PayloadField(alias='Category')
    name: str = PayloadField(alias='Name')
    value: str = PayloadField(alias='Value')
    locked: bool = PayloadField(alias='Locked')
