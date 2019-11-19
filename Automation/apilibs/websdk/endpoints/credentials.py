import json
from typing import *
import time, datetime
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from objects.response_objects.credential import Credentials


class _Credentials:
    def __init__(self, session, api_type):
        self.Create = self._Create(session=session, api_type=api_type)
        self.Delete = self._Delete(session=session, api_type=api_type)
        self.Enumerate = self._Enumerate(session=session, api_type=api_type)
        self.Rename = self._Rename(session=session, api_type=api_type)
        self.Retrieve = self._Retrieve(session=session, api_type=api_type)
        self.Update = self._Update(session=session, api_type=api_type)
        self.CyberArk = self._CyberArk(session=session, api_type=api_type)

    class _Create(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Create',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        def post(self, credential_path: str, friendly_name: str, values: List[Dict], password: str = None, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: List[str] = None):
            payload = {
                'CredentialPath': credential_path,
                'Password': password,
                'FriendlyName': friendly_name,
                'Values': values
            }
            if description:
                payload.update({'Description': description})

            if encryption_key:
                payload.update({'EncryptionKey': encryption_key})

            if shared:
                payload.update({'Shared': shared})

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            payload.update({'Expiration': r'/Date(%s)/' % exp_date})
            if contact:
                payload.update({'Contact': contact})

            body = json.dumps(payload)
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Delete(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Delete',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        def post(self, credential_path: str):
            body = json.dumps({
                'CredentialPath': credential_path
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Enumerate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Enumerate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        @property
        @response_property()
        def credential_infos(self):
            result = self.response.json()['CredentialInfos']
            self.logger.log('CredentialInfos object created successfully.')
            return [Credentials.CredentialInfo(cred_info) for cred_info in result]

        def post(self, credential_path: str, pattern: str = None, recursive: bool = False):
            body = {
                'CredentialPath': credential_path,
                'Recursive': recursive
            }

            if pattern:
                body.update({'Pattern': pattern})

            body = json.dumps(body)
            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Rename(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Rename',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        def post(self, credential_path: str, new_credential_path: str):
            body = json.dumps({
                'CredentialPath': credential_path,
                'NewCredentialPath': new_credential_path
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Retrieve(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Retrieve',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def classname(self):
            return self.response.json()['Classname']

        @property
        @response_property()
        def description(self):
            return self.response.json()['Description']

        @property
        @response_property()
        def expiration(self):
            return self.response.json()['Expiration']

        @property
        @response_property()
        def friendly_name(self):
            return self.response.json()['FriendlyName']
        
        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result
        
        @property
        @response_property()
        def values(self):
            result = self.response.json()['Values']
            v = [Credentials.NameTypeValue(ntv) for ntv in result]
            self.logger.log('Values object created successfully.')
            return v
        
        def post(self, credential_path: str):
            body = json.dumps({
                'CredentialPath': credential_path
            })
            
            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Update(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Update',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json()['Result']
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        def post(self, credential_path: str, friendly_name: str, values: List[Dict], description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: List[str] = None):
            payload = {
                'CredentialPath': credential_path,
                'FriendlyName': friendly_name,
                'Values': values
            }
            if description:
                payload.update({'Description': description})

            if encryption_key:
                payload.update({'EncryptionKey': encryption_key})

            if shared:
                payload.update({'Shared': shared})

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            payload.update({'Expiration': r'/Date(%s)/' % exp_date})
            if contact:
                payload.update({'Contact': contact})

            body = json.dumps(payload)
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _CyberArk:
        def __init__(self, session, api_type):
            self.Create = self._Create(session=session, api_type=api_type)
            self.Update = self._Update(session=session, api_type=api_type)

        class _Create(API):
            def __init__(self, session, api_type):
                super().__init__(
                    session=session,
                    api_type=api_type,
                    url=WEBSDK_URL + '/Credentials/CyberArk/Create',
                    valid_return_codes=[200]
                )

            @property
            @response_property()
            def result(self):
                result = self.response.json()['Result']
                result = Credentials.Result(result)
                if result.code != 1:
                    raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
                self.logger.log('Credential object created successfully.')
                return result

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credentials_path: str):
                body = json.dumps({
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username': username,
                    'AppID': app_id,
                    'SafeName': safe_name,
                    'FolderName': folder_name,
                    'AccountName': account_name,
                    'CredentialsPath': credentials_path
                })

                self.response = self._session.post(url=self._url, data=body)
                return self

        class _Update(API):
            def __init__(self, session, api_type):
                super().__init__(
                    session=session,
                    api_type=api_type,
                    url=WEBSDK_URL + '/Credentials/CyberArk/Update',
                    valid_return_codes=[200]
                )

                @property
                @response_property()
                def result(self):
                    result = self.response.json()['Result']
                    result = Credentials.Result(result)
                    if result.code != 1:
                        raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
                    self.logger.log('Credential object created successfully.')
                    return result

                def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                         folder_name: str, account_name: str, credentials_path: str):
                    body = json.dumps({
                        'CyberArkUsername': cyber_ark_username,
                        'CyberArkPassword': cyber_ark_password,
                        'Username': username,
                        'AppID': app_id,
                        'SafeName': safe_name,
                        'FolderName': folder_name,
                        'AccountName': account_name,
                        'CredentialsPath': credentials_path
                    })

                    self.response = self._session.post(url=self._url, data=body)
                    return self
