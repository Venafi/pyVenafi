from properties.response_objects.dataclasses import codesign, flow
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField
from typing import List


class _Flow:
    def __init__(self, api_obj):
        self.Actions = self._Actions(api_obj=api_obj)
        self.Tickets = self._Tickets(api_obj=api_obj)

    class _Actions:
        def __init__(self, api_obj):
            self.CodeSign = self._CodeSign(api_obj=api_obj)

        class _CodeSign:
            def __init__(self, api_obj):
                self.PreQualify = self._PreQualify(api_obj=api_obj)

            class _PreQualify:
                def __init__(self, api_obj):
                    self.Create = self._Create(api_obj=api_obj)

                class _Create(API):
                    def __init__(self, api_obj):
                        super().__init__(api_obj=api_obj, url='Flow/Actions/CodeSign/PreQualify/Create')

                    def post(self, comment: str, data: str, dn: str, user: str, hours: int = None,
                             single_use: bool = None):
                        body = {
                            'Comment'  : comment,
                            'Data'     : data,
                            'Dn'       : dn,
                            'Hours'    : hours,
                            'SingleUse': single_use,
                            'User'     : user
                        }

                        class Response(APIResponse):
                            result: codesign.ResultCode = ResponseField(
                                alias='Result', converter=lambda x: codesign.ResultCode(code=x)
                            )
                            success: bool = ResponseField(alias='Success')

                        return ResponseFactory(response_cls=Response, response=self._post(data=body))

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

                class Response(APIResponse):
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ResponseField(alias='Message')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Count(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Count')

            def post(self):
                class Response(APIResponse):
                    count: int = ResponseField(alias='Count')
                    message: str = ResponseField(alias='Message')
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))

                return ResponseFactory(response_cls=Response, response=self._post(data={}))

        class _CountApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/CountApproved')

            def post(self):
                class Response(APIResponse):
                    count: int = ResponseField(alias='Count')
                    message: str = ResponseField(alias='Message')
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))

                return ResponseFactory(response_cls=Response, response=self._post(data={}))

        class _Enumerate(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Enumerate')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class Response(APIResponse):
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ResponseField(alias='Message')
                    tickets: List[flow.Ticket] = ResponseField(alias='Tickets', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _EnumerateApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/EnumerateApproved')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class Response(APIResponse):
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ResponseField(alias='Message')
                    tickets: List[flow.Ticket] = ResponseField(alias='Tickets', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

        class _Load(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Load')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None):
                body = {
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids
                }

                class Response(APIResponse):
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ResponseField(alias='Message')
                    tickets: List[flow.Ticket] = ResponseField(alias='Tickets', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

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

                class Response(APIResponse):
                    invalid_ticket_ids: List[int] = ResponseField(default_factory=list, alias='InvalidTicketIds')
                    message: str = ResponseField(alias='Message')
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

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

                class Response(APIResponse):
                    result: flow.Result = ResponseField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ResponseField(alias='Message')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))
