from typing import List
from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.models import identity, oauth


class _ApplicationIntegration(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/application-integration')
        self.Access = self._Access(api_obj=api_obj, url=f'{self._url}/access')

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

        class Output(ApertureOutputModel):
            application_id: str = ApiField()

        return generate_output(output_cls=Output, response=self._post(data=body), root_field='application_id')

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

        class Output(ApertureOutputModel):
            application_id: str = ApiField()

        return generate_output(output_cls=Output, response=self._put(data=body), root_field='application_id')

    def ApplicationId(self, id: str):
        return self._ApplicationId(api_obj=self._api_obj, url=f'{self._url}/?id={id}')

    class _Access(ApertureEndpoint):
        def ApplicationId(self, id: str):
            return self._ApplicationId(api_obj=self._api_obj, url=f'{self._url}/?id={id}')

        class _ApplicationId(ApertureEndpoint):
            def put(self, identities: list):
                body = identities
                return generate_output(output_cls=ApertureOutputModel, response=self._put(data=body))

    class _ApplicationId(ApertureEndpoint):
        def delete(self):
            return generate_output(output_cls=ApertureOutputModel, response=self._delete())

        def get(self):
            class Output(ApertureOutputModel):
                access_granted: int = ApiField(alias='accessGranted')
                access_validity_days: int = ApiField(alias='accessValidityDays')
                allowed_identities: List[identity.Identity] = ApiField(default_factory=list, alias='allowedIdentities')
                application_id: str = ApiField(alias='applicationId')
                application_name: str = ApiField(alias='applicationName')
                application_scope: oauth.ApplicationScope = ApiField(alias='applicationScope')
                default_access_settings_used: bool = ApiField(alias='defaultAccessSettingsUsed')
                description: str = ApiField(alias='description')
                grant_validity_days: int = ApiField(alias='grantValidityDays')
                renewable: bool = ApiField(alias='renewable')
                vendor: str = ApiField(alias='vendor')

            return generate_output(output_cls=Output, response=self._get())
