from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.plugins.properties.response_objects.dataclasses import certificate_dashboard


class CertificateDashboard:
    @staticmethod
    def Record(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate_dashboard.Record(
            filter_key=response_object.get("filterKey"),
            record=response_object.get("record"),
            record_value=response_object.get("recordValue"),
            is_risk=response_object.get("isRisk"),
            is_legend=response_object.get("isLegend"),
        )

    @staticmethod
    def Trend(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate_dashboard.Trend(
            date=from_date_string(response_object.get("date")),
            key_length=response_object.get("KeyLength"),
            signing_algorithm=response_object.get("SigningAlgorithm"),
            key_algorithm=response_object.get("KeyAlgorithm"),
            management_type=response_object.get("ManagementType"),
            issuer=response_object.get("Issuer"),
            validity_period=response_object.get("ValidityPeriod"),
            certificate_type=response_object.get("CertificateType"),
            total_certs=response_object.get("TotalCerts"),
            renewal=response_object.get("Renewal"),
            trust_net_cert_summary=response_object.get("TrustNetCertSummary"),
            protection_status_summary=response_object.get("ProtectionStatusSummary"),
        )
