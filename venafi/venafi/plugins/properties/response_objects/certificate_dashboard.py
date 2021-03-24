from venafi.tools.helpers.date_converter import from_date_string


class CertificateDashboard:
    class Record:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.filter_key = response_object.get("filterKey")  # type: str
            self.record = response_object.get("record")  # type: str
            self.record_value = response_object.get("recordValue")  # type: int
            self.is_risk = response_object.get("isRisk")  # type: bool
            self.is_legend = response_object.get("isLegend")  # type: bool

    class Trend:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.date = from_date_string(response_object.get("date"))
            self.key_length = response_object.get("KeyLength")  # type: dict
            self.signing_algorithm = response_object.get("SigningAlgorithm")  # type: dict
            self.key_algorithm = response_object.get("KeyAlgorithm")  # type: dict
            self.management_type = response_object.get("ManagementType")  # type: dict
            self.issuer = response_object.get("Issuer")  # type: dict
            self.validity_period = response_object.get("ValidityPeriod")  # type: dict
            self.certificate_type = response_object.get("CertificateType")  # type: dict
            self.total_certs = response_object.get("TotalCerts")  # type: dict
            self.renewal = response_object.get("Renewal")  # type: dict
            self.trust_net_cert_summary = response_object.get("TrustNetCertSummary")  # type: dict
            self.protection_status_summary = response_object.get("ProtectionStatusSummary")  # type: dict
