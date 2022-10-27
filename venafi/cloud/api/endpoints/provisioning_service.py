from __future__ import annotations
from venafi.cloud.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output
from venafi.cloud.api.models import provisioning_service


class _machineidentitysearch(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/machineidentitysearch')

    def post(self, MachineIdentitySearchRequest: provisioning_service.MachineIdentitySearchRequest):
        data = {**MachineIdentitySearchRequest.dict()}

        class Output(VaasSdkOutputModel):
            MachineIdentityDocumentResponse: provisioning_service.MachineIdentityDocumentResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'MachineIdentityDocumentResponse'})


class _machineidentities(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/machineidentities')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(VaasSdkOutputModel):
            MachineIdentityResponse: provisioning_service.MachineIdentityResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'MachineIdentityResponse'})

    def post(self, MachineIdentityCreationRequest: provisioning_service.MachineIdentityCreationRequest):
        data = {**MachineIdentityCreationRequest.dict()}

        class Output(VaasSdkOutputModel):
            MachineIdentityInformation: provisioning_service.MachineIdentityInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'MachineIdentityInformation'})

    class _ID(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.workflows = self._workflows(api_obj=self._api_obj, url=f'{self._url}/workflows')

        def get(self):
            class Output(VaasSdkOutputModel):
                MachineIdentityInformation: provisioning_service.MachineIdentityInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'MachineIdentityInformation'})

        def delete(self):
            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def patch(self, MachineIdentityUpdateRequest: provisioning_service.MachineIdentityUpdateRequest):
            data = {**MachineIdentityUpdateRequest.dict()}

            class Output(VaasSdkOutputModel):
                MachineIdentityInformation: provisioning_service.MachineIdentityInformation
            return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'MachineIdentityInformation'})

        class _workflows(VaasSdkEndpoint):
            def post(self, MachineIdentityWorkflowRequest: provisioning_service.MachineIdentityWorkflowRequest):
                data = {**MachineIdentityWorkflowRequest.dict()}

                class Output(VaasSdkOutputModel):
                    MachineIdentityWorkflowInformation: provisioning_service.MachineIdentityWorkflowInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'MachineIdentityWorkflowInformation'})


class _machinetypes(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/machinetypes')

    def get(self):
        class Output(VaasSdkOutputModel):
            MachineTypeResponse: provisioning_service.MachineTypeResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'MachineTypeResponse'})


class _machines(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/machines')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self):
        class Output(VaasSdkOutputModel):
            MachinesResponse: provisioning_service.MachinesResponse
        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'MachinesResponse'})

    def post(self, MachineCreationRequest: provisioning_service.MachineCreationRequest):
        data = {**MachineCreationRequest.dict()}

        class Output(VaasSdkOutputModel):
            MachineInformation: provisioning_service.MachineInformation
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'MachineInformation'})

    class _ID(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.workflows = self._workflows(api_obj=self._api_obj, url=f'{self._url}/workflows')

        def get(self):
            class Output(VaasSdkOutputModel):
                MachineInformation: provisioning_service.MachineInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'MachineInformation'})

        def delete(self):
            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._delete(params={}))

        def patch(self, MachineUpdateRequest: provisioning_service.MachineUpdateRequest):
            data = {**MachineUpdateRequest.dict()}

            class Output(VaasSdkOutputModel):
                MachineInformation: provisioning_service.MachineInformation
            return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'MachineInformation'})

        class _workflows(VaasSdkEndpoint):
            def post(self, MachineWorkflowRequest: provisioning_service.MachineWorkflowRequest):
                data = {**MachineWorkflowRequest.dict()}

                class Output(VaasSdkOutputModel):
                    MachineInformation: provisioning_service.MachineInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'MachineInformation'})


class _machinesearch(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/machinesearch')

    def post(self, ownershipTree: bool):
        data = {
            'ownershipTree': ownershipTree,
        }

        class Output(VaasSdkOutputModel):
            MachineDocumentResponse: provisioning_service.MachineDocumentResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'MachineDocumentResponse'})
