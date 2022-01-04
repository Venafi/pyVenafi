from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass
class CertificateDetails:
    allowed_app_type: str
    aperture_status: List[str]
    approver: List[str]
    city: str
    common_name: str
    contact: List[str]
    country: str
    days_to_expire: int
    description: str
    dn: str
    dns_sans: List[str]
    domain: str
    elliptic_curve: str
    email_sans: List[str]
    error_details: str
    id: str
    installations: int
    ip_sans: List[str]
    is_disabled: bool
    is_in_error: bool
    is_rename_allowed: bool
    is_validation_enabled: bool
    issuer: str
    key_algorithm: str
    key_size: int
    last_renewed_by: List[str]
    management_type: str
    name: str
    organization: str
    organizational_unit: List[str]
    parent_dn: str
    renewal_date: datetime
    revocation_status: str
    risks: List[str]
    serial_number: str
    signature_algorithm: str
    single_click_actions: List[str]
    state: str
    status_details: Dict[str, List[str]]
    tls_endpoints: int
    trust_net_reputation_score: int
    trust_net_reviewed_by: str
    trust_net_reviewed_date: datetime
    upn_sans: List[str]
    uri_sans: List[str]
    usage: str
    use_manual_csr: bool
    valid_from: datetime
    valid_to: datetime
    validation_state: str
    validity_period_days: int
