from __future__ import annotations
from venafi.cloud.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output
from venafi.cloud.api.models import outagedetection_service
from datetime import datetime
from typing import (Any, Literal, Dict, List)


class _outagedetection(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='outagedetection')
        self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
        self.applications = self._applications(api_obj=self._api_obj, url=f'{self._url}/applications')
        self.certificatesearch = self._certificatesearch(api_obj=self._api_obj, url=f'{self._url}/certificatesearch')
        self.certificateinstances = self._certificateinstances(api_obj=self._api_obj, url=f'{self._url}/certificateinstances')
        self.certificateinstancesearch = self._certificateinstancesearch(api_obj=self._api_obj, url=f'{self._url}/certificateinstancesearch')
        self.savedsearches = self._savedsearches(api_obj=self._api_obj, url=f'{self._url}/savedsearches')
        self.certificateaggregates = self._certificateaggregates(api_obj=self._api_obj, url=f'{self._url}/certificateaggregates')
        self.certificaterequests = self._certificaterequests(api_obj=self._api_obj, url=f'{self._url}/certificaterequests')
        self.certificaterequestssearch = self._certificaterequestssearch(api_obj=self._api_obj, url=f'{self._url}/certificaterequestssearch')
        self.applicationservertypes = self._applicationservertypes(api_obj=self._api_obj, url=f'{self._url}/applicationservertypes')

    class _certificates(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')
            self.retirement = self._retirement(api_obj=self._api_obj, url=f'{self._url}/retirement')
            self.recovery = self._recovery(api_obj=self._api_obj, url=f'{self._url}/recovery')
            self.deletion = self._deletion(api_obj=self._api_obj, url=f'{self._url}/deletion')
            self.managed = self._managed(api_obj=self._api_obj, url=f'{self._url}/managed')

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def get(self, subject: str, limit: int):
            data = {
                'subject': subject,
                'limit': limit,
            }

            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._get(params=data))

        def post(self, CertificateImportRequest: outagedetection_service.CertificateImportRequest):
            data = {**CertificateImportRequest.dict()}

            class Output(VaasSdkOutputModel):
                CertificateImportResponse: outagedetection_service.CertificateImportResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateImportResponse'})

        class _validation(VaasSdkEndpoint):
            def post(self, CertificateValidationRequest: outagedetection_service.CertificateValidationRequest):
                data = {**CertificateValidationRequest.dict()}

                class Output(VaasSdkOutputModel):
                    length: int
                    location: str
                    language: outagedetection_service.language
                    lastModified: datetime
                    date: datetime
                    mediaType: outagedetection_service.mediaType
                    metadataDict: Dict[str, List[Dict[str, Any]]]
                    status: int
                    stringHeadersDict: Dict[str, List[str]]
                    allowedMethodsList: List[str]
                    entityTag: outagedetection_service.entityTag
                    linksList: List[Dict[str, Any]]
                    cookiesDict: Dict[str, Dict[str, Any]]
                    statusInfo: outagedetection_service.statusInfo
                    headersDict: Dict[str, List[Dict[str, Any]]]
                    entityDict: Dict[str, Any]
                return generate_output(output_cls=Output, response=self._post(data=data))

        class _ID(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.contents = self._contents(api_obj=self._api_obj, url=f'{self._url}/contents')
                self.keystore = self._keystore(api_obj=self._api_obj, url=f'{self._url}/keystore')

            def get(self, ownershipTree: bool):
                data = {
                    'ownershipTree': ownershipTree,
                }

                class Output(VaasSdkOutputModel):
                    ExtendedCertificateInformation: outagedetection_service.ExtendedCertificateInformation
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ExtendedCertificateInformation'})

            class _contents(VaasSdkEndpoint):
                def get(self, format: Literal['DER', 'PEM'], chainOrder: Literal['EE_FIRST', 'EE_ONLY', 'ROOT_FIRST']):
                    data = {
                        'format': format,
                        'chainOrder': chainOrder,
                    }

                    class Output(VaasSdkOutputModel):
                        str: str
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'str'})

            class _keystore(VaasSdkEndpoint):
                def post(self, CertificateKeystoreRequest: outagedetection_service.CertificateKeystoreRequest):
                    data = {**CertificateKeystoreRequest.dict()}

                    class Output(VaasSdkOutputModel):
                        str: str
                    return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'str'})

        class _retirement(VaasSdkEndpoint):
            def post(self, CertificateRetirementRequest: outagedetection_service.CertificateRetirementRequest):
                data = {**CertificateRetirementRequest.dict()}

                class Output(VaasSdkOutputModel):
                    CertificateResponse: outagedetection_service.CertificateResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateResponse'})

        class _recovery(VaasSdkEndpoint):
            def post(self, CertificateRecoveryRequest: outagedetection_service.CertificateRecoveryRequest):
                data = {**CertificateRecoveryRequest.dict()}

                class Output(VaasSdkOutputModel):
                    CertificateResponse: outagedetection_service.CertificateResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateResponse'})

        class _deletion(VaasSdkEndpoint):
            def post(self, CertificateDeletionRequest: outagedetection_service.CertificateDeletionRequest):
                data = {**CertificateDeletionRequest.dict()}

                class Output(VaasSdkOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._post(data=data))

        class _managed(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            class _ID(VaasSdkEndpoint):
                def get(self, ownershipTree: bool):
                    data = {
                        'ownershipTree': ownershipTree,
                    }

                    class Output(VaasSdkOutputModel):
                        CertificateResponse: outagedetection_service.CertificateResponse
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateResponse'})

    class _applications(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
            self.name = self._name(api_obj=self._api_obj, url=f'{self._url}/name')

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def NAME(self, name: str):
            return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

        def get(self, ownerDetails: bool, ownershipCheck: bool, issuingTemplateAssigned: bool, ownershipTree: bool):
            data = {
                'ownerDetails': ownerDetails,
                'ownershipCheck': ownershipCheck,
                'issuingTemplateAssigned': issuingTemplateAssigned,
                'ownershipTree': ownershipTree,
            }

            class Output(VaasSdkOutputModel):
                ApplicationResponse: outagedetection_service.ApplicationResponse
            return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ApplicationResponse'})

        def post(self, ApplicationRequest: outagedetection_service.ApplicationRequest):
            data = {**ApplicationRequest.dict()}

            class Output(VaasSdkOutputModel):
                ApplicationResponse: outagedetection_service.ApplicationResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'ApplicationResponse'})

        class _ID(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.scanaficonfiguration = self._scanaficonfiguration(api_obj=self._api_obj, url=f'{self._url}/scanaficonfiguration')
                self.invitations = self._invitations(api_obj=self._api_obj, url=f'{self._url}/invitations')

            def get(self, ownershipTree: bool):
                data = {
                    'ownershipTree': ownershipTree,
                }

                class Output(VaasSdkOutputModel):
                    ApplicationInformation: outagedetection_service.ApplicationInformation
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ApplicationInformation'})

            def put(self, ApplicationRequest: outagedetection_service.ApplicationRequest):
                data = {**ApplicationRequest.dict()}

                class Output(VaasSdkOutputModel):
                    ApplicationInformation: outagedetection_service.ApplicationInformation
                return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'ApplicationInformation'})

            def delete(self):
                class Output(VaasSdkOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._delete(params={}))

            class _scanaficonfiguration(VaasSdkEndpoint):
                def get(self):
                    class Output(VaasSdkOutputModel):
                        ScanafiConfigResponseV1: outagedetection_service.ScanafiConfigResponseV1
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ScanafiConfigResponseV1'})

            class _invitations(VaasSdkEndpoint):
                def post(self, InvitationRequest: outagedetection_service.InvitationRequest):
                    data = {**InvitationRequest.dict()}

                    class Output(VaasSdkOutputModel):
                        InvitationResponse: outagedetection_service.InvitationResponse
                    return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'InvitationResponse'})

        class _certificates(VaasSdkEndpoint):
            def patch(self, ApplicationsAssignRequest: outagedetection_service.ApplicationsAssignRequest):
                data = {**ApplicationsAssignRequest.dict()}

                class Output(VaasSdkOutputModel):
                    ApplicationsAssignResponse: outagedetection_service.ApplicationsAssignResponse
                return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'ApplicationsAssignResponse'})

        class _name(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def NAME(self, name: str):
                return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

            class _NAME(VaasSdkEndpoint):
                def get(self, ownershipTree: bool):
                    data = {
                        'ownershipTree': ownershipTree,
                    }

                    class Output(VaasSdkOutputModel):
                        ApplicationInformation: outagedetection_service.ApplicationInformation
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ApplicationInformation'})

        class _NAME(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.certificateissuingtemplates = self._certificateissuingtemplates(
                    api_obj=self._api_obj, url=f'{self._url}/certificateissuingtemplates')

            class _certificateissuingtemplates(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ALIAS(self, alias: str):
                    return self._ALIAS(api_obj=self._api_obj, url=f'{self._url}/{alias}')

                class _ALIAS(VaasSdkEndpoint):
                    def get(self):
                        class Output(VaasSdkOutputModel):
                            CertificateIssuingTemplateInformation: outagedetection_service.CertificateIssuingTemplateInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateIssuingTemplateInformation'})

    class _certificatesearch(VaasSdkEndpoint):
        def post(self, CertificateSearchRequest: outagedetection_service.CertificateSearchRequest):
            data = {**CertificateSearchRequest.dict()}

            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._post(data=data))

    class _certificateinstances(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def get(self, source: Literal['DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'ON_PREM_CA_IMPORT', 'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL', 'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'], ipAddress: str, hostname: str, limit: int):
            data = {
                'source': source,
                'ipAddress': ipAddress,
                'hostname': hostname,
                'limit': limit,
            }

            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._get(params=data))

        class _validation(VaasSdkEndpoint):
            def post(self, CertificateInstanceValidationRequest: outagedetection_service.CertificateInstanceValidationRequest):
                data = {**CertificateInstanceValidationRequest.dict()}

                class Output(VaasSdkOutputModel):
                    length: int
                    location: str
                    language: outagedetection_service.language
                    lastModified: datetime
                    date: datetime
                    mediaType: outagedetection_service.mediaType
                    metadataDict: Dict[str, List[Dict[str, Any]]]
                    status: int
                    stringHeadersDict: Dict[str, List[str]]
                    allowedMethodsList: List[str]
                    entityTag: outagedetection_service.entityTag
                    linksList: List[Dict[str, Any]]
                    cookiesDict: Dict[str, Dict[str, Any]]
                    statusInfo: outagedetection_service.statusInfo
                    headersDict: Dict[str, List[Dict[str, Any]]]
                    entityDict: Dict[str, Any]
                return generate_output(output_cls=Output, response=self._post(data=data))

        class _ID(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    ExtendedCertificateInstanceInformation: outagedetection_service.ExtendedCertificateInstanceInformation
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ExtendedCertificateInstanceInformation'})

    class _certificateinstancesearch(VaasSdkEndpoint):
        def post(self, CertificateInstanceSearchRequest: outagedetection_service.CertificateInstanceSearchRequest):
            data = {**CertificateInstanceSearchRequest.dict()}

            class Output(VaasSdkOutputModel):
                pass
            return generate_output(output_cls=Output, response=self._post(data=data))

    class _savedsearches(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def get(self):
            class Output(VaasSdkOutputModel):
                SavedSearchResponse: outagedetection_service.SavedSearchResponse
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'SavedSearchResponse'})

        def post(self, SavedSearchRequest: outagedetection_service.SavedSearchRequest):
            data = {**SavedSearchRequest.dict()}

            class Output(VaasSdkOutputModel):
                SavedSearchResponse: outagedetection_service.SavedSearchResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'SavedSearchResponse'})

        class _ID(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    SavedSearchInfo: outagedetection_service.SavedSearchInfo
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'SavedSearchInfo'})

            def put(self, SavedSearchRequest: outagedetection_service.SavedSearchRequest):
                data = {**SavedSearchRequest.dict()}

                class Output(VaasSdkOutputModel):
                    SavedSearchInfo: outagedetection_service.SavedSearchInfo
                return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'SavedSearchInfo'})

            def delete(self):
                class Output(VaasSdkOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._delete(params={}))

    class _certificateaggregates(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.unassigned = self._unassigned(api_obj=self._api_obj, url=f'{self._url}/unassigned')
            self.range = self._range(api_obj=self._api_obj, url=f'{self._url}/range')
            self.quota = self._quota(api_obj=self._api_obj, url=f'{self._url}/quota')

        def NAME(self, name: str):
            return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

        def post(self, CertificateAggregationsRequest: outagedetection_service.CertificateAggregationsRequest):
            data = {**CertificateAggregationsRequest.dict()}

            class Output(VaasSdkOutputModel):
                FacetResponse: outagedetection_service.FacetResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'FacetResponse'})

        class _NAME(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    CertificateAggregatesResponse: outagedetection_service.CertificateAggregatesResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAggregatesResponse'})

        class _unassigned(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    UnassignedCertificateAggregatesResponse: outagedetection_service.UnassignedCertificateAggregatesResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'UnassignedCertificateAggregatesResponse'})

        class _range(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    CertificateAggregatesRangeResponse: outagedetection_service.CertificateAggregatesRangeResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAggregatesRangeResponse'})

        class _quota(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    CertificateInstallationsUsageResponse: outagedetection_service.CertificateInstallationsUsageResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateInstallationsUsageResponse'})

    class _certificaterequests(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def get(self):
            class Output(VaasSdkOutputModel):
                CertificateRequestResponse: outagedetection_service.CertificateRequestResponse
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateRequestResponse'})

        def post(self, CertificateRequestRequest: outagedetection_service.CertificateRequestRequest):
            data = {**CertificateRequestRequest.dict()}

            class Output(VaasSdkOutputModel):
                CertificateRequestResponse: outagedetection_service.CertificateRequestResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateRequestResponse'})

        class _validation(VaasSdkEndpoint):
            def post(self, CertificateRequestRequest: outagedetection_service.CertificateRequestRequest):
                data = {**CertificateRequestRequest.dict()}

                class Output(VaasSdkOutputModel):
                    CertificationRequestInformation: outagedetection_service.CertificationRequestInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificationRequestInformation'})

        class _ID(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.resubmission = self._resubmission(api_obj=self._api_obj, url=f'{self._url}/resubmission')

            def get(self):
                class Output(VaasSdkOutputModel):
                    CertificateRequestInformation: outagedetection_service.CertificateRequestInformation
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateRequestInformation'})

            class _resubmission(VaasSdkEndpoint):
                def post(self, CertificateRequestResubmissionRequest: outagedetection_service.CertificateRequestResubmissionRequest):
                    data = {**CertificateRequestResubmissionRequest.dict()}

                    class Output(VaasSdkOutputModel):
                        CertificateRequestResponse: outagedetection_service.CertificateRequestResponse
                    return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateRequestResponse'})

    class _certificaterequestssearch(VaasSdkEndpoint):
        def post(self, CertificateRequestsSearchRequest: outagedetection_service.CertificateRequestsSearchRequest):
            data = {**CertificateRequestsSearchRequest.dict()}

            class Output(VaasSdkOutputModel):
                CertificateRequestDocumentResponse: outagedetection_service.CertificateRequestDocumentResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateRequestDocumentResponse'})

    class _applicationservertypes(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def ID(self, id: str):
            return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

        def get(self):
            class Output(VaasSdkOutputModel):
                ApplicationServerTypeResponse: outagedetection_service.ApplicationServerTypeResponse
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ApplicationServerTypeResponse'})

        def post(self, BaseApplicationServerTypeRequest: outagedetection_service.BaseApplicationServerTypeRequest):
            data = {**BaseApplicationServerTypeRequest.dict()}

            class Output(VaasSdkOutputModel):
                ApplicationServerTypeInformation: outagedetection_service.ApplicationServerTypeInformation
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'ApplicationServerTypeInformation'})

        class _ID(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    ApplicationServerTypeInformation: outagedetection_service.ApplicationServerTypeInformation
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ApplicationServerTypeInformation'})

            def delete(self):
                class Output(VaasSdkOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._delete(params={}))
