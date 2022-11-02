from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import account_service
from typing import (List, Literal)
from uuid import UUID


class _notifications(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/notifications')
        self.type = self._type(api_obj=self._api_obj, url=f'{self._url}/type')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(CloudApiOutputModel):
            NotificationConfigurationResponse: account_service.NotificationConfigurationResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'NotificationConfigurationResponse'})

    def post(self, NotificationConfigurationRequest: account_service.NotificationConfigurationRequest):
        data = {**NotificationConfigurationRequest.dict()}

        class Output(CloudApiOutputModel):
            NotificationConfigurationInformation: account_service.NotificationConfigurationInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'NotificationConfigurationInformation'})

    class _ID(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.unsubscribe = self._unsubscribe(api_obj=self._api_obj, url=f'{self._url}/unsubscribe')

        def delete(self):
            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def get(self):
            class Output(CloudApiOutputModel):
                NotificationConfigurationInformation: account_service.NotificationConfigurationInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'NotificationConfigurationInformation'})

        def put(self, NotificationConfigurationRequest: account_service.NotificationConfigurationRequest):
            data = {**NotificationConfigurationRequest.dict()}

            class Output(CloudApiOutputModel):
                NotificationConfigurationInformation: account_service.NotificationConfigurationInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'NotificationConfigurationInformation'})

        class _unsubscribe(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def RECIPIENTTOKEN(self, recipienttoken: str):
                return self._RECIPIENTTOKEN(api_obj=self._api_obj, url=f'{self._url}/{recipienttoken}')

            class _RECIPIENTTOKEN(CloudApiEndpoint):
                def put(self):
                    class Output(CloudApiOutputModel):
                        UnsubscribeNotificationInformation: account_service.UnsubscribeNotificationInformation
                    return generate_output(output_cls=Output, response=self._put(data={}), rc_mapping={202: 'UnsubscribeNotificationInformation'})

    class _type(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def TYPE(self, type: str):
            return self._TYPE(api_obj=self._api_obj, url=f'{self._url}/{type}')

        class _TYPE(CloudApiEndpoint):
            def get(self):
                class Output(CloudApiOutputModel):
                    NotificationConfigurationInformation: account_service.NotificationConfigurationInformation
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'NotificationConfigurationInformation'})


class _preferences(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/preferences')
        self.name = self._name(api_obj=self._api_obj, url=f'{self._url}/name')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(CloudApiOutputModel):
            UserPreferencesResponse: account_service.UserPreferencesResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserPreferencesResponse'})

    def post(self, UserPreferenceRequest: account_service.UserPreferenceRequest):
        data = {**UserPreferenceRequest.dict()}

        class Output(CloudApiOutputModel):
            UserPreferenceInformation: account_service.UserPreferenceInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'UserPreferenceInformation'})

    class _ID(CloudApiEndpoint):
        def delete(self):
            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def get(self):
            class Output(CloudApiOutputModel):
                UserPreferenceInformation: account_service.UserPreferenceInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserPreferenceInformation'})

        def put(self, UserPreferenceRequest: account_service.UserPreferenceRequest):
            data = {**UserPreferenceRequest.dict()}

            class Output(CloudApiOutputModel):
                UserPreferenceInformation: account_service.UserPreferenceInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'UserPreferenceInformation'})

    class _name(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def NAME(self, name: str):
            return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

        class _NAME(CloudApiEndpoint):
            def get(self):
                class Output(CloudApiOutputModel):
                    UserPreferenceInformation: account_service.UserPreferenceInformation
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserPreferenceInformation'})


class _ssoconfigurations(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/ssoconfigurations')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(CloudApiOutputModel):
            SsoConfigurationResponse: account_service.SsoConfigurationResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'SsoConfigurationResponse'})

    def post(self, SsoConfigurationRequest: account_service.SsoConfigurationRequest):
        data = {**SsoConfigurationRequest.dict()}

        class Output(CloudApiOutputModel):
            SsoConfigurationInformation: account_service.SsoConfigurationInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'SsoConfigurationInformation'})

    class _ID(CloudApiEndpoint):
        def delete(self):
            class Output(CloudApiOutputModel):
                SsoConfigurationInformation: account_service.SsoConfigurationInformation
            return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'SsoConfigurationInformation'})

        def put(self, SsoConfigurationRequest: account_service.SsoConfigurationRequest):
            data = {**SsoConfigurationRequest.dict()}

            class Output(CloudApiOutputModel):
                SsoConfigurationInformation: account_service.SsoConfigurationInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={201: 'SsoConfigurationInformation'})


