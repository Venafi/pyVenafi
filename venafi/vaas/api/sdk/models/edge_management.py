from datetime import datetime
from uuid import UUID
from venafi.vaas.api.api_base import ApiField, ObjectModel
from typing import List, Literal

ProductEntitlements = Literal['ANY', 'MIRA', 'DEVOPS', 'OUTAGE_DETECTION']


class PairingCodeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    company_id: UUID = ApiField(alias='companyId')
    product_entitlements: List[ProductEntitlements] = ApiField(alias='productEntitlements')
    environment_id: UUID = ApiField(alias='environmentId')
    pairing_code: str = ApiField(alias='pairingCode')
    reuse_count: int = ApiField(alias='reuseCount')
    expiration_date: datetime = ApiField(alias='expirationDate')
    modification_date: datetime = ApiField(alias='modificationDate')
