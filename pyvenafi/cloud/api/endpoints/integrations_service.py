from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import integrations_service
from uuid import UUID


class _environments(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/environments')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, name: str):
        data = {
            'name': name,
        }

        class Output(CloudApiOutputModel):
            EnvironmentResponse: integrations_service.EnvironmentResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'EnvironmentResponse'})

    class _ID(CloudApiEndpoint):
        def get(self):
            class Output(CloudApiOutputModel):
                EnvironmentInformation: integrations_service.EnvironmentInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'EnvironmentInformation'})


class _integrationservices(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/integrationservices')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, edgeInstanceId: UUID, totalCount: bool):
        data = {
            'edgeInstanceId': edgeInstanceId,
            'totalCount': totalCount,
        }

        class Output(CloudApiOutputModel):
            IntegrationServiceDetailsResponse: integrations_service.IntegrationServiceDetailsResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'IntegrationServiceDetailsResponse'})

    def post(self, IntegrationServiceCreationRequest: integrations_service.IntegrationServiceCreationRequest):
        data = {**IntegrationServiceCreationRequest.dict()}

        class Output(CloudApiOutputModel):
            IntegrationServiceInformation: integrations_service.IntegrationServiceInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'IntegrationServiceInformation'})

    class _ID(CloudApiEndpoint):
        def delete(self, retireCertificates: bool):
            data = {
                'retireCertificates': retireCertificates,
            }

            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params=data))

        def get(self):
            class Output(CloudApiOutputModel):
                IntegrationServiceInformation: integrations_service.IntegrationServiceInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'IntegrationServiceInformation'})

        def patch(self, IntegrationServiceUpdateRequest: integrations_service.IntegrationServiceUpdateRequest):
            data = {**IntegrationServiceUpdateRequest.dict()}

            class Output(CloudApiOutputModel):
                IntegrationServiceInformation: integrations_service.IntegrationServiceInformation
            return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'IntegrationServiceInformation'})


class _integrationservicesaggregates(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/integrationservicesaggregates')

    def get(self):
        class Output(CloudApiOutputModel):
            IntegrationsServicesAggregatesResponse: integrations_service.IntegrationsServicesAggregatesResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'IntegrationsServicesAggregatesResponse'})
