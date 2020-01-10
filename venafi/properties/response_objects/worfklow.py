from typing import List
from venafi.properties.resultcodes import ResultCodes
from venafi.tools.helpers.date_converter import from_date_string


class Workflow:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.workflow_result = ResultCodes.Workflow.get(code, 'Unknown')

    class Details:
        def __init__(self, details_dict: dict):
            if not isinstance(details_dict, dict):
                details_dict = {}

            self.approval_explanation = details_dict.get('ApprovalExplanation')  # type: str
            self.approval_from = details_dict.get('ApprovalFrom')  # type: str
            self.approvers = details_dict.get('Approvers')  # type: List[str]
            self.blocking = details_dict.get('Blocking')  # type: str
            self.created = from_date_string(details_dict.get('Created'))
            self.issued_due_to = details_dict.get('IssuedDueTo')  # type: str
            self.status = details_dict.get('Status')  # type: str
            self.updated = from_date_string(details_dict.get('Updated'))