class _teams(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/teams')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(CloudApiOutputModel):
            TeamsResponse: account_service.TeamsResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TeamsResponse'})

    def post(self, CreateTeamRequest: account_service.CreateTeamRequest):
        data = {**CreateTeamRequest.dict()}

        class Output(CloudApiOutputModel):
            TeamInformation: account_service.TeamInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'TeamInformation'})

    class _ID(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.members = self._members(api_obj=self._api_obj, url=f'{self._url}/members')
            self.owners = self._owners(api_obj=self._api_obj, url=f'{self._url}/owners')

        def delete(self):
            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def get(self):
            class Output(CloudApiOutputModel):
                TeamInformation: account_service.TeamInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TeamInformation'})

        def patch(self, UpdateTeamRequest: account_service.UpdateTeamRequest):
            data = {**UpdateTeamRequest.dict()}

            class Output(CloudApiOutputModel):
                TeamInformation: account_service.TeamInformation
            return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'TeamInformation'})

        class _members(CloudApiEndpoint):
            def delete(self, TeamMembersRequest: account_service.TeamMembersRequest):
                data = {**TeamMembersRequest.dict()}

                class Output(CloudApiOutputModel):
                    TeamInformation: account_service.TeamInformation
                return generate_output(output_cls=Output, response=self._delete(params=data), rc_mapping={200: 'TeamInformation'})

            def post(self, TeamMembersRequest: account_service.TeamMembersRequest):
                data = {**TeamMembersRequest.dict()}

                class Output(CloudApiOutputModel):
                    TeamInformation: account_service.TeamInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'TeamInformation'})

        class _owners(CloudApiEndpoint):
            def delete(self, TeamOwnersRequest: account_service.TeamOwnersRequest):
                data = {**TeamOwnersRequest.dict()}

                class Output(CloudApiOutputModel):
                    TeamInformation: account_service.TeamInformation
                return generate_output(output_cls=Output, response=self._delete(params=data), rc_mapping={200: 'TeamInformation'})

            def post(self, TeamOwnersRequest: account_service.TeamOwnersRequest):
                data = {**TeamOwnersRequest.dict()}

                class Output(CloudApiOutputModel):
                    TeamInformation: account_service.TeamInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'TeamInformation'})


