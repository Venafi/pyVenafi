import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from objects.response_objects.secret_store import SecretStore


class _SecretStore:
    def __init__(self, session, api_type):
        self.Add = self._Add(session=session, api_type=api_type)
        self.Associate = self._Associate(session=session, api_type=api_type)
        self.Delete = self._Delete(session=session, api_type=api_type)
        self.Dissociate = self._Dissociate(session=session, api_type=api_type)
        self.EncryptionKeysInUse = self._EncryptionKeysInUse(session=session, api_type=api_type)
        self.Lookup = self._Lookup(session=session, api_type=api_type)
        self.LookupAllAssocationsbyVaultid = self._LookupAllAssocationsbyVaultid(session=session, api_type=api_type)
        self.LookupByAssociation = self._LookupByAssociation(session=session, api_type=api_type)
        self.LookupAssocationbyVaultID = self._LookupAssocationbyVaultID(session=session, api_type=api_type)
        self.LookupByOwner = self._LookupByOwner(session=session, api_type=api_type)
        self.LookupByVaultType = self._LookupByVaultType(session=session, api_type=api_type)
        self.Mutate = self._Mutate(session=session, api_type=api_type)
        self.OrphanLookup = self._OrphanLookup(session=session, api_type=api_type)
        self.OwnerAdd = self._OwnerAdd(session=session, api_type=api_type)
        self.OwnerDelete = self._OwnerDelete(session=session, api_type=api_type)
        self.OwnerLookup = self._OwnerLookup(session=session, api_type=api_type)
        self.Retrieve = self._Retrieve(session=session, api_type=api_type)

    class _Add(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Add',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_id(self):
            result = self.response.json()['VaultId']
            self.logger.log('VaultId is %s.' % result)
            return result

        def post(self, base_64_data: str, keyname: str, namespace: str, owner: str, vault_type: int):
            body = json.dumps({
                'Base64Data': base_64_data,
                'Keyname': keyname,
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Associate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Associate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, name: str, vault_id: int, date_value: int = None, int_value: int = None, string_value: str = None):
            body = json.dumps({
                'Name': name,
                'VaultID': vault_id,
                'DateValue': date_value,
                'IntValue': int_value,
                'StringValue': string_value
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Delete(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Delete',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, vault_id: int):
            body = json.dumps({
                'VaultId': vault_id
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Dissociate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Dissociate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, vault_id: int, int_value: int = None, name: str = None, string_value: str = None, date_value: int = None):
            body = json.dumps({
                'VaultID': vault_id,
                'IntValue': int_value,
                'Name': name,
                'StringValue': string_value,
                'DateValue': date_value
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _EncryptionKeysInUse(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/EncryptionKeysInUse',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def encryption_keys(self):
            result = self.response.json()['EncryptionKeys']
            self.logger.log('Encryption Keys retrieved successfully.')
            return result

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def get(self):
            self.response = self._session.get(url=self._url)
            return self

    class _Lookup(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Lookup',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_ids(self):
            result = self.response.json()['VaultIDs']
            self.logger.log('Vault IDs retrieved successfully.')
            return result

        def get(self):
            self.response = self._session.get(url=self._url)
            return self

    class _LookupAllAssocationsbyVaultid(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/LookupAllAssocationsbyVaultid',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def typed_name_values(self):
            result = self.response.json()['TypedNameValues']
            return [SecretStore.TypedNameValues(tnv) for tnv in result]

        def post(self, vault_id: int):
            body = json.dumps({
                'VaultID': vault_id
            })

            self.response = self._session.post(url=-self._url, data=body)
            return self

    class _LookupByAssociation(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/LookupByAssociation',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_ids(self):
            return self.response.json()['VaultIDs']

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

            body = json.dumps(body)
            self.response = self._session.post(url=self._url, data=body)
            return self

    class _LookupAssocationbyVaultID(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/LookupAssocationbyVaultID',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def value(self):
            return self.response.json()['Value']

        def post(self, vault_id: int, name: str = None):
            body = {
                'VaultID': vault_id
            }

            if name:
                body.update({'Name': name})

            self.response = self._session.post(url=-self._url, data=body)
            return self

    class _LookupByOwner(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/LookupByOwner',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_ids(self):
            return self.response.json()['VaultIDs']

        def post(self, namespace: str, owner: str, vault_type: str = None):
            body = {
                'Namespace': namespace,
                'Owner': owner
            }
            if vault_type:
                body.update({'VaultType': vault_type})

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _LookupByVaultType(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/LookupByVaultType',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_ids(self):
            return self.response.json()['VaultIDs']

        def post(self, vault_type: int):
            body = json.dumps({
                'VaultType': vault_type
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Mutate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Mutate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, vault_id: int, vault_type: int):
            body = json.dumps({
                'VaultID': vault_id,
                'VaultType': vault_type
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _OrphanLookup(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/OrphanLookup',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_ids(self):
            return self.response.json()['VaultIDs']

        def post(self, vault_type: int):
            body = json.dumps({
                'VaultType': vault_type
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _OwnerAdd(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/OwnerAdd',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, namespace: str, owner: str, vault_id: int):
            body = json.dumps({
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _OwnerDelete(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/OwnerDelete',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        def post(self, namespace: str, owner: str, vault_id: int = None):
            body = {
                'Namespace': namespace,
                'Owner': owner
            }

            if vault_id:
                body.update({'VaultId': vault_id})

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _OwnerLookup(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/OwnerLookup',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def owners(self):
            return self.response.json()['Owners']

        def post(self, namespace: str, vault_id: int):
            body = json.dumps({
                'Namespace': namespace,
                'VaultID': vault_id
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Retrieve(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/SecretStore/Retrieve',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def base_64_data(self):
            return self.response.json()['Base64Data']

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = SecretStore.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.secret_store_result))
            self.logger.log('Secret Store object created successfully.')
            return result

        @property
        @response_property()
        def vault_type(self):
            return self.response.json()['VaultType']

        def post(self, vault_id: int):
            body = json.dumps({
                'VaultID': vault_id
            })

            self.response = self._session.post(url=self._url, data=body)
            return self
