from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string
from typing import List


class Flow:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.flow_result = ResultCodes.Flow.get(code, 'Unknown')

    class Ticket:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.approvals = [Flow.Approval(a) for a in response_object.get('Approvals')]
            self.approvers = response_object.get('Approvers')  # type: List[str]
            self.creation_time = from_date_string(response_object.get('CreationTime'))
            self.environment = [Flow.KeyValue(i) for i in response_object.get('Environment')]
            self.flow_process_id = response_object.get('FlowProcessId')  # type: int
            self.id = response_object.get('Id')  # type: int
            self.identifier = response_object.get('Identifier')  # type: str
            self.product_code = response_object.get('ProductCode')  # type: int
            self.remaining_uses = response_object.get('RemainingUses')  # type: int
            self.required_approvals = response_object.get('RequiredApprovals')  # type: int

    class Approval:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.approval_time = from_date_string(response_object.get('ApprovalTime'))
            self.universal = response_object.get('Universal')  # type: str

    class KeyValue:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key = response_object.get('Key')  # type: str
            self.value = response_object.get('Value')  # type: str
