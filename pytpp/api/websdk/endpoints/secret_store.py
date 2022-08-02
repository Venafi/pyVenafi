from typing import List
from properties.response_objects.dataclasses import secret_store
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _SecretStore:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Associate = self._Associate(api_obj=api_obj)
        self.Dissociate = self._Dissociate(api_obj=api_obj)
        self.EncryptionKeysInUse = self._EncryptionKeysInUse(api_obj=api_obj)
        self.Lookup = self._Lookup(api_obj=api_obj)
        self.LookupAllAssociationsbyVaultid = self._LookupAllAssociationsbyVaultid(api_obj=api_obj)
        self.LookupByAssociation = self._LookupByAssociation(api_obj=api_obj)
        self.LookupAssociationbyVaultID = self._LookupAssociationbyVaultID(api_obj=api_obj)
        self.LookupByOwner = self._LookupByOwner(api_obj=api_obj)
        self.LookupByVaultType = self._LookupByVaultType(api_obj=api_obj)
        self.Mutate = self._Mutate(api_obj=api_obj)
        self.OrphanLookup = self._OrphanLookup(api_obj=api_obj)
        self.OwnerAdd = self._OwnerAdd(api_obj=api_obj)
        self.OwnerDelete = self._OwnerDelete(api_obj=api_obj)
        self.OwnerLookup = self._OwnerLookup(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)

    class _Add(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Add')

        def post(self, base_64_data: str, keyname: str, namespace: str, owner: str, vault_type: int):
            body = {
                'Base64Data': base_64_data,
                'Keyname': keyname,
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ResponseField(alias='VaultID')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Associate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Associate')

        def post(self, name: str, vault_id: int, date_value: str = None, int_value: int = None, string_value: str = None):
            body = {
                'Name': name,
                'VaultID': vault_id,
                'DateValue': date_value,
                'IntValue': int_value,
                'StringValue': string_value
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Dissociate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Dissociate')

        def post(self, vault_id: int, int_value: int = None, name: str = None, string_value: str = None, date_value: int = None):
            body = {
                'VaultID': vault_id,
                'IntValue': int_value,
                'Name': name,
                'StringValue': string_value,
                'DateValue': date_value
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _EncryptionKeysInUse(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/EncryptionKeysInUse')

        def get(self):
            class Response(APIResponse):
                encryption_keys: List[str] = ResponseField(default_factory=list, alias='EncryptionKeys')
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._get())

    class _Lookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Lookup')

        def get(self):
            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ResponseField(default_factory=list, alias='VaultIDs')

            return ResponseFactory(response_cls=Response, response=self._get())

    class _LookupAllAssociationsbyVaultid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupAllAssociationsbyVaultid')

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                typed_name_values: List[secret_store.TypedNameValues] = ResponseField(default_factory=list, alias='TypedNameValues')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LookupByAssociation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByAssociation')

        def post(self, name: str, int_value: int = None, string_value: str = None, date_value: int = None):
            body = {
                'Name': name,
                'IntValue': int_value,
                'StringValue': string_value,
                'DateValue': date_value
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ResponseField(default_factory=list, alias='VaultIDs')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LookupAssociationbyVaultID(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupAssociationbyVaultID')

        def post(self, vault_id: int, name: str = None):
            body = {
                'VaultID': vault_id,
                'Name': name
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                value: str = ResponseField(alias='Value')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LookupByOwner(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByOwner')

        def post(self, namespace: str, owner: str, vault_type: str = None):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ResponseField(default_factory=list, alias='VaultIDs')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LookupByVaultType(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByVaultType')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ResponseField(default_factory=list, alias='VaultIDs')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Mutate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Mutate')

        def post(self, vault_id: int, vault_type: int):
            body = {
                'VaultID': vault_id,
                'VaultType': vault_type
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _OrphanLookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OrphanLookup')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ResponseField(default_factory=list, alias='VaultIDs')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _OwnerAdd(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerAdd')

        def post(self, namespace: str, owner: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _OwnerDelete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerDelete')

        def post(self, namespace: str, owner: str, vault_id: int = None):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _OwnerLookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerLookup')

        def post(self, namespace: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'VaultID': vault_id
            }

            class Response(APIResponse):
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                owners: List[str] = ResponseField(default_factory=list, alias='Owners')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Retrieve')

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class Response(APIResponse):
                base_64_data: str = ResponseField(alias='Base64Data')
                result: secret_store.Result = ResponseField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_type: str = ResponseField(alias='VaultType')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))
