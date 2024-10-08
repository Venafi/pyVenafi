from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    CloudApiEndpoint,
    CloudApiOutputModel,
    generate_output,
)
from pyvenafi.cloud.api.models import provisioning_service

class _provisioning_service:
    def __init__(self, api_obj):
        self.v1 = self._v1(api_obj=api_obj)

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.machineidentities = self._machineidentities(
                api_obj=self._api_obj,
                url=f'{self._url}/machineidentities'
            )
            self.machineidentitysearch = self._machineidentitysearch(
                api_obj=self._api_obj,
                url=f'{self._url}/machineidentitysearch'
            )
            self.machines = self._machines(api_obj=self._api_obj, url=f'{self._url}/machines')
            self.machinesearch = self._machinesearch(api_obj=self._api_obj, url=f'{self._url}/machinesearch')
            self.machinetypes = self._machinetypes(api_obj=self._api_obj, url=f'{self._url}/machinetypes')

        class _machineidentities(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def get(self):
                class Output(CloudApiOutputModel):
                    MachineIdentityResponse: provisioning_service.MachineIdentityResponse

                return generate_output(
                    output_cls=Output,
                    response=self._get(params={}),
                    rc_mapping={
                        200: 'MachineIdentityResponse'
                    }
                )

            def post(self, MachineIdentityCreationRequest: provisioning_service.MachineIdentityCreationRequest):
                data = {**MachineIdentityCreationRequest.dict()}

                class Output(CloudApiOutputModel):
                    MachineIdentityInformation: provisioning_service.MachineIdentityInformation

                return generate_output(
                    output_cls=Output,
                    response=self._post(data=data),
                    rc_mapping={
                        201: 'MachineIdentityInformation'
                    }
                )

            class _ID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.workflows = self._workflows(api_obj=self._api_obj, url=f'{self._url}/workflows')

                def delete(self):
                    class Output(CloudApiOutputModel):
                        pass

                    return generate_output(output_cls=Output, response=self._delete(params={}))

                def get(self):
                    class Output(CloudApiOutputModel):
                        MachineIdentityInformation: provisioning_service.MachineIdentityInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'MachineIdentityInformation'
                        }
                    )

                def patch(self, MachineIdentityUpdateRequest: provisioning_service.MachineIdentityUpdateRequest):
                    data = {**MachineIdentityUpdateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        MachineIdentityInformation: provisioning_service.MachineIdentityInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._patch(data=data),
                        rc_mapping={
                            200: 'MachineIdentityInformation'
                        }
                    )

                class _workflows(CloudApiEndpoint):
                    def post(self, MachineIdentityWorkflowRequest: provisioning_service.MachineIdentityWorkflowRequest):
                        data = {**MachineIdentityWorkflowRequest.dict()}

                        class Output(CloudApiOutputModel):
                            MachineIdentityWorkflowInformation: provisioning_service.MachineIdentityWorkflowInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                201: 'MachineIdentityWorkflowInformation'
                            }
                        )

        class _machineidentitysearch(CloudApiEndpoint):
            def post(self, MachineIdentitySearchRequest: provisioning_service.MachineIdentitySearchRequest):
                data = {**MachineIdentitySearchRequest.dict()}

                class Output(CloudApiOutputModel):
                    MachineIdentityDocumentResponse: provisioning_service.MachineIdentityDocumentResponse

                return generate_output(
                    output_cls=Output,
                    response=self._post(data=data),
                    rc_mapping={
                        200: 'MachineIdentityDocumentResponse'
                    }
                )

        class _machines(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def get(self):
                class Output(CloudApiOutputModel):
                    MachinesResponse: provisioning_service.MachinesResponse

                return generate_output(
                    output_cls=Output,
                    response=self._get(params={}),
                    rc_mapping={
                        200: 'MachinesResponse'
                    }
                )

            def post(self, MachineCreationRequest: provisioning_service.MachineCreationRequest):
                data = {**MachineCreationRequest.dict()}

                class Output(CloudApiOutputModel):
                    MachineInformation: provisioning_service.MachineInformation

                return generate_output(
                    output_cls=Output,
                    response=self._post(data=data),
                    rc_mapping={
                        201: 'MachineInformation'
                    }
                )

            class _ID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.batchprovisionings = self._batchprovisionings(
                        api_obj=self._api_obj,
                        url=f'{self._url}/batchprovisionings'
                    )
                    self.discovery = self._discovery(api_obj=self._api_obj, url=f'{self._url}/discovery')
                    self.workflows = self._workflows(api_obj=self._api_obj, url=f'{self._url}/workflows')

                def delete(self):
                    class Output(CloudApiOutputModel):
                        pass

                    return generate_output(output_cls=Output, response=self._delete(params={}))

                def get(self):
                    class Output(CloudApiOutputModel):
                        MachineInformation: provisioning_service.MachineInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'MachineInformation'
                        }
                    )

                def patch(self, MachineUpdateRequest: provisioning_service.MachineUpdateRequest):
                    data = {**MachineUpdateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        MachineInformation: provisioning_service.MachineInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._patch(data=data),
                        rc_mapping={
                            200: 'MachineInformation'
                        }
                    )

                class _batchprovisionings(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.abort = self._abort(api_obj=self._api_obj, url=f'{self._url}/abort')

                    class _abort(CloudApiEndpoint):
                        def post(self):
                            class Output(CloudApiOutputModel):
                                pass

                            return generate_output(output_cls=Output, response=self._post(data={}))

                class _discovery(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.abort = self._abort(api_obj=self._api_obj, url=f'{self._url}/abort')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            MachineDiscoveryResultInformation: provisioning_service.MachineDiscoveryResultInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'MachineDiscoveryResultInformation'
                            }
                        )

                    class _abort(CloudApiEndpoint):
                        def post(self):
                            class Output(CloudApiOutputModel):
                                MachineInformation: provisioning_service.MachineInformation

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data={}),
                                rc_mapping={
                                    202: 'MachineInformation'
                                }
                            )

                class _workflows(CloudApiEndpoint):
                    def post(self, MachineWorkflowRequest: provisioning_service.MachineWorkflowRequest):
                        data = {**MachineWorkflowRequest.dict()}

                        class Output(CloudApiOutputModel):
                            MachineInformation: provisioning_service.MachineInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                201: 'MachineInformation'
                            }
                        )

        class _machinesearch(CloudApiEndpoint):
            def post(self, ownershipTree: bool):
                data = {
                    'ownershipTree': ownershipTree,
                }

                class Output(CloudApiOutputModel):
                    MachineDocumentResponse: provisioning_service.MachineDocumentResponse

                return generate_output(
                    output_cls=Output,
                    response=self._post(data=data),
                    rc_mapping={
                        200: 'MachineDocumentResponse'
                    }
                )

        class _machinetypes(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def get(self):
                class Output(CloudApiOutputModel):
                    MachineTypeResponse: provisioning_service.MachineTypeResponse

                return generate_output(
                    output_cls=Output,
                    response=self._get(params={}),
                    rc_mapping={
                        200: 'MachineTypeResponse'
                    }
                )

            class _ID(CloudApiEndpoint):
                def get(self):
                    class Output(CloudApiOutputModel):
                        MachineTypeInformation: provisioning_service.MachineTypeInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'MachineTypeInformation'
                        }
                    )
