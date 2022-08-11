import time
from datetime import datetime
from typing import List, Dict
from pytpp.api.websdk.outputs import credential, identity
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Credentials:
    def __init__(self, api_obj):
        self.Adaptable = self._Adaptable(api_obj=api_obj)
        self.Connector = self._Connector(api_obj=api_obj)
        self.Create = self._Create(api_obj=api_obj)
        self.Delete = self._Delete(api_obj=api_obj)
        self.Enumerate = self._Enumerate(api_obj=api_obj)
        self.Rename = self._Rename(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Update = self._Update(api_obj=api_obj)
        self.CyberArk = self._CyberArk(api_obj=api_obj)

    class _Adaptable:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)
            self.Update = self._Update(api_obj=api_obj)

        class _Create(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/Adaptable/Create')

            def post(self, credential_path: str, credential_type: credential.CredentialType, connector_name: str,
                     custom_fields: List[Dict[str, str]]):
                body = {
                    'CredentialPath': credential_path,
                    'CredentialType': credential_type,
                    'ConnectorName' : connector_name,
                    'CustomFields'  : custom_fields
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output=Output, response=self._post(data=body))

        class _Update(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/Adaptable/Update')

            def post(self, credential_path: str, credential_type: str, connector_name: str,
                     custom_fields: List[Dict[str, str]]):
                body = {
                    'CredentialPath': credential_path,
                    'CredentialType': credential_type,
                    'ConnectorName' : connector_name,
                    'CustomFields'  : custom_fields
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output=Output, response=self._post(data=body))

    class _Connector:
        def __init__(self, api_obj):
            self.Adaptable = self._Adaptable(api_obj=api_obj)

        class _Adaptable(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/Connector/Adaptable')

            def post(self, connector_name: str, powershell_script: str, service_address: str,
                     service_credential: str, allowed_identities: List[str] = None,
                     description: str = None):
                body = {
                    'AllowedIdentities': allowed_identities,
                    'ConnectorName'    : connector_name,
                    'Description'      : description,
                    'PowershellScript' : powershell_script,
                    'ServiceAddress'   : service_address,
                    'ServiceCredential': service_credential
                }

                class Output(WebSdkOutputModel):
                    succcess: bool = ApiField(alias='Succcess')

                return generate_output(output=Output, response=self._post(data=body))

            def Guid(self, guid: str):
                return self._Guid(api_obj=self._api_obj, guid=guid)

            class _Guid(WebSdkEndpoint):
                def __init__(self, api_obj, guid: str):
                    super().__init__(api_obj=api_obj, url=f'/Credentials/Connector/Adaptable/{guid}')

                def delete(self):
                    class Output(WebSdkOutputModel):
                        success: bool = ApiField(alias='Success')

                    return generate_output(output=Output, response=self._delete())

                def get(self):
                    class Output(WebSdkOutputModel):
                        allowed_identities: List[str] = ApiField(default_factory=list, alias='AllowedIdentities')
                        powershell_script: str = ApiField(alias='PowershellScript')
                        service_address: str = ApiField(alias='ServiceAddress')
                        service_credential: str = ApiField(alias='ServiceCredential')
                        success: bool = ApiField(alias='Success')

                    return generate_output(output=Output, response=self._get())

                def put(self, connector_name: str = None, powershell_script: str = None,
                        service_address: str = None, service_credential: str = None,
                        allowed_identities: List[str] = None, description: str = None):
                    body = {
                        'AllowedIdentities': allowed_identities,
                        'ConnectorName'    : connector_name,
                        'Description'      : description,
                        'PowershellScript' : powershell_script,
                        'ServiceAddress'   : service_address,
                        'ServiceCredential': service_credential
                    }

                    class Output(WebSdkOutputModel):
                        succcess: bool = ApiField(alias='Succcess')

                    return generate_output(output=Output, response=self._put(data=body))

    class _Create(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Create')

        def post(self, credential_path: str, friendly_name: str, values: list, password: str = None, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: list = None):
            body = {
                'CredentialPath': credential_path,
                'Password'      : password,
                'FriendlyName'  : friendly_name,
                'Values'        : values,
                'Expiration'    : f'/Date({expiration})/',
                'Description'   : description,
                'EncryptionKey' : encryption_key,
                'Shared'        : shared,
                'Contact'       : contact
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output=Output, response=self._post(data=body))

    class _Delete(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Delete')

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output=Output, response=self._post(data=body))

    class _Enumerate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Enumerate')

        def post(self, credential_path: str, pattern: str = None, recursive: bool = False):
            body = {
                'CredentialPath': credential_path,
                'Recursive'     : recursive,
                'Pattern'       : pattern
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))
                credential_infos: List[credential.CredentialInfo] = ApiField(default_factory=list, alias='CredentialInfos')

            return generate_output(output=Output, response=self._post(data=body))

    class _Rename(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Rename')

        def post(self, credential_path: str, new_credential_path: str):
            body = {
                'CredentialPath': credential_path,
                'NewCredentialPath': new_credential_path
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output=Output, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Retrieve')

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class Output(WebSdkOutputModel):
                classname: str = ApiField(alias='Classname')
                contact: List[identity.Identity] = ApiField(alias='Contact')
                description: str = ApiField(alias='Description')
                expiration: datetime = ApiField(alias='Expiration')
                friendly_name: str = ApiField(alias='FriendlyName')
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))
                values: List[credential.NameTypeValue] = ApiField(default_factory=list, alias='Values')

            return generate_output(output=Output, response=self._post(data=body))

    class _Update(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Update')

        def post(self, credential_path: str, friendly_name: str, values: list, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: list = None):
            body = {
                'CredentialPath': credential_path,
                'FriendlyName'  : friendly_name,
                'Values'        : values,
                'Description'   : description,
                'EncryptionKey' : encryption_key,
                'Shared'        : shared,
                'Contact'       : contact
            }

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            body.update({
                'Expiration': r'/Date(%s)/' % exp_date
            })

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output=Output, response=self._post(data=body))

    class _CyberArk:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)
            self.Update = self._Update(api_obj=api_obj)

        class _Create(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/CyberArk/Create')

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credential_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username'        : username,
                    'AppID'           : app_id,
                    'SafeName'        : safe_name,
                    'FolderName'      : folder_name,
                    'AccountName'     : account_name,
                    'CredentialPath' : credential_path
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output=Output, response=self._post(data=body))

        class _Update(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/CyberArk/Update')

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credential_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username'        : username,
                    'AppID'           : app_id,
                    'SafeName'        : safe_name,
                    'FolderName'      : folder_name,
                    'AccountName'     : account_name,
                    'CredentialPath' : credential_path
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output=Output, response=self._post(data=body))
