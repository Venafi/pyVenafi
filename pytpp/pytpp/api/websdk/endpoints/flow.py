from pytpp.api.api_base import API, APIResponse, json_response_property
from pytpp.properties.response_objects.flow import Flow
from typing import List


class _Flow:
    def __init__(self, api_obj):
        self.Tickets = self._Tickets(api_obj=api_obj)

    class _Tickets:
        def __init__(self, api_obj):
            self.Approve = self._Approve(api_obj=api_obj)
            self.Count = self._Count(api_obj=api_obj)
            self.CountApproved = self._CountApproved(api_obj=api_obj)
            self.Enumerate = self._Enumerate(api_obj=api_obj)
            self.EnumerateApproved = self._EnumerateApproved(api_obj=api_obj)
            self.Load = self._Load(api_obj=api_obj)
            self.Reject = self._Reject(api_obj=api_obj)
            self.Update = self._Update(api_obj=api_obj)

        class _Approve(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Approve')

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
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(response=self._post(data=body))

        class _Count(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Count')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data={}))

        class _CountApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/CountApproved')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data={}))

        class _Enumerate(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Enumerate')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data=body))

        class _EnumerateApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/EnumerateApproved')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data=body))

        class _Load(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Load')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None):
                body = {
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data=body))

        class _Reject(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Reject')

            def post(self, comment: str, rejection_level: int, ticket_id: int = None,
                     ticket_ids: List[int] = None):
                body = {
                    'Comment'       : comment,
                    'RejectionLevel': rejection_level,
                    'TicketId'      : ticket_id,
                    'TicketIds'     : ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

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

                return _Response(response=self._post(data=body))

        class _Update(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Update')

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
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @json_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @json_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(response=self._post(data=body))
