from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.plugins.properties.response_objects.dataclasses import ssh_dashboard


class SshDashboard:
    @staticmethod
    def PolicyViolation(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_dashboard.PolicyViolation(
            name=response_object.get("name"),
            items=response_object.get("items"),
            total_items=response_object.get("totalItems"),
        )

    @staticmethod
    def Record(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_dashboard.Record(
            record=response_object.get("record"),
            record_value=response_object.get("recordValue"),
            is_risk=response_object.get("isRisk"),
            is_legend=response_object.get("isLegend"),
        )

    @staticmethod
    def Trend(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_dashboard.Trend(
            date=from_date_string(response_object.get("date")),
            orphans=response_object.get("TGOrphans"),
            non_compliant_hosts=response_object.get("TGNonCompliantHosts"),
            non_compliant_keys=response_object.get("TGNonCompliantKeys"),
            agents=response_object.get("TGAgents"),
            duplicate_private_keys=response_object.get("TGDuplicatePrivateKeys"),
            policy_violations_summary=response_object.get("TGPolicyViolationsSummary"),
            key_lengths=response_object.get("TGKeyLengths"),
            algorithms=response_object.get("TGAlgorithms"),
            vendor_formats=response_object.get("TGVendorFormats"),
        )
