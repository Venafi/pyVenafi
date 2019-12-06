from typing import *
import time
from api.api_base import API, response_property
from objects.response_objects.credential import Credentials


class _Credentials:
    def __init__(self, websdk_obj):
        self.Create = self._Create(websdk_obj=websdk_obj)
        self.Delete = self._Delete(websdk_obj=websdk_obj)
        self.Enumerate = self._Enumerate(websdk_obj=websdk_obj)
        self.Rename = self._Rename(websdk_obj=websdk_obj)
        self.Retrieve = self._Retrieve(websdk_obj=websdk_obj)
        self.Update = self._Update(websdk_obj=websdk_obj)
        self.CyberArk = self._CyberArk(websdk_obj=websdk_obj)

    class _Create(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Create', valid_return_codes=[200])

        @property
        @response_property()
        def result(self):
            return Credentials.Result(self.json_response(key='Result'))

        def post(self, credential_path: str, friendly_name: str, values: List[Dict], password: str = None, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: List[str] = None):
            body = {
                'CredentialPath': credential_path,
                'Password': password,
                'FriendlyName': friendly_name,
                'Values': values,
                'Expiration': f'/Date({expiration})/'
            }
            if description:
                body.update({'Description': description})

            if encryption_key:
                body.update({'EncryptionKey': encryption_key})

            if shared:
                body.update({'Shared': shared})

            if contact:
                body.update({'Contact': contact})

            self.response = self._post(data=body)

            return self

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Delete', valid_return_codes=[200])

        @property
        @response_property()
        def result(self):
            return Credentials.Result(self.json_response(key='Result'))

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            self.response = self._post(data=body)
            return self

    class _Enumerate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Enumerate', valid_return_codes=[200])

        @property
        @response_property()
        def result(self):
            return Credentials.Result(self.json_response(key='Result'))

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
            self.response = self._post(data=body)
            return self

    class _Rename(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Rename', valid_return_codes=[200])

        @property
        @response_property()
        def result(self):
            return Credentials.Result(self.json_response(key='Result'))

        def post(self, credential_path: str, new_credential_path: str):
            body = {
                'CredentialPath': credential_path,
                'NewCredentialPath': new_credential_path
            }

            self.response = self._post(data=body)
            return self

    class _Retrieve(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Retrieve', valid_return_codes=[200])

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
            return Credentials.Result(self.json_response(key='Result'))
        
        @property
        @response_property()
        def values(self):
            result = self.json_response(key='Values')
            return [Credentials.NameTypeValue(ntv) for ntv in result]
        
        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }
            
            self.response = self._post(data=body)
            return self

    class _Update(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Credentials/Update', valid_return_codes=[200])

        @property
        @response_property()
        def result(self):
            return Credentials.Result(self.json_response(key='Result'))

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
            self.response = self._post(data=body)

            return self

    class _CyberArk:
        def __init__(self, websdk_obj):
            self.Create = self._Create(websdk_obj=websdk_obj)
            self.Update = self._Update(websdk_obj=websdk_obj)

        class _Create(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Credentials/CyberArk/Create', valid_return_codes=[200])

            @property
            @response_property()
            def result(self):
                return Credentials.Result(self.json_response(key='Result'))

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

                self.response = self._post(data=body)
                return self

        class _Update(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Credentials/CyberArk/Update', valid_return_codes=[200])

            @property
            @response_property()
            def result(self):
                return Credentials.Result(self.json_response(key='Result'))

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

                self.response = self._post(data=body)
                return self
