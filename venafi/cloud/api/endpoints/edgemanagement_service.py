from __future__ import annotations
from venafi.cloud.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output
from venafi.cloud.api.models import edgemanagement_service
from uuid import UUID


class _pairingcodes(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/pairingcodes')

    def get(self):
        class Output(VaasSdkOutputModel):
            PairingCodeResponse: edgemanagement_service.PairingCodeResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'PairingCodeResponse'})

    def post(self, PairingCodeRequest: edgemanagement_service.PairingCodeRequest):
        data = {**PairingCodeRequest.dict()}

        class Output(VaasSdkOutputModel):
            PairingCodeInformation: edgemanagement_service.PairingCodeInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'PairingCodeInformation'})


class _edgeinstances(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/edgeinstances')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, environmentId: UUID):
        data = {
            'environmentId': environmentId,
        }

        class Output(VaasSdkOutputModel):
            EdgeInstanceResponse: edgemanagement_service.EdgeInstanceResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'EdgeInstanceResponse'})

    class _ID(VaasSdkEndpoint):
        def get(self, statusDetails: bool):
            data = {
                'statusDetails': statusDetails,
            }

            class Output(VaasSdkOutputModel):
                EdgeInstanceInformation: edgemanagement_service.EdgeInstanceInformation
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'EdgeInstanceInformation'})

        def put(self, EdgeInstanceRequest: edgemanagement_service.EdgeInstanceRequest):
            data = {**EdgeInstanceRequest.dict()}

            class Output(VaasSdkOutputModel):
                EdgeInstanceInformation: edgemanagement_service.EdgeInstanceInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'EdgeInstanceInformation'})

        def delete(self):
            class Output(VaasSdkOutputModel):
                EdgeInstanceDeleteResponse: edgemanagement_service.EdgeInstanceDeleteResponse
            return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'EdgeInstanceDeleteResponse'})


class _edgeencryptionkeys(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/edgeencryptionkeys')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, edgeInstanceId: UUID):
        data = {
            'edgeInstanceId': edgeInstanceId,
        }

        class Output(VaasSdkOutputModel):
            EncryptionKeysResponse: edgemanagement_service.EncryptionKeysResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'EncryptionKeysResponse'})

    class _ID(VaasSdkEndpoint):
        def get(self):
            class Output(VaasSdkOutputModel):
                EncryptionKeyInformation: edgemanagement_service.EncryptionKeyInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'EncryptionKeyInformation'})


class _edgeworkers(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/edgeworkers')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, edgeInstanceId: UUID):
        data = {
            'edgeInstanceId': edgeInstanceId,
        }

        class Output(VaasSdkOutputModel):
            EdgeWorkersResponse: edgemanagement_service.EdgeWorkersResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'EdgeWorkersResponse'})

    def post(self, EdgeWorkerRequest: edgemanagement_service.EdgeWorkerRequest):
        data = {**EdgeWorkerRequest.dict()}

        class Output(VaasSdkOutputModel):
            EdgeWorkerInformation: edgemanagement_service.EdgeWorkerInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'EdgeWorkerInformation'})

    class _ID(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.pair = self._pair(api_obj=self._api_obj, url=f'{self._url}/pair')

        def get(self):
            class Output(VaasSdkOutputModel):
                EdgeWorkerInformation: edgemanagement_service.EdgeWorkerInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'EdgeWorkerInformation'})

        def delete(self):
            class Output(VaasSdkOutputModel):
                EdgeWorkerDeleteResponse: edgemanagement_service.EdgeWorkerDeleteResponse
            return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'EdgeWorkerDeleteResponse'})

        class _pair(VaasSdkEndpoint):
            def post(self, EdgeWorkerRequest: edgemanagement_service.EdgeWorkerRequest):
                data = {**EdgeWorkerRequest.dict()}

                class Output(VaasSdkOutputModel):
                    EdgeWorkerInformation: edgemanagement_service.EdgeWorkerInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'EdgeWorkerInformation'})


class _billofmaterials(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/billofmaterials')

    def get(self):
        class Output(VaasSdkOutputModel):
            BillOfMaterialResponse: edgemanagement_service.BillOfMaterialResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'BillOfMaterialResponse'})
