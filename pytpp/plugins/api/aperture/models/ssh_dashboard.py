from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List


class PolicyViolation(ObjectModel):
    name: str = ApiField(alias='name')
    items: List[str] = ApiField(alias='items', default_factory=list)
    total_items: int = ApiField(alias='totalItems')


class Record(ObjectModel):
    record: str = ApiField(alias='record')
    record_value: int = ApiField(alias='recordValue')
    is_risk: bool = ApiField(alias='isRisk')
    is_legend: bool = ApiField(alias='isLegend')


class Trend(ObjectModel):
    date: datetime = ApiField(alias='date')
    orphans: dict = ApiField(alias='orphans')
    non_compliant_hosts: dict = ApiField(alias='nonCompliantHosts')
    non_compliant_keys: dict = ApiField(alias='nonCompliantKeys')
    agents: dict = ApiField(alias='agents')
    duplicate_private_keys: dict = ApiField(alias='duplicatePrivateKeys')
    policy_violations_summary: dict = ApiField(alias='policyViolationsSummary')
    key_lengths: dict = ApiField(alias='keyLengths')
    algorithms: dict = ApiField(alias='algorithms')
    vendor_formats: dict = ApiField(alias='vendorFormats')
