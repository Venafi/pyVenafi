from typing import List
from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string


class Workflow:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.workflow_result = ResultCodes.Workflow.get(code, 'Unknown')

    class Details:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.approval_explanation = response_object.get('ApprovalExplanation')  # type: str
            self.approval_from = response_object.get('ApprovalFrom')  # type: str
            self.approvers = response_object.get('Approvers')  # type: List[str]
            self.blocking = response_object.get('Blocking')  # type: str
            self.created = from_date_string(response_object.get('Created'))
            self.issued_due_to = response_object.get('IssuedDueTo')  # type: str
            self.status = response_object.get('Status')  # type: str
            self.updated = from_date_string(response_object.get('Updated'))
