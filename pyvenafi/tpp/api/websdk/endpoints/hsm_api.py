from __future__ import annotations

from typing import (
    Union,
)

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import hsm_api

class _HSMAPI(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/API')
        self._url = self._url.replace('vedsdk', 'vedhsm')
        self.Decrypt = self._Decrypt(api_obj=api_obj, url=f'{self._url}/decrypt')
        self.Derive = self._Derive(api_obj=api_obj, url=f'{self._url}/derive')
        self.GetChain = self._GetChain(api_obj=api_obj, url=f'{self._url}/getchain')
        self.GetGPGPublicKey = self._GetGPGPublicKey(api_obj=self._api_obj, url=f'{self._url}/GetGPGPublicKey')
        self.GetObjects = self._GetObjects(api_obj=self._api_obj, url=f'{self._url}/GetObjects')
        self.IsHsm = self._IsHsm(api_obj=api_obj, url=f'{self._url}/IsHsm')
        self.Sign = self._Sign(api_obj=self._api_obj, url=f'{self._url}/Sign')
        self.SignJWT = self._SignJWT(api_obj=self._api_obj, url=f'{self._url}/SignJWT')
        self.StoreObject = self._StoreObject(api_obj=api_obj, url=f'{self._url}/storeobject')

    class _IsHsm(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                vedauth: str = ApiField(alias='vedauth')
                pks: str = ApiField(alias='pks')
                timestamp: str = ApiField(alias='timestamp')
                csc: str = ApiField(alias='csc')

            return generate_output(output_cls=Output, response=self._get())

    class _Decrypt(WebSdkEndpoint):
        def post(self, key_id: str, data: str):
            body = {
                "KeyId": key_id,
                "Data": data,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                error: str = ApiField(alias='Error')
                try_later: bool = ApiField(alias='TryLater')
                result_data: str = ApiField(alias='ResultData')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Derive(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                error: str = ApiField(alias='Error')
                try_later: bool = ApiField(alias='TryLater')
                request_thumbprint: str = ApiField(alias='RequestThumbprint')
                result_data: str = ApiField(alias='ResultData')

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _StoreObject(WebSdkEndpoint):
        def post(
            self,
            key_id: str = None,
            key_creation_timestamp: str = None,
            key_context: str = None,
            public_key: str = None,
            private_key: str = None,
            private_key_password: str = None,
        ):
            body = {
                "KeyId"               : key_id,
                "KeyCreationTimestamp": key_creation_timestamp,
                "KeyContext"          : key_context,
                "PublicKey"           : public_key,
                "PrivateKey"          : private_key,
                "PrivateKeyPassword"  : private_key_password,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetChain(WebSdkEndpoint):
        def post(self, key_id: str):
            body = {
                "KeyId": key_id,
            }

            class Output(WebSdkOutputModel):
                certificates: list[hsm_api.Certificate] = ApiField(alias='Certificates')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Sign(WebSdkEndpoint):
        def post(
            self,
            client_info: Union[dict, hsm_api.ClientInfo],
            data: str,
            key_context: str,
            key_id: int,
            mechanism: int,
            process_info: Union[dict, hsm_api.ProcessInfo],
            client_mechanism: str = None,
            justification: str = None,
            key_context_to_wrap: int = None,
            key_id_to_wrap: int = None,
            parameter: Union[dict, hsm_api.Parameter] = None,
            password: str = None,
            username: str = None,
            verify_data: bool = None,
            wrapping_key_id: int = None
        ):
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

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SignJWT(WebSdkEndpoint):
        def post(
            self,
            client_info: Union[dict, hsm_api.ClientInfo],
            process_info: Union[dict, hsm_api.ProcessInfo],
            key_id: str,
            header: str,
            payload: str
        ):
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

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetGPGPublicKey(WebSdkEndpoint):
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

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetObjects(WebSdkEndpoint):
        def post(
            self, environment_filter: list[int] = None, include_chains: bool = None, include_archived: bool = None,
            key_id: str = None, key_context: str = None, object_type_filter: list[int] = None
        ):
            body = {
                'EnvironmentFilter': environment_filter,
                'IncludeChains'    : include_chains,
                'IncludeArchived'  : include_archived,
                'KeyId'            : key_id,
                'KeyContext'       : key_context,
                'ObjectTypeFilter' : object_type_filter,
            }

            class Output(WebSdkOutputModel):
                certificates: list[hsm_api.Certificate] = ApiField(alias='Certificates', default_factory=list)
                pending: bool = ApiField(alias='Pending')
                private_keys: list[hsm_api.PrivateKey] = ApiField(alias='PrivateKeys', default_factory=list)
                public_keys: list[hsm_api.PublicKey] = ApiField(alias='PublicKeys', default_factory=list)
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))