class _useraccounts(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/useraccounts')
        self.activation = self._activation(api_obj=self._api_obj, url=f'{self._url}/activation')
        self.activationresend = self._activationresend(api_obj=self._api_obj, url=f'{self._url}/activationresend')
        self.apikeyrotation = self._apikeyrotation(api_obj=self._api_obj, url=f'{self._url}/apikeyrotation')
        self.invitations = self._invitations(api_obj=self._api_obj, url=f'{self._url}/invitations')
        self.password = self._password(api_obj=self._api_obj, url=f'{self._url}/password')
        self.passwordreset = self._passwordreset(api_obj=self._api_obj, url=f'{self._url}/passwordreset')
        self.updatepassword = self._updatepassword(api_obj=self._api_obj, url=f'{self._url}/updatepassword')

    def get(self):
        class Output(CloudApiOutputModel):
            UserAccountResponse: account_service.UserAccountResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserAccountResponse'})

    def post(self, UserAccountRequest: account_service.UserAccountRequest):
        data = {**UserAccountRequest.dict()}

        class Output(CloudApiOutputModel):
            UserAccountResponse: account_service.UserAccountResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'UserAccountResponse', 202: 'UserAccountResponse'})

    class _activation(CloudApiEndpoint):
        def get(self, k: UUID, v: bool):
            data = {
                'k': k,
                'v': v,
            }

            class Output(CloudApiOutputModel):
                UserInformation: account_service.UserInformation
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'UserInformation'})

    class _activationresend(CloudApiEndpoint):
        def post(self, ResendActivationRequest: account_service.ResendActivationRequest):
            data = {**ResendActivationRequest.dict()}

            class Output(CloudApiOutputModel):
                ResendActivationResponse: account_service.ResendActivationResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={202: 'ResendActivationResponse'})

    class _apikeyrotation(CloudApiEndpoint):
        def get(self, k: UUID, v: bool):
            data = {
                'k': k,
                'v': v,
            }

            class Output(CloudApiOutputModel):
                ApiKeyInformation: account_service.ApiKeyInformation
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ApiKeyInformation'})

    class _invitations(CloudApiEndpoint):
        def get(self, id: UUID):
            data = {
                'id': id,
            }

            class Output(CloudApiOutputModel):
                UserInformation: account_service.UserInformation
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'UserInformation'})

        def post(self, InvitationRequest: account_service.InvitationRequest):
            data = {**InvitationRequest.dict()}

            class Output(CloudApiOutputModel):
                InvitationResponse: account_service.InvitationResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'InvitationResponse'})

        def put(self, InvitationConfirmationRequest: account_service.InvitationConfirmationRequest):
            data = {**InvitationConfirmationRequest.dict()}

            class Output(CloudApiOutputModel):
                UserInformation: account_service.UserInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={202: 'UserInformation'})

    class _password(CloudApiEndpoint):
        def post(self, ChangePasswordRequest: account_service.ChangePasswordRequest):
            data = {**ChangePasswordRequest.dict()}

            class Output(CloudApiOutputModel):
                UserInformation: account_service.UserInformation
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'UserInformation'})

    class _passwordreset(CloudApiEndpoint):
        def get(self, token: str):
            data = {
                'token': token,
            }

            class Output(CloudApiOutputModel):
                ApiKeyInformation: account_service.ApiKeyInformation
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={201: 'ApiKeyInformation'})

        def post(self, ResetPasswordRequest: account_service.ResetPasswordRequest):
            data = {**ResetPasswordRequest.dict()}

            class Output(CloudApiOutputModel):
                ResetPasswordResponse: account_service.ResetPasswordResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={202: 'ResetPasswordResponse'})

    class _updatepassword(CloudApiEndpoint):
        def post(self, UpdatePasswordRequest: account_service.UpdatePasswordRequest):
            data = {**UpdatePasswordRequest.dict()}

            class Output(CloudApiOutputModel):
                UpdatePasswordResponse: account_service.UpdatePasswordResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'UpdatePasswordResponse'})


