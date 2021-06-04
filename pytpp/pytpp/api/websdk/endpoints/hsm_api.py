from pytpp.api.api_base import API, APIResponse, json_response_property


class _HSMAPI:
    def __init__(self, api_obj):
        self.Sign = self._Sign(api_obj=api_obj)

    class _Sign(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/Sign')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, client_info: dict, data: str, key_context: str, key_id: int, mechanism: int,
                 process_info: dict, client_mechanism: str = None, justification: str = None,
                 key_context_to_wrap: int = None, key_id_to_wrap: int = None, parameter: dict = None,
                 password: str = None, username: str = None, verify_data: bool = None,
                 wrapping_key_id: int = None):
            body = {
                'ClientInfo': client_info,
                'ClientMechanism': client_mechanism,
                'Data': data,
                'Justification': justification,
                'KeyContext': key_context,
                'KeyContextToWrap': key_context_to_wrap,
                'KeyId': key_id,
                'KeyIdToWrap': key_id_to_wrap,
                'Mechanism': mechanism,
                'Parameter': parameter,
                'Password': password,
                'ProcessInfo': process_info,
                'Username': username,
                'VerifyData': verify_data,
                'WrappingKeyId': wrapping_key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @json_response_property()
                def result_data(self) -> str:
                    return self._from_json(key='ResultData')

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

                @property
                @json_response_property()
                def try_later(self) -> bool:
                    return self._from_json(key='TryLater')

            return _Response(response=self._post(data=body))
