from typing import List 
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.worfklow import Workflow
from venafi.tools.helpers.date_converter import from_date_string


class _Workflow:
    def __init__(self, websdk_obj):
        self.Ticket = self._Ticket(websdk_obj=websdk_obj)

    class _Ticket:
        def __init__(self, websdk_obj):
            self.Create = self._Create(websdk_obj=websdk_obj)
            self.Delete = self._Delete(websdk_obj=websdk_obj)
            self.Details = self._Details(websdk_obj=websdk_obj)
            self.Enumerate = self._Enumerate(websdk_obj=websdk_obj)
            self.Exists = self._Exists(websdk_obj=websdk_obj)
            self.Status = self._Status(websdk_obj=websdk_obj)
            self.UpdateStatus = self._UpdateStatus(websdk_obj=websdk_obj)

        class _Create(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Create', valid_return_codes=[200])

            @property
            @json_response_property()
            def guid(self) -> str:
                return self._from_json('GUID')

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, object_dn: str, approvers: list, reason: str, workflow_dn: str, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'Approvers': approvers,
                    'Reason': reason,
                    'UserData': user_data,
                    'WorkflowDN': workflow_dn
                }

                self.json_response = self._post(data=body)
                return self

        class _Delete(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Delete', valid_return_codes=[200])

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                self.json_response = self._post(data=body)
                return self

        class _Details(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Details', valid_return_codes=[200])

            @property
            @json_response_property()
            def details(self):
                return Workflow.Details(self._from_json())

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                self.json_response = self._post(data=body)
                return self

        class _Enumerate(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Enumerate', valid_return_codes=[200])

            @property
            @json_response_property()
            def guids(self) -> List[str]:
                return self._from_json('GUIDS')

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, object_dn: str = None, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'UserData': user_data
                }

                self.json_response = self._post(data=body)
                return self

        class _Exists(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Exists', valid_return_codes=[200])

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                self.json_response = self._post(data=body)
                return self

        class _Status(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Status', valid_return_codes=[200])

            @property
            @json_response_property()
            def status(self) -> str:
                return self._from_json('Status')

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                self.json_response = self._post(data=body)
                return self

        class _UpdateStatus(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/UpdateStatus', valid_return_codes=[200])

            @property
            @json_response_property()
            def result(self):
                return Workflow.Result(self._from_json('Result'))

            def post(self, guid: str, status: str, explanation: str = None, scheduled_start: str = None, scheduled_stop: str = None):
                body = {
                    'GUID': guid,
                    'Status': status,
                    'Explanation': explanation,
                    'ScheduledStart': scheduled_start,
                    'ScheduledStop': scheduled_stop
                }

                self.json_response = self._post(data=body)
                return self
