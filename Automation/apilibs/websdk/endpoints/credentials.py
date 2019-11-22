from typing import *
import time
from apilibs.base import API, response_property, InvalidResultCode
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
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
            return result

        def post(self, credential_path: str, friendly_name: str, values: List[Dict], password: str = None, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: List[str] = None):
            body = {
                'CredentialPath': credential_path,
                'Password': password,
                'FriendlyName': friendly_name,
                'Values': values
            }
            if description:
                body.update({'Description': description})

            if encryption_key:
                body.update({'EncryptionKey': encryption_key})

            if shared:
                body.update({'Shared': shared})

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            body.update({'Expiration': r'/Date(%s)/' % exp_date})
            if contact:
                body.update({'Contact': contact})

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
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
            return result

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

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
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
            return result

        @property
        @response_property()
        def credential_infos(self):
            result = self.json_response(key='CredentialInfos')
            return [Credentials.CredentialInfo(cred_info) for cred_info in result]

        def post(self, credential_path: str, pattern: str = None, recursive: bool = False):
            body = {
                'CredentialPath': credential_path,
                'Recursive': recursive
            }

            if pattern:
                body.update({'Pattern': pattern})

            body = body
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
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
            return result

        def post(self, credential_path: str, new_credential_path: str):
            body = {
                'CredentialPath': credential_path,
                'NewCredentialPath': new_credential_path
            }

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
            return self.json_response(key='Classname')

        @property
        @response_property()
        def description(self):
            return self.json_response(key='Description')

        @property
        @response_property()
        def expiration(self):
            return self.json_response(key='Expiration')

        @property
        @response_property()
        def friendly_name(self):
            return self.json_response(key='FriendlyName')
        
        @property
        @response_property()
        def result(self):
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
            return result
        
        @property
        @response_property()
        def values(self):
            result = self.json_response(key='Values')
            return [Credentials.NameTypeValue(ntv) for ntv in result]
        
        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }
            
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
            result = Credentials.Result(self.json_response(key='Result'))
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
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

            body = payload
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
                result = Credentials.Result(self.json_response(key='Result'))
                if result.code != 1:
                    raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
                return result

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credentials_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username': username,
                    'AppID': app_id,
                    'SafeName': safe_name,
                    'FolderName': folder_name,
                    'AccountName': account_name,
                    'CredentialsPath': credentials_path
                }

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
                result = Credentials.Result(self.json_response(key='Result'))
                if result.code != 1:
                    raise InvalidResultCode(url=self._url, code=result.code, code_description=result.credential_result)
                return result

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credentials_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username': username,
                    'AppID': app_id,
                    'SafeName': safe_name,
                    'FolderName': folder_name,
                    'AccountName': account_name,
                    'CredentialsPath': credentials_path
                }

                self.response = self._session.post(url=self._url, data=body)
                return self
