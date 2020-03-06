from venafi.tools.helpers.date_converter import from_date_string


class CertificateDashboard:
    class Record:
        def __init__(self, record: dict):
            if not isinstance(record, dict):
                record = {}
            self.filter_key = record.get("filterKey")  # type: str
            self.record = record.get("record")  # type: str
            self.record_value = record.get("recordValue")  # type: int
            self.is_risk = record.get("isRisk")  # type: bool
            self.is_legend = record.get("isLegend")  # type: bool

    class Trend:
        def __init__(self, trend: dict):
            if not isinstance(trend, dict):
                trend = {}
            self.date = from_date_string(trend.get("date"))
            self.key_length = trend.get("KeyLength")  # type: dict
            self.signing_algorithm = trend.get("SigningAlgorithm")  # type: dict
            self.key_algorithm = trend.get("KeyAlgorithm")  # type: dict
            self.management_type = trend.get("ManagementType")  # type: dict
            self.issuer = trend.get("Issuer")  # type: dict
            self.validity_period = trend.get("ValidityPeriod")  # type: dict
            self.certificate_type = trend.get("CertificateType")  # type: dict
            self.total_certs = trend.get("TotalCerts")  # type: dict
            self.renewal = trend.get("Renewal")  # type: dict
            self.trust_net_cert_summary = trend.get("TrustNetCertSummary")  # type: dict
            self.protection_status_summary = trend.get("ProtectionStatusSummary")  # type: dict
