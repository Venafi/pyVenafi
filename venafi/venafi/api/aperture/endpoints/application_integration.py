from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.identity import Identity
from venafi.properties.response_objects.oauth import OAuth


class _ApplicationIntegration(API):
    def __init__(self, aperture_obj):
        super().__init__(api_obj=aperture_obj, url='/application-integration', valid_return_codes=[201, 204])

    @property
    @json_response_property()
    def application_id(self) -> str:
        return self._from_json()

    def post(self, allowed_identities: List[str], application_id: str, application_name: str, application_scope: dict,
             description: str, vendor: str, mode: str = "create"):
        body = {
            'allowedIdentities': allowed_identities,
            'applicationId': application_id,
            'applicationName': application_name,
            'applicationScope': application_scope,
            'description': description,
            'vendor': vendor,
            'mode': mode
        }

        self.json_response = self._post(data=body)
        return self

    def put(self, allowed_identities: List[str], application_id: str, application_name: str, application_scope: dict,
            description: str, vendor: str, mode: str = "edit"):
        body = {
            'allowedIdentities': allowed_identities,
            'applicationId': application_id,
            'applicationName': application_name,
            'applicationScope': application_scope,
            'description': description,
            'vendor': vendor,
            'mode': mode
        }

        self.json_response = self._put(data=body)
        return self

    def ApplicationId(self, id: str):
        return self._ApplicationId(id=id, aperture_obj=self._api_obj)

    class _ApplicationId(API):
        def __init__(self, id: str, aperture_obj):
            super().__init__(
                api_obj=aperture_obj,
                url=f'/application-integration/{id}',
                valid_return_codes=[200, 204]
            )

        @property
        @json_response_property()
        def allowed_identities(self):
            return [Identity.Identity(id, self._api_type) for id in self._from_json(key='allowedIdentities')]
        
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
        def description(self) -> str:
            return self._from_json(key='description')

        @property
        @json_response_property()
        def vendor(self) -> str:
            return self._from_json(key='vendor')

        def delete(self):
            self.json_response = self._delete()
            return self

        def get(self):
            self.json_response = self._get()
            return self
