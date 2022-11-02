from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import connectors_service


class _connectors(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/connectors')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(CloudApiOutputModel):
            ConnectorsResponse: connectors_service.ConnectorsResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ConnectorsResponse'})

    def post(self, ConnectorsCreationRequest: connectors_service.ConnectorsCreationRequest):
        data = {**ConnectorsCreationRequest.dict()}

        class Output(CloudApiOutputModel):
            ConnectorsInformation: connectors_service.ConnectorsInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'ConnectorsInformation'})

    class _ID(CloudApiEndpoint):
        def delete(self):
            class Output(CloudApiOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def get(self):
            class Output(CloudApiOutputModel):
                ConnectorsInformation: connectors_service.ConnectorsInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ConnectorsInformation'})

        def put(self, ConnectorsUpdateRequest: connectors_service.ConnectorsUpdateRequest):
            data = {**ConnectorsUpdateRequest.dict()}

            class Output(CloudApiOutputModel):
                ConnectorsInformation: connectors_service.ConnectorsInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'ConnectorsInformation'})
