from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class PolicyViolation:
    name: str
    items: List[str]
    total_items: int


@dataclass
class Record:
    record: str
    record_value: int
    is_risk: bool
    is_legend: bool


@dataclass
class Trend:
    date: datetime
    orphans: dict
    non_compliant_hosts: dict
    non_compliant_keys: dict
    agents: dict
    duplicate_private_keys: dict
    policy_violations_summary: dict
    key_lengths: dict
    algorithms: dict
    vendor_formats: dict

