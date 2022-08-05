from typing import List
from properties.response_objects.dataclasses import secret_store
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _X509CertificateStore:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Lookup = self._Lookup(api_obj=api_obj)
        self.LookupExpiring = self._LookupExpiring(api_obj=api_obj)
        self.Remove = self._Remove(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)

    class _Add(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Add')

        def post(self, owner_dn: str, certificate_collection_strings: list = None, certificate_string: str = None,
                 protection_key: str = None, typed_name_values: list = None):
            body = {
                'CertificateCollectionStrings': certificate_collection_strings,
                'CertificateString': certificate_string,
                'OwnerDN': owner_dn,
                'ProtectionKey': protection_key,
                'TypedNameValues': typed_name_values
            }

            class Response(APIResponse):
                leaf_existed: bool = ResponseField(alias='LeafExisted')
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ResponseField(alias='VaultId')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Lookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Lookup')

        def post(self, certificate_string: str = None, name: str = None, owner_dn: str = None, value: str = None):
            body = {
                'CertificateString': certificate_string,
                'Name': name,
                'OwnerDN': owner_dn,
                'Value': value
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ResponseField(alias='VaultId')
                vault_ids: List[int] = ResponseField(alias='VaultIds')
                certificate_collection_strings: List[str] = ResponseField(alias='CertificateCollectionStrings')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LookupExpiring(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/LookupExpiring')

        def post(self, days_to_expiration: int, owner_dn: str):
            body = {
                'DaysToExpiration': days_to_expiration,
                'OwnerDN': owner_dn
            }

            class Response(APIResponse):
                vault_ids: List[int] = ResponseField(alias='VaultIds')
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Remove(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Remove')

        def post(self, owner_dn: str, certificate: str = None, vault_id: int = None):
            body = {
                'Certificate': certificate,
                'OwnerDN': owner_dn,
                'VaultId': vault_id
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Retrieve')

        def post(self, vault_id: int):
            body = {
                'VaultId': vault_id
            }

            class Response(APIResponse):
                certificate_string: str = ResponseField(alias='CertificateString')
                typed_name_values: List[secret_store.TypedNameValues] = ResponseField(alias='TypedNameValues')
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))
