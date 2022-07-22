import logging
import warnings
from datetime import datetime
from pydantic import Field
from pytpp.tools.logger import api_logger
from pytpp.api.api_base import API, APIResponse, ResponseFactory


class _Authorize(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Authorize')

        self.Certificate = self._Certificate(api_obj=api_obj)
        self.Device = self._Device(api_obj=api_obj)
        self.Integrated = self._Integrated(api_obj=api_obj)
        self.OAuth = self._OAuth(api_obj=api_obj)
        self.Token = self._Token(api_obj=api_obj)
        self.Verify = self._Verify(api_obj=api_obj)

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        warnings.warn('Authorizing to TPP with only a username and password is being deprecated. '
                      'Refer to product documentation on using OAuth authentication.')
        body = {
            "Username": username,
            "Password": password
        }

        class _Response(APIResponse):
            token = Field(default=None, alias='APIKey')

        api_logger.debug(f'Authenticating to TPP as "{username}"...')
        with api_logger.suppressed(logging.WARNING):
            response = self._post(data=body)
        api_logger.debug(f'Authenticated as "{username}"!')
        return ResponseFactory(response=response, response_cls=_Response)

    class _Certificate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Certificate')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope': scope
            }

            class _Response(APIResponse):
                access_token = Field(default=None, alias='access_token')
                expires = Field(default=None, alias='expires')
                expires_in = Field(default=None, alias='expires_in')
                identity = Field(default=None, alias='identity')
                refresh_token = Field(default=None, alias='refresh_token')
                refresh_until = Field(default=None, alias='refresh_until')
                scope = Field(default=None, alias='scope')
                token_type = Field(default=None, alias='token_type')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return ResponseFactory(response=response, response_cls=_Response)

    class _Device(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Device')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope'    : scope
            }

            class _Response(APIResponse):
                device_code = Field(default=None, alias='device_code')
                interval = Field(default=None, alias='interval')
                user_code = Field(default=None, alias='user_code')
                verification_uri = Field(default=None, alias='verification_uri')
                verification_url_complete = Field(default=None, alias='verification_uri_complete')
                expires_in = Field(default=None, alias='expires_in')
                expires = Field(default=None, alias='expires')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return ResponseFactory(response=response, response_cls=_Response)

    class _Integrated(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Integrated')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str, state: str = None):
            body = {
                'client_id': client_id,
                'scope'    : scope,
                'state'    : state
            }

            class _Response(APIResponse):
                access_token: str = Field(alias='access_token', default=None)
                expires: datetime = Field(default=None, alias='expires')
                expires_in = Field(default=None, alias='expires_in')
                identity = Field(default=None, alias='identity')
                refresh_token = Field(default=None, alias='refresh_token')
                refresh_until = Field(default=None, alias='refresh_until')
                scope = Field(default=None, alias='scope')
                token_type = Field(default=None, alias='token_type')

            return ResponseFactory(response=self._post(data=body), response_cls=_Response)

    class _OAuth(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Authorize/OAuth')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password': password,
                'scope': scope,
                'username': username,
                'state': state
            }

            class _Response(APIResponse):
                access_token: str = Field(alias='access_token', default=None)
                expires: str = Field(alias='expires', default=None)
                identity: str = Field(alias='identity', default=None)
                refresh_token: str = Field(alias='refresh_token', default=None)
                scope: str = Field(alias='scope', default=None)
                token_type: str = Field(alias='token_type', default=None)

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated as {username}!')
            return ResponseFactory(response=response, response_cls=_Response)

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Authorize/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, refresh_token: str, grant_type: str = None, device_code: str = None):
            body = {
                'client_id': client_id,
                'refresh_token': refresh_token,
                'grant_type': grant_type,
                'device_code': device_code
            }

            class _Response(APIResponse):
                access_token = Field(default=None, alias='access_token')
                expires = Field(default=None, alias='expires')
                refresh_token = Field(default=None, alias='refresh_token')
                refresh_until = Field(default=None, alias='refresh_until')
                scope = Field(default=None, alias='scope')
                token_type = Field(default=None, alias='token_type')

            api_logger.debug(f'Authenticating to TPP OAuth application with a refresh token...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return ResponseFactory(response=response, response_cls=_Response)

    class _Verify(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Verify')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            class _Response(APIResponse):
                access_issued_on_unix_time = Field(default=None, alias='access_issued_on_unix_time')
                application = Field(default=None, alias='application')
                expires_unix_time = Field(default=None, alias='expires_unix_time')
                grant_issued_on_unix_time = Field(default=None, alias='grant_issued_on_unix_time')
                identity = Field(default=None, alias='identity')
                scope = Field(default=None, alias='scope')
                valid_for = Field(default=None, alias='valid_for')
        
                @property
                def access_issued_on(self):
                    return self.access_issued_on_unix_time
                
                @property
                def access_issued_on_ISO8601(self):
                    return self.access_issued_on_unix_time
            
                @property
                def expires(self): 
                    return self.expires_unix_time
        
                @property
                def expires_ISO8601(self):
                    return self.expires_unix_time
        
                @property
                def grant_issued_on(self):
                    return self.grant_issued_on_unix_time
                
                @property
                def grant_issued_on_ISO8601(self):
                    return self.grant_issued_on_unix_time

            return ResponseFactory(response=self._get(), response_cls=_Response)
