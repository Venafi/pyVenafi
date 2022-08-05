from typing import List
from pytpp.properties.response_objects.dataclasses import hsm_api
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _HSMAPI:
    def __init__(self, api_obj):
        self.Sign = self._Sign(api_obj=api_obj)
        self.SignJWT = self._SignJWT(api_obj=api_obj)
        self.GetGPGPublicKey = self._GetGPGPublicKey(api_obj=api_obj)

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
                'ClientInfo'      : client_info,
                'ClientMechanism' : client_mechanism,
                'Data'            : data,
                'Justification'   : justification,
                'KeyContext'      : key_context,
                'KeyContextToWrap': key_context_to_wrap,
                'KeyId'           : key_id,
                'KeyIdToWrap'     : key_id_to_wrap,
                'Mechanism'       : mechanism,
                'Parameter'       : parameter,
                'Password'        : password,
                'ProcessInfo'     : process_info,
                'Username'        : username,
                'VerifyData'      : verify_data,
                'WrappingKeyId'   : wrapping_key_id
            }

            class Response(APIResponse):
                result_data: str = ResponseField(alias='ResultData')
                success: bool = ResponseField(alias='Success')
                try_later: bool = ResponseField(alias='TryLater')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _SignJWT(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/SignJWT')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, client_info: dict, process_info: dict, key_id: str,
                 header: str, payload: str):
            body = {
                'ClientInfo' : client_info,
                'ProcessInfo': process_info,
                'KeyId'      : key_id,
                'Header'     : header,
                'Payload'    : payload
            }

            class Response(APIResponse):
                result_data: str = ResponseField(alias='ResultData')
                success: bool = ResponseField(alias='Success')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetGPGPublicKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/GetGPGPublicKey')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, key_id: str, key_context: str = None):
            body = {
                'KeyId'     : key_id,
                'KeyContext': key_context
            }

            class Response(APIResponse):
                fingerprint: str = ResponseField(alias='Fingerprint')
                location: str = ResponseField(alias='Location')
                public_key: str = ResponseField(alias='PublicKey')
                success: bool = ResponseField(alias='Success')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetObjects(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/GetObjects')

        def post(self, environment_filter: List[int] = None, include_chains: bool = None, include_archived: bool = None,
                 key_id: str = None, key_context: str = None, object_type_filter: List[int] = None):
            body = {
                'EnvironmentFilter': environment_filter,
                'IncludeChains'    : include_chains,
                'IncludeArchived'  : include_archived,
                'KeyId'            : key_id,
                'KeyContext'       : key_context,
                'ObjectTypeFilter' : object_type_filter,
            }

            class Response(APIResponse):
                certificates: List[hsm_api.Certificate] = ResponseField(alias='Certificates', default_factory=list)
                pending: bool = ResponseField(alias='PendingDeprecationWarningbool')
                private_keys: List[hsm_api.PrivateKey] = ResponseField(alias='PrivateKeys')
                public_keys: List[hsm_api.PublicKey] = ResponseField(alias='PublicKeys')
                success: bool = ResponseField(alias='Success')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))
