from dataclasses import dataclass
from datetime import datetime


@dataclass
class Record:
    filter_key: str
    record: str
    record_value: int
    is_risk: bool
    is_legend: bool


@dataclass
class Trend:
    date: datetime
    key_length: dict
    signing_algorithm: dict
    key_algorithm: dict
    management_type: dict
    issuer: dict
    validity_period: dict
    certificate_type: dict
    total_certs: dict
    renewal: dict
    trust_net_cert_summary: dict
    protection_status_summary: dict
