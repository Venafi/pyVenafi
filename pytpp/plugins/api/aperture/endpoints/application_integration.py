from typing import List
from api.api_base import ResponseFactory, ResponseField
from properties.response_objects.dataclasses import identity
from plugins.properties.response_objects.dataclasses import oauth
from pytpp.plugins.api.api_base import API, APIResponse, ApiApp


class _ApplicationIntegration(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/application-integration')
        self.Access = self._Access(api_obj=api_obj)

    def post(self, application_id: str, application_name: str, application_scope: dict,
             description: str, vendor: str, access_validity_days: int = None, grant_validity_days: int = None):
        use_defaults = grant_validity_days is None
        renewable = None if use_defaults else bool(access_validity_days is not None)
        body = {
            'accessValidityDays'       : access_validity_days if not use_defaults else None,
            'applicationId'            : application_id,
            'applicationName'          : application_name,
            'applicationScope'         : application_scope,
            'defaultAccessSettingsUsed': use_defaults,
            'description'              : description,
            'grantValidityDays'        : grant_validity_days,
            'mode'                     : 'create',
            'renewable'                : renewable,
            'vendor'                   : vendor
        }

        class Response(APIResponse):
            __api_app__ = ApiApp.aperture
            application_id: str = ResponseField()

        return ResponseFactory(response_cls=Response, response=self._post(data=body), root_field='application_id')

    def put(self, application_id: str, application_name: str, application_scope: dict,
            description: str, vendor: str, access_validity_days: int = None, grant_validity_days: int = None):
        use_defaults = grant_validity_days is None
        renewable = None if use_defaults else bool(access_validity_days is not None)
        body = {
            'accessValidityDays'       : access_validity_days if not use_defaults else None,
            'applicationId'            : application_id,
            'applicationName'          : application_name,
            'applicationScope'         : application_scope,
            'defaultAccessSettingsUsed': use_defaults,
            'description'              : description,
            'grantValidityDays'        : grant_validity_days,
            'mode'                     : 'edit',
            'renewable'                : renewable,
            'vendor'                   : vendor
        }

        class Response(APIResponse):
            __api_app__ = ApiApp.aperture
            application_id: str = ResponseField()

        return ResponseFactory(response_cls=Response, response=self._put(data=body), root_field='application_id')

    def ApplicationId(self, id: str):
        return self._ApplicationId(id=id, api_obj=self._api_obj)

    class _Access:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def ApplicationId(self, id: str):
            return self._ApplicationId(id=id, api_obj=self._api_obj)

        class _ApplicationId(API):
            def __init__(self, id: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/application-integration/access/?id={id}')

            def put(self, identities: list):
                body = identities
                
                class Response(APIResponse):
                    __api_app__ = ApiApp.aperture

                return ResponseFactory(response_cls=Response, response=self._put(data=body))

    class _ApplicationId(API):
        def __init__(self, id: str, api_obj):
            super().__init__(
                api_obj=api_obj,
                url=f'/application-integration/?id={id}'
            )

        def delete(self):
            class Response(APIResponse):
                __api_app__ = ApiApp.aperture
                
            return ResponseFactory(response_cls=Response, response=self._delete())

        def get(self):
            class Response(APIResponse):
                access_granted: int = ResponseField(alias='accessGranted')
                access_validity_days: int = ResponseField(alias='accessValidityDays')
                allowed_identities : List[identity.Identity] = ResponseField(default_factory=list, alias='allowedIdentities')
                application_id: str = ResponseField(alias='applicationId')
                application_name: str = ResponseField(alias='applicationName')
                application_scope: oauth.ApplicationScope = ResponseField(alias='applicationScope')
                default_access_settings_used: bool = ResponseField(alias='defaultAccessSettingsUsed')
                description: str = ResponseField(alias='description')
                grant_validity_days: int = ResponseField(alias='grantValidityDays')
                renewable: bool = ResponseField(alias='renewable')
                vendor: str = ResponseField(alias='vendor')

            return ResponseFactory(response_cls=Response, response=self._get())
