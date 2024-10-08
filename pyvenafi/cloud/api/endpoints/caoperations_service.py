from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    CloudApiEndpoint,
    CloudApiOutputModel,
    generate_output,
)
from pyvenafi.cloud.api.models import caoperations_service
from typing import Literal
from uuid import UUID

class _caoperations_service:
    def __init__(self, api_obj):
        self.v1 = self._v1(api_obj=api_obj)

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.builtinca = self._builtinca(api_obj=self._api_obj, url=f'{self._url}/builtinca')
            self.certificateauthorities = self._certificateauthorities(
                api_obj=self._api_obj,
                url=f'{self._url}/certificateauthorities'
            )
            self.certificateissuingtemplates = self._certificateissuingtemplates(
                api_obj=self._api_obj, url=f'{self._url}/certificateissuingtemplates'
            )
            self.certificaterequests = self._certificaterequests(
                api_obj=self._api_obj,
                url=f'{self._url}/certificaterequests'
            )
            self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')

        class _builtinca(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.ca = self._ca(api_obj=self._api_obj, url=f'{self._url}/ca')
                self.cachain = self._cachain(api_obj=self._api_obj, url=f'{self._url}/cachain')
                self.crl = self._crl(api_obj=self._api_obj, url=f'{self._url}/crl')

            class _ca(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def CANAME(self, caname: str):
                    return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

                class _CANAME(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            str: str

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'str'
                            }
                        )

            class _cachain(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def CANAME(self, caname: str):
                    return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

                class _CANAME(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            str: str

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'str'
                            }
                        )

            class _crl(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def CANAME(self, caname: str):
                    return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

                class _CANAME(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            str: str

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'str'
                            }
                        )

        class _certificateauthorities(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def CERTIFICATEAUTHORITY(self, certificateauthority: str):
                return self._CERTIFICATEAUTHORITY(api_obj=self._api_obj, url=f'{self._url}/{certificateauthority}')

            def get(
                self,
                includeSystemGenerated: bool,
                issuanceCertificateType: Literal['ALL', 'END_ENTITY', 'ISSUER']
            ):
                data = {
                    'includeSystemGenerated' : includeSystemGenerated,
                    'issuanceCertificateType': issuanceCertificateType,
                }

                class Output(CloudApiOutputModel):
                    CertificateAuthorityResponse: caoperations_service.CertificateAuthorityResponse

                return generate_output(
                    output_cls=Output,
                    response=self._get(params=data),
                    rc_mapping={
                        200: 'CertificateAuthorityResponse'
                    }
                )

            class _CERTIFICATEAUTHORITY(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.accounts = self._accounts(api_obj=self._api_obj, url=f'{self._url}/accounts')

                class _accounts(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.configuration = self._configuration(
                            api_obj=self._api_obj,
                            url=f'{self._url}/configuration'
                        )
                        self.connection = self._connection(api_obj=self._api_obj, url=f'{self._url}/connection')
                        self.credentials = self._credentials(api_obj=self._api_obj, url=f'{self._url}/credentials')

                    def ACCOUNTID(self, accountid: str):
                        return self._ACCOUNTID(api_obj=self._api_obj, url=f'{self._url}/{accountid}')

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(
                        self,
                        edgeInstanceId: UUID,
                        includeObsoleteOptionsDetails: bool,
                        includeOptionsDetails: bool,
                        reloadOptionsDetails: bool
                    ):
                        data = {
                            'edgeInstanceId'               : edgeInstanceId,
                            'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                            'includeOptionsDetails'        : includeOptionsDetails,
                            'reloadOptionsDetails'         : reloadOptionsDetails,
                        }

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params=data),
                            rc_mapping={
                                200: 'CertificateAuthorityAccountResponse'
                            }
                        )

                    def post(
                        self,
                        CertificateAuthorityAccountRequest: caoperations_service.CertificateAuthorityAccountRequest
                    ):
                        data = {**CertificateAuthorityAccountRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                201: 'CertificateAuthorityAccountResponse',
                                202: 'CertificateAuthorityAccountResponse'
                            }
                        )

                    class _ACCOUNTID(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.domains = self._domains(api_obj=self._api_obj, url=f'{self._url}/domains')
                            self.importoptions = self._importoptions(
                                api_obj=self._api_obj,
                                url=f'{self._url}/importoptions'
                            )
                            self.operations = self._operations(api_obj=self._api_obj, url=f'{self._url}/operations')
                            self.productoptions = self._productoptions(
                                api_obj=self._api_obj,
                                url=f'{self._url}/productoptions'
                            )

                        class _domains(CloudApiEndpoint):
                            def __init__(self, *args, **kwargs):
                                super().__init__(*args, **kwargs)

                            def ID(self, id: str):
                                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                            def get(self):
                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._get(params={}),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountDomainInformation'
                                    }
                                )

                            def post(
                                self,
                                CertificateAuthorityAccountDomainRequest: caoperations_service.CertificateAuthorityAccountDomainRequest
                            ):
                                data = {**CertificateAuthorityAccountDomainRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountDomainInformation'
                                    }
                                )

                            class _ID(CloudApiEndpoint):
                                def get(self):
                                    class Output(CloudApiOutputModel):
                                        CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation

                                    return generate_output(
                                        output_cls=Output,
                                        response=self._get(params={}),
                                        rc_mapping={
                                            200: 'CertificateAuthorityAccountDomainInformation'
                                        }
                                    )

                        class _importoptions(CloudApiEndpoint):
                            def __init__(self, *args, **kwargs):
                                super().__init__(*args, **kwargs)

                            def ID(self, id: str):
                                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                            def get(self):
                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountImportOptionResponse: caoperations_service.CertificateAuthorityAccountImportOptionResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._get(params={}),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountImportOptionResponse'
                                    }
                                )

                            def post(
                                self,
                                CertificateAuthorityAccountImportOptionRequest: caoperations_service.CertificateAuthorityAccountImportOptionRequest
                            ):
                                data = {**CertificateAuthorityAccountImportOptionRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        201: 'CertificateAuthorityImportOptionInformation'
                                    }
                                )

                            class _ID(CloudApiEndpoint):
                                def delete(self):
                                    class Output(CloudApiOutputModel):
                                        pass

                                    return generate_output(output_cls=Output, response=self._delete(params={}))

                                def get(self):
                                    class Output(CloudApiOutputModel):
                                        CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation

                                    return generate_output(
                                        output_cls=Output,
                                        response=self._get(params={}),
                                        rc_mapping={
                                            200: 'CertificateAuthorityImportOptionInformation'
                                        }
                                    )

                        class _operations(CloudApiEndpoint):
                            def post(self, CaOperationRequest: caoperations_service.CaOperationRequest):
                                data = {**CaOperationRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountInformation: caoperations_service.CertificateAuthorityAccountInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountInformation'
                                    }
                                )

                        class _productoptions(CloudApiEndpoint):
                            def __init__(self, *args, **kwargs):
                                super().__init__(*args, **kwargs)
                                self.testissuance = self._testissuance(
                                    api_obj=self._api_obj,
                                    url=f'{self._url}/testissuance'
                                )

                            def ID(self, id: str):
                                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                            def get(self):
                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._get(params={}),
                                    rc_mapping={
                                        200: 'CertificateAuthorityProductOptionResponse'
                                    }
                                )

                            def post(
                                self,
                                CertificateAuthorityProductOptionRequest: caoperations_service.CertificateAuthorityProductOptionRequest
                            ):
                                data = {**CertificateAuthorityProductOptionRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation
                                    CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        201: 'CertificateAuthorityProductOptionInformation',
                                        202: 'CertificateAuthorityProductOptionResponse'
                                    }
                                )

                            class _ID(CloudApiEndpoint):
                                def delete(self):
                                    class Output(CloudApiOutputModel):
                                        pass

                                    return generate_output(output_cls=Output, response=self._delete(params={}))

                                def get(self):
                                    class Output(CloudApiOutputModel):
                                        CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation

                                    return generate_output(
                                        output_cls=Output,
                                        response=self._get(params={}),
                                        rc_mapping={
                                            200: 'CertificateAuthorityProductOptionInformation'
                                        }
                                    )

                            class _testissuance(CloudApiEndpoint):
                                def get(self):
                                    class Output(CloudApiOutputModel):
                                        CertificateAuthorityProductOptionsTestIssuanceResultsResponse: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceResultsResponse

                                    return generate_output(
                                        output_cls=Output,
                                        response=self._get(params={}),
                                        rc_mapping={
                                            200: 'CertificateAuthorityProductOptionsTestIssuanceResultsResponse'
                                        }
                                    )

                                def post(
                                    self,
                                    CertificateAuthorityProductOptionsTestIssuanceRequest: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceRequest
                                ):
                                    data = {**CertificateAuthorityProductOptionsTestIssuanceRequest.dict()}

                                    class Output(CloudApiOutputModel):
                                        pass

                                    return generate_output(output_cls=Output, response=self._post(data=data))

                    class _ID(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.certificateimportstatus = self._certificateimportstatus(
                                api_obj=self._api_obj, url=f'{self._url}/certificateimportstatus'
                            )
                            self.issuingrules = self._issuingrules(
                                api_obj=self._api_obj,
                                url=f'{self._url}/issuingrules'
                            )
                            self.synchronisation = self._synchronisation(
                                api_obj=self._api_obj,
                                url=f'{self._url}/synchronisation'
                            )

                        def delete(self):
                            class Output(CloudApiOutputModel):
                                CertificateAuthorityAccountDeleteResponse: caoperations_service.CertificateAuthorityAccountDeleteResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._delete(params={}),
                                rc_mapping={
                                    200: 'CertificateAuthorityAccountDeleteResponse'
                                }
                            )

                        def get(
                            self,
                            includeObsoleteOptionsDetails: bool,
                            includeOptionsDetails: bool,
                            reloadAccountDetails: bool,
                            reloadOptionsDetails: bool
                        ):
                            data = {
                                'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                                'includeOptionsDetails'        : includeOptionsDetails,
                                'reloadAccountDetails'         : reloadAccountDetails,
                                'reloadOptionsDetails'         : reloadOptionsDetails,
                            }

                            class Output(CloudApiOutputModel):
                                ExtendedCertificateAuthorityAccountInformation: caoperations_service.ExtendedCertificateAuthorityAccountInformation

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params=data),
                                rc_mapping={
                                    200: 'ExtendedCertificateAuthorityAccountInformation'
                                }
                            )

                        def put(
                            self,
                            CertificateAuthorityAccountUpdateRequest: caoperations_service.CertificateAuthorityAccountUpdateRequest
                        ):
                            data = {**CertificateAuthorityAccountUpdateRequest.dict()}

                            class Output(CloudApiOutputModel):
                                CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._put(data=data),
                                rc_mapping={
                                    200: 'CertificateAuthorityAccountResponse'
                                }
                            )

                        class _certificateimportstatus(CloudApiEndpoint):
                            def put(self, CertificateImportRequest: caoperations_service.CertificateImportRequest):
                                data = {**CertificateImportRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._put(data=data),
                                    rc_mapping={
                                        204: 'CertificateAuthorityAccountResponse'
                                    }
                                )

                        class _issuingrules(CloudApiEndpoint):
                            def get(self):
                                class Output(CloudApiOutputModel):
                                    CertificateIssuingTemplateRulesInformation: caoperations_service.CertificateIssuingTemplateRulesInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._get(params={}),
                                    rc_mapping={
                                        200: 'CertificateIssuingTemplateRulesInformation'
                                    }
                                )

                        class _synchronisation(CloudApiEndpoint):
                            def put(self):
                                class Output(CloudApiOutputModel):
                                    ExtendedCertificateAuthorityAccountInformation: caoperations_service.ExtendedCertificateAuthorityAccountInformation

                                return generate_output(
                                    output_cls=Output,
                                    response=self._put(data={}),
                                    rc_mapping={
                                        200: 'ExtendedCertificateAuthorityAccountInformation'
                                    }
                                )

                    class _configuration(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                        class _validation(CloudApiEndpoint):
                            def post(
                                self,
                                CertificateAuthorityAccountConfigurationRequest: caoperations_service.CertificateAuthorityAccountConfigurationRequest
                            ):
                                data = {**CertificateAuthorityAccountConfigurationRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountResponse',
                                        204: 'CertificateAuthorityAccountResponse'
                                    }
                                )

                    class _connection(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                        class _validation(CloudApiEndpoint):
                            def post(
                                self,
                                CertificateAuthorityTestConnectionRequest: caoperations_service.CertificateAuthorityTestConnectionRequest
                            ):
                                data = {**CertificateAuthorityTestConnectionRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountResponse'
                                    }
                                )

                    class _credentials(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                        class _validation(CloudApiEndpoint):
                            def post(
                                self,
                                CertificateAuthorityCredentialsRequest: caoperations_service.CertificateAuthorityCredentialsRequest
                            ):
                                data = {**CertificateAuthorityCredentialsRequest.dict()}

                                class Output(CloudApiOutputModel):
                                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse

                                return generate_output(
                                    output_cls=Output,
                                    response=self._post(data=data),
                                    rc_mapping={
                                        200: 'CertificateAuthorityAccountResponse'
                                    }
                                )

        class _certificateissuingtemplates(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def get(self, certificateAuthorityAccountId: UUID):
                data = {
                    'certificateAuthorityAccountId': certificateAuthorityAccountId,
                }

                class Output(CloudApiOutputModel):
                    CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse

                return generate_output(
                    output_cls=Output,
                    response=self._get(params=data),
                    rc_mapping={
                        200: 'CertificateIssuingTemplateResponse'
                    }
                )

            def post(self, CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest):
                data = {**CertificateIssuingTemplateRequest.dict()}

                class Output(CloudApiOutputModel):
                    CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse

                return generate_output(
                    output_cls=Output,
                    response=self._post(data=data),
                    rc_mapping={
                        201: 'CertificateIssuingTemplateResponse'
                    }
                )

            class _ID(CloudApiEndpoint):
                def delete(self):
                    class Output(CloudApiOutputModel):
                        CertificateIssuingTemplateDeleteResponse: caoperations_service.CertificateIssuingTemplateDeleteResponse

                    return generate_output(
                        output_cls=Output,
                        response=self._delete(params={}),
                        rc_mapping={
                            204: 'CertificateIssuingTemplateDeleteResponse'
                        }
                    )

                def get(self):
                    class Output(CloudApiOutputModel):
                        CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'CertificateIssuingTemplateInformation'
                        }
                    )

                def put(
                    self,
                    CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest
                ):
                    data = {**CertificateIssuingTemplateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation

                    return generate_output(
                        output_cls=Output,
                        response=self._put(data=data),
                        rc_mapping={
                            200: 'CertificateIssuingTemplateInformation',
                            202: 'CertificateIssuingTemplateInformation'
                        }
                    )

        class _certificaterequests(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.approval = self._approval(api_obj=self._api_obj, url=f'{self._url}/approval')
                self.approvalrequests = self._approvalrequests(
                    api_obj=self._api_obj,
                    url=f'{self._url}/approvalrequests'
                )
                self.approvalrules = self._approvalrules(api_obj=self._api_obj, url=f'{self._url}/approvalrules')

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            class _ID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.approval = self._approval(api_obj=self._api_obj, url=f'{self._url}/approval')

                class _approval(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def DECISION(self, decision: str):
                        return self._DECISION(api_obj=self._api_obj, url=f'{self._url}/{decision}')

                    class _DECISION(CloudApiEndpoint):
                        def post(self, ApprovalDecisionRequest: caoperations_service.ApprovalDecisionRequest):
                            data = {**ApprovalDecisionRequest.dict()}

                            class Output(CloudApiOutputModel):
                                CertificateRequestInformation: caoperations_service.CertificateRequestInformation

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data=data),
                                rc_mapping={
                                    200: 'CertificateRequestInformation'
                                }
                            )

            class _approval(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.bulk = self._bulk(api_obj=self._api_obj, url=f'{self._url}/bulk')

                class _bulk(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def DECISION(self, decision: str):
                        return self._DECISION(api_obj=self._api_obj, url=f'{self._url}/{decision}')

                    def OPERATIONID(self, operationid: str):
                        return self._OPERATIONID(api_obj=self._api_obj, url=f'{self._url}/{operationid}')

                    class _DECISION(CloudApiEndpoint):
                        def post(self, BulkApprovalRequest: caoperations_service.BulkApprovalRequest):
                            data = {**BulkApprovalRequest.dict()}

                            class Output(CloudApiOutputModel):
                                BulkApprovalResponse: caoperations_service.BulkApprovalResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._post(data=data),
                                rc_mapping={
                                    201: 'BulkApprovalResponse'
                                }
                            )

                    class _OPERATIONID(CloudApiEndpoint):
                        def get(self):
                            class Output(CloudApiOutputModel):
                                BulkApprovalStatusResponse: caoperations_service.BulkApprovalStatusResponse

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params={}),
                                rc_mapping={
                                    200: 'BulkApprovalStatusResponse'
                                }
                            )

            class _approvalrequests(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ENTITYID(self, entityid: str):
                    return self._ENTITYID(api_obj=self._api_obj, url=f'{self._url}/{entityid}')

                class _ENTITYID(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            ApprovalRequestInformation: caoperations_service.ApprovalRequestInformation

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'ApprovalRequestInformation'
                            }
                        )

            class _approvalrules(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self):
                    class Output(CloudApiOutputModel):
                        CertificateRequestApprovalRulesResponseOpenApi: caoperations_service.CertificateRequestApprovalRulesResponseOpenApi

                    return generate_output(
                        output_cls=Output,
                        response=self._get(params={}),
                        rc_mapping={
                            200: 'CertificateRequestApprovalRulesResponseOpenApi'
                        }
                    )

                def post(
                    self,
                    CertificateRequestApprovalRulesRequest: caoperations_service.CertificateRequestApprovalRulesRequest
                ):
                    data = {**CertificateRequestApprovalRulesRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateRequestApprovalRuleOpenApi: caoperations_service.CertificateRequestApprovalRuleOpenApi

                    return generate_output(
                        output_cls=Output,
                        response=self._post(data=data),
                        rc_mapping={
                            201: 'CertificateRequestApprovalRuleOpenApi'
                        }
                    )

                class _ID(CloudApiEndpoint):
                    def delete(self):
                        class Output(CloudApiOutputModel):
                            CertificateRequestApprovalRuleDeleteResponseOpenApi: caoperations_service.CertificateRequestApprovalRuleDeleteResponseOpenApi

                        return generate_output(
                            output_cls=Output,
                            response=self._delete(params={}),
                            rc_mapping={
                                200: 'CertificateRequestApprovalRuleDeleteResponseOpenApi'
                            }
                        )

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateRequestApprovalRuleOpenApi: caoperations_service.CertificateRequestApprovalRuleOpenApi

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateRequestApprovalRuleOpenApi'
                            }
                        )

                    def put(
                        self,
                        CertificateRequestApprovalRulesUpdateRequest: caoperations_service.CertificateRequestApprovalRulesUpdateRequest
                    ):
                        data = {**CertificateRequestApprovalRulesUpdateRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateRequestApprovalRuleOpenApi: caoperations_service.CertificateRequestApprovalRuleOpenApi

                        return generate_output(
                            output_cls=Output,
                            response=self._put(data=data),
                            rc_mapping={
                                200: 'CertificateRequestApprovalRuleOpenApi'
                            }
                        )

        class _certificates(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.revocations = self._revocations(api_obj=self._api_obj, url=f'{self._url}/revocations')

            class _revocations(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.approvalrules = self._approvalrules(api_obj=self._api_obj, url=f'{self._url}/approvalrules')

                class _approvalrules(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateRevocationApprovalRulesResponseOpenApi: caoperations_service.CertificateRevocationApprovalRulesResponseOpenApi

                        return generate_output(
                            output_cls=Output,
                            response=self._get(params={}),
                            rc_mapping={
                                200: 'CertificateRevocationApprovalRulesResponseOpenApi'
                            }
                        )

                    def post(
                        self,
                        CertificateRevocationApprovalRulesRequest: caoperations_service.CertificateRevocationApprovalRulesRequest
                    ):
                        data = {**CertificateRevocationApprovalRulesRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateRevocationApprovalRuleOpenApi: caoperations_service.CertificateRevocationApprovalRuleOpenApi

                        return generate_output(
                            output_cls=Output,
                            response=self._post(data=data),
                            rc_mapping={
                                201: 'CertificateRevocationApprovalRuleOpenApi'
                            }
                        )

                    class _ID(CloudApiEndpoint):
                        def delete(self):
                            class Output(CloudApiOutputModel):
                                CertificateRevocationApprovalRuleDeleteResponseOpenApi: caoperations_service.CertificateRevocationApprovalRuleDeleteResponseOpenApi

                            return generate_output(
                                output_cls=Output,
                                response=self._delete(params={}),
                                rc_mapping={
                                    200: 'CertificateRevocationApprovalRuleDeleteResponseOpenApi'
                                }
                            )

                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateRevocationApprovalRuleOpenApi: caoperations_service.CertificateRevocationApprovalRuleOpenApi

                            return generate_output(
                                output_cls=Output,
                                response=self._get(params={}),
                                rc_mapping={
                                    200: 'CertificateRevocationApprovalRuleOpenApi'
                                }
                            )

                        def put(
                            self,
                            CertificateRevocationApprovalRulesUpdateRequest: caoperations_service.CertificateRevocationApprovalRulesUpdateRequest
                        ):
                            data = {**CertificateRevocationApprovalRulesUpdateRequest.dict()}

                            class Output(CloudApiOutputModel):
                                CertificateRevocationApprovalRuleOpenApi: caoperations_service.CertificateRevocationApprovalRuleOpenApi

                            return generate_output(
                                output_cls=Output,
                                response=self._put(data=data),
                                rc_mapping={
                                    200: 'CertificateRevocationApprovalRuleOpenApi'
                                }
                            )
