from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    CloudApiEndpoint,
    CloudApiOutputModel,
    generate_output,
)
from pyvenafi.cloud.api.models import outagedetection_service
from typing import (
    Any,
    Literal,
)

class _outagedetection_service:
    def __init__(self, api_obj):
        self.outagedetection = self._outagedetection(api_obj=api_obj)

    class _outagedetection(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='outagedetection')
            self.v1 = self._v1(api_obj=self._api_obj, url=f'{self._url}/v1')

        class _v1(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.applications = self._applications(api_obj=self._api_obj, url=f'{self._url}/applications')
                self.certificateaggregates = self._certificateaggregates(
                    api_obj=self._api_obj,
                    url=f'{self._url}/certificateaggregates'
                )
                self.certificateinstances = self._certificateinstances(
                    api_obj=self._api_obj,
                    url=f'{self._url}/certificateinstances'
                )
                self.certificateinstancesearch = self._certificateinstancesearch(
                    api_obj=self._api_obj, url=f'{self._url}/certificateinstancesearch'
                )
                self.certificaterequests = self._certificaterequests(
                    api_obj=self._api_obj,
                    url=f'{self._url}/certificaterequests'
                )
                self.certificaterequestssearch = self._certificaterequestssearch(
                    api_obj=self._api_obj, url=f'{self._url}/certificaterequestssearch'
                )
                self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
                self.certificatesearch = self._certificatesearch(
                    api_obj=self._api_obj,
                    url=f'{self._url}/certificatesearch'
                )
                self.inventorymonitoringconfig = self._inventorymonitoringconfig(
                    api_obj=self._api_obj, url=f'{self._url}/inventorymonitoringconfig'
                )
                self.savedsearches = self._savedsearches(api_obj=self._api_obj, url=f'{self._url}/savedsearches')

            class _applications(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
                    self.name = self._name(api_obj=self._api_obj, url=f'{self._url}/name')

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def NAME(self, name: str):
                    return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

                def get(
                    self,
                    issuingTemplateAssigned: bool,
                    ownerDetails: bool,
                    ownershipCheck: bool,
                    ownershipTree: bool
                ):
                    data = {
                        'issuingTemplateAssigned': issuingTemplateAssigned,
                        'ownerDetails'           : ownerDetails,
                        'ownershipCheck'         : ownershipCheck,
                        'ownershipTree'          : ownershipTree,
                    }

                    class Output(CloudApiOutputModel):
                        ApplicationResponse: outagedetection_service.ApplicationResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params=data),
                        rc_mapping={
                            200: 'ApplicationResponse'
                        }
                    )

                def post(self, ApplicationRequest: outagedetection_service.ApplicationRequest):
                    data = {**ApplicationRequest.dict()}

                    class Output(CloudApiOutputModel):
                        ApplicationResponse: outagedetection_service.ApplicationResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'ApplicationResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.invitations = self._invitations(api_obj=self._api_obj, url=f'{self._url}/invitations')
                        self.scanaficonfiguration = self._scanaficonfiguration(
                            api_obj=self._api_obj,
                            url=f'{self._url}/scanaficonfiguration'
                        )

                    def delete(self):
                        class Output(CloudApiOutputModel):
                            pass

                        return generate_output(output_cls=Output, response=self._delete(params={}))

                    def get(self, ownershipTree: bool):
                        data = {
                            'ownershipTree': ownershipTree,
                        }

                        class Output(CloudApiOutputModel):
                            ApplicationInformation: outagedetection_service.ApplicationInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params=data),
                            rc_mapping={
                                200: 'ApplicationInformation'
                            }
                        )

                    def put(self, ApplicationRequest: outagedetection_service.ApplicationRequest):
                        data = {**ApplicationRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ApplicationInformation: outagedetection_service.ApplicationInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._put(data=data),
                            rc_mapping={
                                200: 'ApplicationInformation'
                            }
                        )

                    class _invitations(CloudApiEndpoint):
                        def post(self, InvitationRequest: outagedetection_service.InvitationRequest):
                            data = {**InvitationRequest.dict()}

                            class Output(CloudApiOutputModel):
                                InvitationResponse: outagedetection_service.InvitationResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data=data),
                                rc_mapping={
                                    201: 'InvitationResponse'
                                }
                            )

                    class _scanaficonfiguration(CloudApiEndpoint):
                        def get(self):
                            class Output(CloudApiOutputModel):
                                ScanafiConfigResponseV1: outagedetection_service.ScanafiConfigResponseV1

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params={}),
                                rc_mapping={
                                    200: 'ScanafiConfigResponseV1'
                                }
                            )

                class _NAME(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.certificateissuingtemplates = self._certificateissuingtemplates(
                            api_obj=self._api_obj, url=f'{self._url}/certificateissuingtemplates'
                        )

                    class _certificateissuingtemplates(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)

                        def ALIAS(self, alias: str):
                            return self._ALIAS(api_obj=self._api_obj, url=f'{self._url}/{alias}')

                        class _ALIAS(CloudApiEndpoint):
                            def get(self):
                                class Output(CloudApiOutputModel):
                                    CertificateIssuingTemplateInformation: outagedetection_service.CertificateIssuingTemplateInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._get(params={}),
                                    rc_mapping={
                                        200: 'CertificateIssuingTemplateInformation'
                                    }
                                )

                class _certificates(CloudApiEndpoint):
                    def patch(self, ApplicationsAssignRequest: outagedetection_service.ApplicationsAssignRequest):
                        data = {**ApplicationsAssignRequest.dict()}

                        class Output(CloudApiOutputModel):
                            ApplicationsAssignResponse: outagedetection_service.ApplicationsAssignResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._patch(data=data),
                            rc_mapping={
                                200: 'ApplicationsAssignResponse'
                            }
                        )

                class _name(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def NAME(self, name: str):
                        return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

                    class _NAME(CloudApiEndpoint):
                        def get(self, ownershipTree: bool):
                            data = {
                                'ownershipTree': ownershipTree,
                            }

                            class Output(CloudApiOutputModel):
                                ApplicationInformation: outagedetection_service.ApplicationInformation

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params=data),
                                rc_mapping={
                                    200: 'ApplicationInformation'
                                }
                            )

            class _certificateaggregates(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.quota = self._quota(api_obj=self._api_obj, url=f'{self._url}/quota')
                    self.range = self._range(api_obj=self._api_obj, url=f'{self._url}/range')
                    self.unassigned = self._unassigned(api_obj=self._api_obj, url=f'{self._url}/unassigned')

                def NAME(self, name: str):
                    return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

                def post(self, CertificateAggregationsRequest: outagedetection_service.CertificateAggregationsRequest):
                    data = {**CertificateAggregationsRequest.dict()}

                    class Output(CloudApiOutputModel):
                        FacetResponse: outagedetection_service.FacetResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            200: 'FacetResponse'
                        }
                    )

                class _NAME(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateAggregatesResponse: outagedetection_service.CertificateAggregatesResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateAggregatesResponse'
                            }
                        )

                class _quota(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateInstallationsUsageResponse: outagedetection_service.CertificateInstallationsUsageResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateInstallationsUsageResponse'
                            }
                        )

                class _range(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateAggregatesRangeResponse: outagedetection_service.CertificateAggregatesRangeResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateAggregatesRangeResponse'
                            }
                        )

                class _unassigned(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            UnassignedCertificateAggregatesResponse: outagedetection_service.UnassignedCertificateAggregatesResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'UnassignedCertificateAggregatesResponse'
                            }
                        )

            class _certificateinstances(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(
                    self,
                    hostname: str,
                    ipAddress: str,
                    limit: int,
                    source: Literal[
                        'AWS_DISCOVERY', 'AZURE_DISCOVERY', 'DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'GCP_DISCOVERY', 'KUBERNETES_DISCOVERY', 'MACHINE_DISCOVERY', 'ON_PREM_CA_IMPORT', 'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL', 'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN']
                ):
                    data = {
                        'hostname' : hostname,
                        'ipAddress': ipAddress,
                        'limit'    : limit,
                        'source'   : source,
                    }

                    class Output(CloudApiOutputModel):
                        ExtendedCertificateInstanceResponse: outagedetection_service.ExtendedCertificateInstanceResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params=data),
                        rc_mapping={
                            200: 'ExtendedCertificateInstanceResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            ExtendedCertificateInstanceInformation: outagedetection_service.ExtendedCertificateInstanceInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'ExtendedCertificateInstanceInformation'
                            }
                        )

                class _validation(CloudApiEndpoint):
                    def post(
                        self,
                        CertificateInstanceValidationRequest: outagedetection_service.CertificateInstanceValidationRequest
                    ):
                        data = {**CertificateInstanceValidationRequest.dict()}

                        class Output(CloudApiOutputModel):
                            Response: outagedetection_service.Response

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                202: 'Response'
                            }
                        )

            class _certificateinstancesearch(CloudApiEndpoint):
                def post(self, Filter: outagedetection_service.Filter):
                    data = {**Filter.dict()}

                    class Output(CloudApiOutputModel):
                        ExtendedCertificateInstanceResponse: outagedetection_service.ExtendedCertificateInstanceResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            200: 'ExtendedCertificateInstanceResponse'
                        }
                    )

            class _certificaterequests(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        CertificateRequestResponse: outagedetection_service.CertificateRequestResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'CertificateRequestResponse'
                        }
                    )

                def post(self, CertificateRequestRequest: outagedetection_service.CertificateRequestRequest):
                    data = {**CertificateRequestRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateRequestResponse: outagedetection_service.CertificateRequestResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'CertificateRequestResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.resubmission = self._resubmission(api_obj=self._api_obj, url=f'{self._url}/resubmission')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateRequestInformation: outagedetection_service.CertificateRequestInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateRequestInformation'
                            }
                        )

                    class _resubmission(CloudApiEndpoint):
                        def post(
                            self,
                            CertificateRequestResubmissionRequest: outagedetection_service.CertificateRequestResubmissionRequest
                        ):
                            data = {**CertificateRequestResubmissionRequest.dict()}

                            class Output(CloudApiOutputModel):
                                CertificateRequestResponse: outagedetection_service.CertificateRequestResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data=data),
                                rc_mapping={
                                    200: 'CertificateRequestResponse'
                                }
                            )

                class _validation(CloudApiEndpoint):
                    def post(self, CertificateRequestRequest: outagedetection_service.CertificateRequestRequest):
                        data = {**CertificateRequestRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificationRequestInformation: outagedetection_service.CertificationRequestInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                201: 'CertificationRequestInformation'
                            }
                        )

            class _certificaterequestssearch(CloudApiEndpoint):
                def post(self, Filter: outagedetection_service.Filter):
                    data = {**Filter.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateRequestDocumentResponse: outagedetection_service.CertificateRequestDocumentResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            200: 'CertificateRequestDocumentResponse'
                        }
                    )

            class _certificates(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.deletion = self._deletion(api_obj=self._api_obj, url=f'{self._url}/deletion')
                    self.managed = self._managed(api_obj=self._api_obj, url=f'{self._url}/managed')
                    self.recovery = self._recovery(api_obj=self._api_obj, url=f'{self._url}/recovery')
                    self.retirement = self._retirement(api_obj=self._api_obj, url=f'{self._url}/retirement')
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self, excludeSupersededInstances: bool, limit: Any, ownershipTree: bool, subject: str):
                    data = {
                        'excludeSupersededInstances': excludeSupersededInstances,
                        'limit'                     : limit,
                        'ownershipTree'             : ownershipTree,
                        'subject'                   : subject,
                    }

                    class Output(CloudApiOutputModel):
                        CertificateResponse: outagedetection_service.CertificateResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params=data),
                        rc_mapping={
                            200: 'CertificateResponse'
                        }
                    )

                def post(self, CertificateImportRequest: outagedetection_service.CertificateImportRequest):
                    data = {**CertificateImportRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateImportResponse: outagedetection_service.CertificateImportResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'CertificateImportResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.contents = self._contents(api_obj=self._api_obj, url=f'{self._url}/contents')
                        self.keystore = self._keystore(api_obj=self._api_obj, url=f'{self._url}/keystore')

                    def get(self, excludeSupersededInstances: bool, ownershipTree: bool):
                        data = {
                            'excludeSupersededInstances': excludeSupersededInstances,
                            'ownershipTree'             : ownershipTree,
                        }

                        class Output(CloudApiOutputModel):
                            ExtendedCertificateInformation: outagedetection_service.ExtendedCertificateInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params=data),
                            rc_mapping={
                                200: 'ExtendedCertificateInformation'
                            }
                        )

                    class _contents(CloudApiEndpoint):
                        def get(
                            self,
                            Accept: Literal['application/octet-stream', 'text/plain'],
                            chainOrder: Literal['EE_FIRST', 'EE_ONLY', 'ROOT_FIRST'],
                            format: Literal['DER', 'PEM']
                        ):
                            data = {
                                'Accept'    : Accept,
                                'chainOrder': chainOrder,
                                'format'    : format,
                            }

                            class Output(CloudApiOutputModel):
                                str: str

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params=data),
                                rc_mapping={
                                    200: 'str'
                                }
                            )

                    class _keystore(CloudApiEndpoint):
                        def post(self, CertificateKeystoreRequest: outagedetection_service.CertificateKeystoreRequest):
                            data = {**CertificateKeystoreRequest.dict()}

                            class Output(CloudApiOutputModel):
                                str: str

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data=data),
                                rc_mapping={
                                    200: 'str'
                                }
                            )

                class _deletion(CloudApiEndpoint):
                    def post(self, CertificateDeletionRequest: outagedetection_service.CertificateDeletionRequest):
                        data = {**CertificateDeletionRequest.dict()}

                        class Output(CloudApiOutputModel):
                            pass

                        return generate_output(output_cls=Output, response=self._post(data=data))

                class _managed(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    class _ID(CloudApiEndpoint):
                        def get(self, excludeSupersededInstances: bool, ownershipTree: bool):
                            data = {
                                'excludeSupersededInstances': excludeSupersededInstances,
                                'ownershipTree'             : ownershipTree,
                            }

                            class Output(CloudApiOutputModel):
                                CertificateResponse: outagedetection_service.CertificateResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params=data),
                                rc_mapping={
                                    200: 'CertificateResponse'
                                }
                            )

                class _recovery(CloudApiEndpoint):
                    def post(self, CertificateRecoveryRequest: outagedetection_service.CertificateRecoveryRequest):
                        data = {**CertificateRecoveryRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateResponse: outagedetection_service.CertificateResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                200: 'CertificateResponse'
                            }
                        )

                class _retirement(CloudApiEndpoint):
                    def post(self, CertificateRetirementRequest: outagedetection_service.CertificateRetirementRequest):
                        data = {**CertificateRetirementRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateResponse: outagedetection_service.CertificateResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                200: 'CertificateResponse'
                            }
                        )

                class _validation(CloudApiEndpoint):
                    def post(self, CertificateValidationRequest: outagedetection_service.CertificateValidationRequest):
                        data = {**CertificateValidationRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateValidationResponse: outagedetection_service.CertificateValidationResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                202: 'CertificateValidationResponse'
                            }
                        )

            class _certificatesearch(CloudApiEndpoint):
                def post(self, excludeSupersededInstances: bool, ownershipTree: bool):
                    data = {
                        'excludeSupersededInstances': excludeSupersededInstances,
                        'ownershipTree'             : ownershipTree,
                    }

                    class Output(CloudApiOutputModel):
                        CertificateResponse: outagedetection_service.CertificateResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            200: 'CertificateResponse'
                        }
                    )

            class _inventorymonitoringconfig(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def TYPE(self, type: str):
                    return self._TYPE(api_obj=self._api_obj, url=f'{self._url}/{type}')

                class _TYPE(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.scheduler = self._scheduler(api_obj=self._api_obj, url=f'{self._url}/scheduler')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            InventoryMonitoringConfigurationResponse: outagedetection_service.InventoryMonitoringConfigurationResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'InventoryMonitoringConfigurationResponse'
                            }
                        )

                    def put(
                        self,
                        InventoryMonitoringConfigRequest: outagedetection_service.InventoryMonitoringConfigRequest
                    ):
                        data = {**InventoryMonitoringConfigRequest.dict()}

                        class Output(CloudApiOutputModel):
                            InventoryMonitoringConfigurationResponse: outagedetection_service.InventoryMonitoringConfigurationResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._put(data=data),
                            rc_mapping={
                                200: 'InventoryMonitoringConfigurationResponse'
                            }
                        )

                    class _scheduler(CloudApiEndpoint):
                        def put(self, runNow: bool):
                            data = {
                                'runNow': runNow,
                            }

                            class Output(CloudApiOutputModel):
                                InventoryMonitoringSchedulerInformation: outagedetection_service.InventoryMonitoringSchedulerInformation

                            return generate_output(
                                output_cls=Output,
                                response=self._put(data=data),
                                rc_mapping={
                                    200: 'InventoryMonitoringSchedulerInformation'
                                }
                            )

            class _savedsearches(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        SavedSearchResponse: outagedetection_service.SavedSearchResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'SavedSearchResponse'
                        }
                    )

                def post(self, SavedSearchRequest: outagedetection_service.SavedSearchRequest):
                    data = {**SavedSearchRequest.dict()}

                    class Output(CloudApiOutputModel):
                        SavedSearchResponse: outagedetection_service.SavedSearchResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'SavedSearchResponse'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def delete(self):
                        class Output(CloudApiOutputModel):
                            pass

                        return generate_output(output_cls=Output, response=self._delete(params={}))

                    def get(self):
                        class Output(CloudApiOutputModel):
                            SavedSearchInfo: outagedetection_service.SavedSearchInfo

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'SavedSearchInfo'
                            }
                        )

                    def put(self, SavedSearchRequest: outagedetection_service.SavedSearchRequest):
                        data = {**SavedSearchRequest.dict()}

                        class Output(CloudApiOutputModel):
                            SavedSearchInfo: outagedetection_service.SavedSearchInfo

                        return generate_output(
                            output_cls=Output,
                            response=self._put(data=data),
                            rc_mapping={
                                200: 'SavedSearchInfo'
                            }
                        )
