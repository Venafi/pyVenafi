from pytpp.api.api_base import OutputModel, ApiField
from typing import Literal

ProductType = Literal[
    'CodeSign Protect',
    'Client Protect',
    'Platform',
    'SSH Protect',
    'TLS Protect',
]


class Preference(OutputModel):
    id: int = ApiField(alias='Id')
    universal: str = ApiField(alias='Universal')
    product: str = ApiField(alias='Product')
    category: str = ApiField(alias='Category')
    name: str = ApiField(alias='Name')
    value: str = ApiField(alias='Value')
    locked: bool = ApiField(alias='Locked')
