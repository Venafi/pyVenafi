from typing import List
from pytpp.api.websdk.outputs import hsm_api
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _HSMAPI:
    def __init__(self, api_obj):
        self.Sign = self._Sign(api_obj=api_obj)
        self.SignJWT = self._SignJWT(api_obj=api_obj)
        self.GetGPGPublicKey = self._GetGPGPublicKey(api_obj=api_obj)

    class _Sign(WebSdkEndpoint):
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

            class Output(WebSdkOutputModel):
                result_data: str = ApiField(alias='ResultData')
                success: bool = ApiField(alias='Success')
                try_later: bool = ApiField(alias='TryLater')

            return generate_output(output=Output, response=self._post(data=body))

    class _SignJWT(WebSdkEndpoint):
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

            class Output(WebSdkOutputModel):
                result_data: str = ApiField(alias='ResultData')
                success: bool = ApiField(alias='Success')

            return generate_output(output=Output, response=self._post(data=body))

    class _GetGPGPublicKey(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/GetGPGPublicKey')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, key_id: str, key_context: str = None):
            body = {
                'KeyId'     : key_id,
                'KeyContext': key_context
            }

            class Output(WebSdkOutputModel):
                fingerprint: str = ApiField(alias='Fingerprint')
                location: str = ApiField(alias='Location')
                public_key: str = ApiField(alias='PublicKey')
                success: bool = ApiField(alias='Success')

            return generate_output(output=Output, response=self._post(data=body))

    class _GetObjects(WebSdkEndpoint):
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

            class Output(WebSdkOutputModel):
                certificates: List[hsm_api.Certificate] = ApiField(alias='Certificates', default_factory=list)
                pending: bool = ApiField(alias='PendingDeprecationWarningbool')
                private_keys: List[hsm_api.PrivateKey] = ApiField(alias='PrivateKeys')
                public_keys: List[hsm_api.PublicKey] = ApiField(alias='PublicKeys')
                success: bool = ApiField(alias='Success')

            return generate_output(output=Output, response=self._post(data=body))
