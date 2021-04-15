from pytpp.plugins.api.api_base import API, APIResponse, json_response_property
from pytpp.plugins.properties.response_objects.identity import Identity
from pytpp.plugins.properties.response_objects.oauth import OAuth


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

        class _Response(APIResponse):
            def __init__(self, response, api_source):
                super().__init__(response=response, api_source=api_source)

            @property
            @json_response_property()
            def application_id(self) -> str:
                return self._from_json()

        return _Response(response=self._post(data=body), api_source=self._api_source)

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

        class _Response(APIResponse):
            def __init__(self, response, api_source):
                super().__init__(response=response, api_source=api_source)

            @property
            @json_response_property()
            def application_id(self) -> str:
                return self._from_json()

        return _Response(response=self._put(data=body), api_source=self._api_source)

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

                return APIResponse(response=self._put(data=body), api_source=self._api_source)

    class _ApplicationId(API):
        def __init__(self, id: str, api_obj):
            super().__init__(
                api_obj=api_obj,
                url=f'/application-integration/?id={id}'
            )

        def delete(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

            return _Response(response=self._delete(), api_source=self._api_source)

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def access_granted(self) -> int:
                    return self._from_json(key='accessGranted')

                @property
                @json_response_property()
                def access_validity_days(self) -> int:
                    return self._from_json(key='accessValidityDays')

                @property
                @json_response_property()
                def allowed_identities(self):
                    return [Identity.Identity(id, self._api_source) for id in self._from_json(key='allowedIdentities')]

                @property
                @json_response_property()
                def application_id(self) -> str:
                    return self._from_json(key='applicationId')

                @property
                @json_response_property()
                def application_name(self) -> str:
                    return self._from_json(key='applicationName')

                @property
                @json_response_property()
                def application_scope(self):
                    return OAuth.ApplicationScope(self._from_json(key='applicationScope'))

                @property
                @json_response_property()
                def default_access_settings_used(self) -> bool:
                    return self._from_json(key='defaultAccessSettingsUsed')

                @property
                @json_response_property()
                def description(self) -> str:
                    return self._from_json(key='description')

                @property
                @json_response_property()
                def grant_validity_days(self) -> int:
                    return self._from_json(key='grantValidityDays')

                @property
                @json_response_property()
                def renewable(self) -> bool:
                    return self._from_json(key='renewable')

                @property
                @json_response_property()
                def vendor(self) -> str:
                    return self._from_json(key='vendor')

            return _Response(response=self._get(), api_source=self._api_source)
