from datetime import datetime
from typing import List
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField
from pytpp.properties.response_objects.dataclasses import workflow


class _Workflow:
    def __init__(self, api_obj):
        self.Ticket = self._Ticket(api_obj=api_obj)

    class _Ticket:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)
            self.Delete = self._Delete(api_obj=api_obj)
            self.Details = self._Details(api_obj=api_obj)
            self.Enumerate = self._Enumerate(api_obj=api_obj)
            self.Exists = self._Exists(api_obj=api_obj)
            self.Status = self._Status(api_obj=api_obj)
            self.UpdateStatus = self._UpdateStatus(api_obj=api_obj)

        class _Create(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Create')

            def post(self, object_dn: str, approvers: list, reason: str, workflow_dn: str, user_data: str = None):
                body = {
                    'ObjectDN'  : object_dn,
                    'Approvers' : approvers,
                    'Reason'    : reason,
                    'UserData'  : user_data,
                    'WorkflowDN': workflow_dn
                }

                class Response(APIResponse):
                    guid: str = ResponseField(alias='GUID')
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Delete(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Delete')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Response(APIResponse):
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Details(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Details')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Response(APIResponse):
                    approval_explanation: str = ResponseField(alias='ApprovalExplanation')
                    approval_from: str = ResponseField(alias='ApprovalFrom')
                    approval_reason: str = ResponseField(alias='ApprovalReason')
                    approvers: List[str] = ResponseField(alias='Approvers')
                    blocking: str = ResponseField(alias='Blocking')
                    created: datetime = ResponseField(alias='Created')
                    issued_due_to: str = ResponseField(alias='IssuedDueTo')
                    result: workflow.Result = ResponseField(alias='Result')
                    status: str = ResponseField(alias='Status')
                    updated: datetime = ResponseField(alias='Updated')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Enumerate(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Enumerate')

            def post(self, object_dn: str = None, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'UserData': user_data
                }

                class Response(APIResponse):
                    guids: List[str] = ResponseField(default_factory=list, alias='GUIDS')
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Exists(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Exists')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Response(APIResponse):
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Status(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/Status')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Response(APIResponse):
                    status: str = ResponseField(alias='Status')
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _UpdateStatus(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Workflow/Ticket/UpdateStatus')

            def post(self, guid: str, status: str, explanation: str = None, scheduled_start: str = None,
                     scheduled_stop: str = None, approvers: List[str] = None, object_dn: str = None,
                     reason: str = None, user_data=None):
                body = {
                    'GUID'          : guid,
                    'Status'        : status,
                    'Explanation'   : explanation,
                    'ScheduledStart': scheduled_start,
                    'ScheduledStop' : scheduled_stop,
                    'Approvers'     : approvers,
                    'ObjectDN'      : object_dn,
                    'Reason'        : reason,
                    'UserData'      : user_data
                }

                class Response(APIResponse):
                    result: workflow.Result = ResponseField(alias='Result')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))