class _users(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/users')
        self.username = self._username(api_obj=self._api_obj, url=f'{self._url}/username')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def USERID(self, userid: str):
        return self._USERID(api_obj=self._api_obj, url=f'{self._url}/{userid}')

    def get(self, userStatus: List[Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']], username: str):
        data = {
            'userStatus': userStatus,
            'username': username,
        }

        class Output(CloudApiOutputModel):
            UserResponse: account_service.UserResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'UserResponse'})

    class _ID(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.accounttype = self._accounttype(api_obj=self._api_obj, url=f'{self._url}/accounttype')
            self.locallogin = self._locallogin(api_obj=self._api_obj, url=f'{self._url}/locallogin')
            self.roles = self._roles(api_obj=self._api_obj, url=f'{self._url}/roles')

        def delete(self):
            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def get(self):
            class Output(CloudApiOutputModel):
                UserInformation: account_service.UserInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserInformation'})

        class _accounttype(CloudApiEndpoint):
            def put(self, CUser: account_service.CUser):
                data = {**CUser.dict()}

                class Output(CloudApiOutputModel):
                    UserInformation: account_service.UserInformation
                return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'UserInformation'})

        class _locallogin(CloudApiEndpoint):
            def put(self, CUser: account_service.CUser):
                data = {**CUser.dict()}

                class Output(CloudApiOutputModel):
                    UserInformation: account_service.UserInformation
                return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'UserInformation'})

        class _roles(CloudApiEndpoint):
            def put(self, CUser: account_service.CUser):
                data = {**CUser.dict()}

                class Output(CloudApiOutputModel):
                    UserInformation: account_service.UserInformation
                return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'UserInformation'})

    class _USERID(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.apikeys = self._apikeys(api_obj=self._api_obj, url=f'{self._url}/apikeys')

        class _apikeys(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def KEY(self, key: str):
                return self._KEY(api_obj=self._api_obj, url=f'{self._url}/{key}')

            def get(self, apiKeyStatus: List[Literal['ACTIVE', 'EXPIRED', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_ROTATION', 'ROTATED']]):
                data = {
                    'apiKeyStatus': apiKeyStatus,
                }

                class Output(CloudApiOutputModel):
                    ApiKeyResponse: account_service.ApiKeyResponse
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ApiKeyResponse'})

            def post(self, ApiKeyRequest: account_service.ApiKeyRequest):
                data = {**ApiKeyRequest.dict()}

                class Output(CloudApiOutputModel):
                    ApiKeyResponse: account_service.ApiKeyResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'ApiKeyResponse'})

            class _KEY(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.replacement = self._replacement(api_obj=self._api_obj, url=f'{self._url}/replacement')
                    self.rotation = self._rotation(api_obj=self._api_obj, url=f'{self._url}/rotation')
                    self.rotationrequest = self._rotationrequest(api_obj=self._api_obj, url=f'{self._url}/rotationrequest')

                def get(self):
                    class Output(CloudApiOutputModel):
                        ApiKeyInformation: account_service.ApiKeyInformation
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ApiKeyInformation'})

                class _replacement(CloudApiEndpoint):
                    def post(self, ApiKeyRequest: account_service.ApiKeyRequest):
                        data = {**ApiKeyRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ApiKeyResponse: account_service.ApiKeyResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'ApiKeyResponse'})

                class _rotation(CloudApiEndpoint):
                    def put(self):
                        class Output(CloudApiOutputModel):
                            ApiKeyNullResponse: account_service.ApiKeyNullResponse
                        return generate_output(output_cls=Output, response=self._put(data={}), rc_mapping={200: 'ApiKeyNullResponse'})

                class _rotationrequest(CloudApiEndpoint):
                    def post(self, ApiKeyRequest: account_service.ApiKeyRequest):
                        data = {**ApiKeyRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ApiKeyResponse: account_service.ApiKeyResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'ApiKeyResponse'})

    class _username(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def USERNAME(self, username: str):
            return self._USERNAME(api_obj=self._api_obj, url=f'{self._url}/{username}')

        class _USERNAME(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.loginconfig = self._loginconfig(api_obj=self._api_obj, url=f'{self._url}/loginconfig')

            def get(self):
                class Output(CloudApiOutputModel):
                    UserResponse: account_service.UserResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserResponse'})

            class _loginconfig(CloudApiEndpoint):
                def get(self):
                    class Output(CloudApiOutputModel):
                        UserResponse: account_service.UserResponse
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UserResponse'})


class _dataencryptionkeys(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='dataencryptionkeys')
        self.rotation = self._rotation(api_obj=self._api_obj, url=f'{self._url}/rotation')

    class _rotation(CloudApiEndpoint):
        def post(self):
            class Output(CloudApiOutputModel):
                DataEncryptionKeyInformation: account_service.DataEncryptionKeyInformation
            return generate_output(output_cls=Output, response=self._post(data={}), rc_mapping={200: 'DataEncryptionKeyInformation'})
