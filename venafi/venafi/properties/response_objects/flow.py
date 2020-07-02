from venafi.properties.resultcodes import ResultCodes
from venafi.tools.helpers.date_converter import from_date_string
from typing import List


class Flow:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.flow_result = ResultCodes.Flow.get(code, 'Unknown')

    class Ticket:
        def __init__(self, ticket_dict: dict):
            if not isinstance(ticket_dict, dict):
                ticket_dict = {}

            self.approvals = [Flow.Approval(a) for a in ticket_dict.get('Approvals')]
            self.approvers = ticket_dict.get('Approvers')  # type: List[str]
            self.creation_time = from_date_string(ticket_dict.get('CreationTime'))
            self.environment = [Flow.KeyValue(i) for i in ticket_dict.get('Environment')]
            self.flow_process_id = ticket_dict.get('FlowProcessId')  # type: int
            self.id = ticket_dict.get('Id')  # type: int
            self.identifier = ticket_dict.get('Identifier')  # type: str
            self.product_code = ticket_dict.get('ProductCode')  # type: int
            self.remaining_uses = ticket_dict.get('RemainingUses')  # type: int
            self.required_approvals = ticket_dict.get('RequiredApprovals')  # type: int

    class Approval:
        def __init__(self, approval_dict: dict):
            if not isinstance(approval_dict, dict):
                approval_dict = {}

            self.approval_time = from_date_string(approval_dict.get('ApprovalTime'))
            self.universal = approval_dict.get('Universal')  # type: str

    class KeyValue:
        def __init__(self, key_value_dict: dict):
            if not isinstance(key_value_dict, dict):
                key_value_dict = {}

            self.key = key_value_dict.get('Key')  # type: str
            self.value = key_value_dict.get('Value')  # type: str
