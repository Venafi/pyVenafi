from pytpp.tools.helpers.date_converter import from_date_string
from typing import List


class SshDashboard:
    class PolicyViolation:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.name = response_object.get("name") # type: str
            self.items = response_object.get("items") # type: List
            self.total_items = response_object.get("totalItems") # type: int

    class Record:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.record = response_object.get("record")  # type: str
            self.record_value = response_object.get("recordValue")  # type: int
            self.is_risk = response_object.get("isRisk")  # type: bool
            self.is_legend = response_object.get("isLegend")  # type: bool

    class Trend:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.date = from_date_string(response_object.get("date"))
            self.orphans = response_object.get("TGOrphans")  # type: dict
            self.non_compliant_hosts = response_object.get("TGNonCompliantHosts")  # type: dict
            self.non_compliant_keys = response_object.get("TGNonCompliantKeys")  # type: dict
            self.agents = response_object.get("TGAgents")  # type: dict
            self.duplicate_private_keys = response_object.get("TGDuplicatePrivateKeys")  # type: dict
            self.policy_violations_summary = response_object.get("TGPolicyViolationsSummary")  # type: dict
            self.key_lengths = response_object.get("TGKeyLengths")  # type: dict
            self.algorithms = response_object.get("TGAlgorithms")  # type: dict
            self.vendor_formats = response_object.get("TGVendorFormats")  # type: dict

