from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.flow import Flow
from typing import List


class _Flow:
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Flow')
        self.Tickets = self._Tickets(websdk_obj=websdk_obj)

    class _Tickets:
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Flow/Tickets')
            self.Approve = self._Approve(websdk_obj=websdk_obj)
            self.Count = self._Count(websdk_obj=websdk_obj)
            self.CountApproved = self._CountApproved(websdk_obj=websdk_obj)
            self.Enumerate = self._Enumerate(websdk_obj=websdk_obj)
            self.EnumerateApproved = self._EnumerateApproved(websdk_obj=websdk_obj)
            self.Load = self._Load(websdk_obj=websdk_obj)
            self.Reject = self._Reject(websdk_obj=websdk_obj)
            self.Update = self._Update(websdk_obj=websdk_obj)

        class _Approve(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Approve')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None, expires: str = None,
                     comment: str = None, not_before: str = None, use_count: int = None):
                body = {
                    'Expires': expires,
                    'Comment': comment,
                    'notBefore': not_before,
                    'TicketId': ticket_id,
                    'TicketIds': ticket_ids,
                    'useCount': use_count
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Count(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Count')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def count(self) -> int:
                        return self._from_json(key='Count')

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(
                    response=self._post(data={}),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _CountApproved(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/CountApproved')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def count(self) -> int:
                        return self._from_json(key='Count')

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(
                    response=self._post(data={}),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Enumerate(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Enumerate')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode': product_code,
                    'TicketPageSize': ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _EnumerateApproved(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/EnumerateApproved')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Load(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Load')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None):
                body = {
                    'TicketId': ticket_id,
                    'TicketIds': ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Reject(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Reject')

            def post(self, comment: str, rejection_level: int, ticket_id: int = None,
                     ticket_ids: List[int] = None):
                body = {
                    'Comment': comment,
                    'RejectionLevel': rejection_level,
                    'TicketId': ticket_id,
                    'TicketIds': ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def invalid_ticket_ids(self) -> List[int]:
                        return self._from_json(key='InvalidTicketIds')

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Update(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Flow/Tickets/Update')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None, expires: str = None,
                     comment: str = None, not_before: str = None, use_count: int = None):
                body = {
                    'Expires'  : expires,
                    'Comment'  : comment,
                    'notBefore': not_before,
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids,
                    'useCount' : use_count
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(
                            response=response,
                            expected_return_codes=expected_return_codes,
                            api_source=api_source
                        )

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )
