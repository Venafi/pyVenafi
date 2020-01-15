from typing import List 
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.secret_store import SecretStore


class _SecretStore:
    def __init__(self, websdk_obj):
        self.Add = self._Add(websdk_obj=websdk_obj)
        self.Associate = self._Associate(websdk_obj=websdk_obj)
        self.Delete = self._Delete(websdk_obj=websdk_obj)
        self.Dissociate = self._Dissociate(websdk_obj=websdk_obj)
        self.EncryptionKeysInUse = self._EncryptionKeysInUse(websdk_obj=websdk_obj)
        self.Lookup = self._Lookup(websdk_obj=websdk_obj)
        self.LookupAllAssociationsbyVaultid = self._LookupAllAssociationsbyVaultid(websdk_obj=websdk_obj)
        self.LookupByAssociation = self._LookupByAssociation(websdk_obj=websdk_obj)
        self.LookupAssociationbyVaultID = self._LookupAssociationbyVaultID(websdk_obj=websdk_obj)
        self.LookupByOwner = self._LookupByOwner(websdk_obj=websdk_obj)
        self.LookupByVaultType = self._LookupByVaultType(websdk_obj=websdk_obj)
        self.Mutate = self._Mutate(websdk_obj=websdk_obj)
        self.OrphanLookup = self._OrphanLookup(websdk_obj=websdk_obj)
        self.OwnerAdd = self._OwnerAdd(websdk_obj=websdk_obj)
        self.OwnerDelete = self._OwnerDelete(websdk_obj=websdk_obj)
        self.OwnerLookup = self._OwnerLookup(websdk_obj=websdk_obj)
        self.Retrieve = self._Retrieve(websdk_obj=websdk_obj)

    class _Add(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Add', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_id(self) -> int:
            return self._from_json(key='VaultID')

        def post(self, base_64_data: str, keyname: str, namespace: str, owner: str, vault_type: int):
            body = {
                'Base64Data': base_64_data,
                'Keyname': keyname,
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            }

            self.json_response = self._post(data=body)
            return self

    class _Associate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Associate', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, name: str, vault_id: int, date_value: int = None, int_value: int = None, string_value: str = None):
            body = {
                'Name': name,
                'VaultID': vault_id,
                'DateValue': date_value,
                'IntValue': int_value,
                'StringValue': string_value
            }

            self.json_response = self._post(data=body)
            return self

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Delete', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Dissociate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Dissociate', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, vault_id: int, int_value: int = None, name: str = None, string_value: str = None, date_value: int = None):
            body = {
                'VaultID': vault_id,
                'IntValue': int_value,
                'Name': name,
                'StringValue': string_value,
                'DateValue': date_value
            }

            self.json_response = self._post(data=body)
            return self

    class _EncryptionKeysInUse(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/EncryptionKeysInUse', valid_return_codes=[200])

        @property
        @json_response_property()
        def encryption_keys(self) -> List[str]:
            return self._from_json(key='EncryptionKeys')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def get(self):
            self.json_response = self._get()
            return self

    class _Lookup(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Lookup', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self._from_json(key='VaultIDs')

        def get(self):
            self.json_response = self._get()
            return self

    class _LookupAllAssociationsbyVaultid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/LookupAllAssociationsbyVaultid', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def typed_name_values(self):
            return [SecretStore.TypedNameValues(tnv) for tnv in self._from_json('TypedNameValues')]

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            self.json_response = self._post(data=body)
            return self

    class _LookupByAssociation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/LookupByAssociation', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self._from_json(key='VaultIDs')

        def post(self, name: str, int_value: int = None ,string_value: str = None, date_value: int = None):
            body = {
                'Name': name
            }
            if int_value:
                body.update({'IntValue': int_value})

            if string_value:
                body.update({'StringValue': string_value})

            if date_value:
                body.update({'DateValue': date_value})

            self.json_response = self._post(data=body)
            return self

    class _LookupAssociationbyVaultID(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/LookupAssociationbyVaultID', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def value(self) -> str:
            return self._from_json(key='Value')

        def post(self, vault_id: int, name: str = None):
            body = {
                'VaultID': vault_id
            }

            if name:
                body.update({'Name': name})

            self.json_response = self._post(data=body)
            return self

    class _LookupByOwner(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/LookupByOwner', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self._from_json(key='VaultIDs')

        def post(self, namespace: str, owner: str, vault_type: str = None):
            body = {
                'Namespace': namespace,
                'Owner': owner
            }
            if vault_type:
                body.update({'VaultType': vault_type})

            self.json_response = self._post(data=body)
            return self

    class _LookupByVaultType(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/LookupByVaultType', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self._from_json(key='VaultIDs')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            self.json_response = self._post(data=body)
            return self

    class _Mutate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Mutate', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, vault_id: int, vault_type: int):
            body = {
                'VaultID': vault_id,
                'VaultType': vault_type
            }

            self.json_response = self._post(data=body)
            return self

    class _OrphanLookup(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/OrphanLookup', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_ids(self) -> List[int]:
            return self._from_json(key='VaultIDs')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            self.json_response = self._post(data=body)
            return self

    class _OwnerAdd(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/OwnerAdd', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, namespace: str, owner: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            }

            self.json_response = self._post(data=body)
            return self

    class _OwnerDelete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/OwnerDelete', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        def post(self, namespace: str, owner: str, vault_id: int = None):
            body = {
                'Namespace': namespace,
                'Owner': owner
            }

            if vault_id:
                body.update({'VaultId': vault_id})

            self.json_response = self._post(data=body)
            return self

    class _OwnerLookup(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/OwnerLookup', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def owners(self) -> List[str]:
            return self._from_json(key='Owners')

        def post(self, namespace: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'VaultID': vault_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Retrieve(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SecretStore/Retrieve', valid_return_codes=[200])

        @property
        @json_response_property()
        def base_64_data(self) -> str:
            return self._from_json(key='Base64Data')

        @property
        @json_response_property()
        def result(self):
            return SecretStore.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def vault_type(self) -> str:
            return self._from_json(key='VaultType')

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            self.json_response = self._post(data=body)
            return self
