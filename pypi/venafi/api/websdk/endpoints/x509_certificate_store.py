from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.secret_store import SecretStore


class _X509CertificateStore:
    def __init__(self, websdk_obj):
        self.Add = self._Add(websdk_obj=websdk_obj)
        self.Lookup = self._Lookup(websdk_obj=websdk_obj)
        self.LookupExpiring = self._LookupExpiring(websdk_obj=websdk_obj)
        self.Remove = self._Remove(websdk_obj=websdk_obj)
        self.Retrieve = self._Retrieve(websdk_obj=websdk_obj)

    class _Add(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/X509CertificateStore/Add', valid_return_codes=[200])

        @property
        @json_response_property()
        def leaf_existed(self) -> bool:
            return self.json_response('LeafExisted')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self.json_response('Result'))

        @property
        @json_response_property()
        def vault_id(self) -> int:
            return self.json_response('VaultId')

        def post(self, owner_dn: str, certificate_collection_strings: list = None, ceritificate_string: str = None,
                 protection_key: str = None, typed_name_values: list = None):
            body = {
                'CertificateCollectionStrings': certificate_collection_strings,
                'CertificateString': ceritificate_string,
                'OwnerDN': owner_dn,
                'ProtectionKey': protection_key,
                'TypedNameValues': typed_name_values
            }

            self.json_response = self._post(data=body)
            return self

    class _Lookup(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/X509CertificateStore/Lookup', valid_return_codes=[200])

        @property
        @json_response_property()
        def vault_id(self) -> int:
            return self.json_response('VaultId')

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self.json_response('VaultIds')

        @property
        @json_response_property()
        def certificate_collection_strings(self) -> List[str]:
            return self.json_response('CertificateCollectionStrings')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self.json_response('Result'))

        def post(self, certificate_string: str = None, name: str = None, owner_dn: str = None, value: str = None):
            body = {
                'CertificateString': certificate_string,
                'Name': name,
                'OwnerDN': owner_dn,
                'Value': value
            }

            self.json_response = self._post(data=body)
            return self

    class _LookupExpiring(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/X509CertificateStore/LookupExpiring', valid_return_codes=[200])

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self.json_response('VaultIds')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self.json_response('Result'))

        def post(self, days_to_expiration: int, owner_dn: str):
            body = {
                'DaysToExpiration': days_to_expiration,
                'OwnerDN': owner_dn
            }

            self.json_response = self._post(data=body)
            return self

    class _Remove(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/X509CertificateStore/Remove', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self.json_response('Result'))

        def post(self, owner_dn: str, certificate: str = None, vault_id: int = None):
            body = {
                'Certificate': certificate,
                'OwnerDN': owner_dn,
                'VaultId': vault_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Retrieve(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/X509CertificateStore/Retrieve', valid_return_codes=[200])

        @property
        @json_response_property()
        def certificate_string(self) -> str:
            return self.json_response('CertificateString')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self.json_response('Result'))

        @property
        @json_response_property()
        def typed_name_values(self):
            return SecretStore.TypedNameValues(self.json_response('TypedNameValues'))

        def post(self, vault_id: int):
            body = {
                'VaultId': vault_id
            }

            self.json_response = self._post(data=body)
            return self
