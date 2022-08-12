from pytpp.api.websdk.models import codesign, flow
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
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

                class _Create(WebSdkEndpoint):
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

                        class Output(WebSdkOutputModel):
                            result: codesign.ResultCode = ApiField(
                                alias='Result', converter=lambda x: codesign.ResultCode(code=x)
                            )
                            success: bool = ApiField(alias='Success')

                        return generate_output(output_cls=Output, response=self._post(data=body))

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

        class _Approve(WebSdkEndpoint):
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

                class Output(WebSdkOutputModel):
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ApiField(alias='Message')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Count(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Count')

            def post(self):
                class Output(WebSdkOutputModel):
                    count: int = ApiField(alias='Count')
                    message: str = ApiField(alias='Message')
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data={}))

        class _CountApproved(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/CountApproved')

            def post(self):
                class Output(WebSdkOutputModel):
                    count: int = ApiField(alias='Count')
                    message: str = ApiField(alias='Message')
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data={}))

        class _Enumerate(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Enumerate')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class Output(WebSdkOutputModel):
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ApiField(alias='Message')
                    tickets: List[flow.Ticket] = ApiField(alias='Tickets', default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _EnumerateApproved(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/EnumerateApproved')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class Output(WebSdkOutputModel):
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ApiField(alias='Message')
                    tickets: List[flow.Ticket] = ApiField(alias='Tickets', default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Load(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Load')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None):
                body = {
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids
                }

                class Output(WebSdkOutputModel):
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ApiField(alias='Message')
                    tickets: List[flow.Ticket] = ApiField(alias='Tickets', default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Reject(WebSdkEndpoint):
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

                class Output(WebSdkOutputModel):
                    invalid_ticket_ids: List[int] = ApiField(default_factory=list, alias='InvalidTicketIds')
                    message: str = ApiField(alias='Message')
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Update(WebSdkEndpoint):
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

                class Output(WebSdkOutputModel):
                    result: flow.Result = ApiField(alias='Result', converter=lambda x: flow.Result(code=x))
                    message: str = ApiField(alias='Message')

                return generate_output(output_cls=Output, response=self._post(data=body))
