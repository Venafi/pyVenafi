from __future__ import annotations
from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime


class Record(OutputModel):
    filter_key: str = ApiField(alias='filterKey')
    record: str = ApiField(alias='record')
    record_value: int = ApiField(alias='recordValue')
    is_risk: bool = ApiField(alias='isRisk')
    is_legend: bool = ApiField(alias='isLegend')


class Trend(OutputModel):
    date: datetime = ApiField(alias='date')
    key_length: dict = ApiField(alias='keyLength')
    signing_algorithm: dict = ApiField(alias='signingAlgorithm')
    key_algorithm: dict = ApiField(alias='keyAlgorithm')
    management_type: dict = ApiField(alias='managementType')
    issuer: dict = ApiField(alias='issuer')
    validity_period: dict = ApiField(alias='validityPeriod')
    certificate_type: dict = ApiField(alias='certificateType')
    total_certs: dict = ApiField(alias='totalCerts')
    renewal: dict = ApiField(alias='renewal')
    trust_net_cert_summary: dict = ApiField(alias='trustNetCertSummary')
    protection_status_summary: dict = ApiField(alias='protectionStatusSummary')
