from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.worfklow import Workflow


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
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Create')

            def post(self, object_dn: str, approvers: list, reason: str, workflow_dn: str, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'Approvers': approvers,
                    'Reason': reason,
                    'UserData': user_data,
                    'WorkflowDN': workflow_dn
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def guid(self) -> str:
                        return self._from_json('GUID')

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Delete(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Delete')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Details(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Details')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def details(self):
                        return Workflow.Details(self._from_json())

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Enumerate(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Enumerate')

            def post(self, object_dn: str = None, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'UserData': user_data
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def guids(self) -> List[str]:
                        return self._from_json('GUIDS')

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Exists(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Exists')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Status(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Status')

            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def status(self) -> str:
                        return self._from_json('Status')

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _UpdateStatus(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/UpdateStatus')

            def post(self, guid: str, status: str, explanation: str = None, scheduled_start: str = None, scheduled_stop: str = None):
                body = {
                    'GUID': guid,
                    'Status': status,
                    'Explanation': explanation,
                    'ScheduledStart': scheduled_start,
                    'ScheduledStop': scheduled_stop
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def result(self):
                        return Workflow.Result(self._from_json('Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )
