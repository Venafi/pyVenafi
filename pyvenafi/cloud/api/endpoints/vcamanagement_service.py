from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    CloudApiEndpoint,
    CloudApiOutputModel,
    generate_output,
)
from pyvenafi.cloud.api.models import vcamanagement_service

class _vcamanagement_service:
    def __init__(self, api_obj):
        self.v1 = self._v1(api_obj=api_obj)

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.distributedissuers = self._distributedissuers(
                api_obj=self._api_obj,
                url=f'{self._url}/distributedissuers'
            )

        class _distributedissuers(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.configurations = self._configurations(api_obj=self._api_obj, url=f'{self._url}/configurations')
                self.intermediatecertificates = self._intermediatecertificates(
                    api_obj=self._api_obj, url=f'{self._url}/intermediatecertificates'
                )
                self.policies = self._policies(api_obj=self._api_obj, url=f'{self._url}/policies')
                self.subcaproviders = self._subcaproviders(api_obj=self._api_obj, url=f'{self._url}/subcaproviders')

            class _configurations(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.regions = self._regions(api_obj=self._api_obj, url=f'{self._url}/regions')

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        ConfigurationResponse: vcamanagement_service.ConfigurationResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'ConfigurationResponse'
                        }
                    )

                def post(self, ConfigurationCreateRequest: vcamanagement_service.ConfigurationCreateRequest):
                    data = {**ConfigurationCreateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        ExtendedConfigurationInformation: vcamanagement_service.ExtendedConfigurationInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'ExtendedConfigurationInformation'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def delete(self):
                        class Output(CloudApiOutputModel):
                            ConfigurationDeleteResponse: vcamanagement_service.ConfigurationDeleteResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._delete(params={}),
                            rc_mapping={
                                200: 'ConfigurationDeleteResponse'
                            }
                        )

                    def get(self):
                        class Output(CloudApiOutputModel):
                            ExtendedConfigurationInformation: vcamanagement_service.ExtendedConfigurationInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'ExtendedConfigurationInformation'
                            }
                        )

                    def patch(self, ConfigurationUpdateRequest: vcamanagement_service.ConfigurationUpdateRequest):
                        data = {**ConfigurationUpdateRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ExtendedConfigurationInformation: vcamanagement_service.ExtendedConfigurationInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._patch(data=data),
                            rc_mapping={
                                200: 'ExtendedConfigurationInformation'
                            }
                        )

                class _regions(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            ConfigurationResponse: vcamanagement_service.ConfigurationResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'ConfigurationResponse'
                            }
                        )

            class _intermediatecertificates(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        IntermediateCertificateResponse: vcamanagement_service.IntermediateCertificateResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'IntermediateCertificateResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            IntermediateCertificateInformation: vcamanagement_service.IntermediateCertificateInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'IntermediateCertificateInformation'
                            }
                        )

            class _policies(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        PolicyResponse: vcamanagement_service.PolicyResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'PolicyResponse'
                        }
                    )

                def post(self, PolicyCreateRequest: vcamanagement_service.PolicyCreateRequest):
                    data = {**PolicyCreateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        ExtendedPolicyInformation: vcamanagement_service.ExtendedPolicyInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'ExtendedPolicyInformation'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def delete(self):
                        class Output(CloudApiOutputModel):
                            PolicyDeleteResponse: vcamanagement_service.PolicyDeleteResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._delete(params={}),
                            rc_mapping={
                                200: 'PolicyDeleteResponse'
                            }
                        )

                    def get(self):
                        class Output(CloudApiOutputModel):
                            ExtendedPolicyInformation: vcamanagement_service.ExtendedPolicyInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'ExtendedPolicyInformation'
                            }
                        )

                    def patch(self, PolicyUpdateRequest: vcamanagement_service.PolicyUpdateRequest):
                        data = {**PolicyUpdateRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ExtendedPolicyInformation: vcamanagement_service.ExtendedPolicyInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._patch(data=data),
                            rc_mapping={
                                200: 'ExtendedPolicyInformation'
                            }
                        )

            class _subcaproviders(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        SubCaProviderResponse: vcamanagement_service.SubCaProviderResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'SubCaProviderResponse'
                        }
                    )

                def post(self, SubCaProviderInformation: vcamanagement_service.SubCaProviderInformation):
                    data = {**SubCaProviderInformation.dict()}

                    class Output(CloudApiOutputModel):
                        SubCaProviderInformation: vcamanagement_service.SubCaProviderInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'SubCaProviderInformation'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def delete(self):
                        class Output(CloudApiOutputModel):
                            SubCaProviderDeleteResponse: vcamanagement_service.SubCaProviderDeleteResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._delete(params={}),
                            rc_mapping={
                                200: 'SubCaProviderDeleteResponse'
                            }
                        )

                    def get(self):
                        class Output(CloudApiOutputModel):
                            SubCaProviderInformation: vcamanagement_service.SubCaProviderInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'SubCaProviderInformation'
                            }
                        )

                    def patch(self, SubCaProviderInformation: vcamanagement_service.SubCaProviderInformation):
                        data = {**SubCaProviderInformation.dict()}

                        class Output(CloudApiOutputModel):
                            SubCaProviderUpdateRequest: vcamanagement_service.SubCaProviderUpdateRequest

                        return generate_output(
                            output_cls=Output,
                            response=self._patch(data=data),
                            rc_mapping={
                                200: 'SubCaProviderUpdateRequest'
                            }
                        )
