from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class Certificate(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    fingerprint: str = ApiField(alias='fingerprint')

class Protocol(ObjectModel):
    certificates: list[str] = ApiField(alias='certificates')
    protocol: str = ApiField(alias='protocol')

class Endpoint(ObjectModel):
    certificates: list[Certificate] = ApiField(alias='certificates')
    host: str = ApiField(alias='host')
    ip: str = ApiField(alias='ip')
    port: int = ApiField(alias='port')
    protocols: list[Protocol] = ApiField(alias='protocols')
