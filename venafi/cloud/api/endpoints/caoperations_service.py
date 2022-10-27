from __future__ import annotations
from venafi.cloud.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output
from venafi.cloud.api.models import caoperations_service
from uuid import UUID


class _certificateissuingtemplates(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/certificateissuingtemplates')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, certificateAuthorityAccountId: UUID):
        data = {
            'certificateAuthorityAccountId': certificateAuthorityAccountId,
        }

        class Output(VaasSdkOutputModel):
            CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateIssuingTemplateResponse'})

    def post(self, CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest):
        data = {**CertificateIssuingTemplateRequest.dict()}

        class Output(VaasSdkOutputModel):
            CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateIssuingTemplateResponse'})

    class _ID(VaasSdkEndpoint):
        def get(self):
            class Output(VaasSdkOutputModel):
                CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateIssuingTemplateInformation'})

        def put(self, CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest):
            data = {**CertificateIssuingTemplateRequest.dict()}

            class Output(VaasSdkOutputModel):
                CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'CertificateIssuingTemplateInformation', 202: 'CertificateIssuingTemplateInformation'})

        def delete(self):
            class Output(VaasSdkOutputModel):
                CertificateIssuingTemplateDeleteResponse: caoperations_service.CertificateIssuingTemplateDeleteResponse
            return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'CertificateIssuingTemplateDeleteResponse'})


class _certificateauthorities(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/certificateauthorities')

    def CERTIFICATEAUTHORITY(self, certificateauthority: str):
        return self._CERTIFICATEAUTHORITY(api_obj=self._api_obj, url=f'{self._url}/{certificateauthority}')

    def get(self, includeSystemGenerated: bool):
        data = {
            'includeSystemGenerated': includeSystemGenerated,
        }

        class Output(VaasSdkOutputModel):
            CertificateAuthorityResponse: caoperations_service.CertificateAuthorityResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateAuthorityResponse'})

    class _CERTIFICATEAUTHORITY(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.accounts = self._accounts(api_obj=self._api_obj, url=f'{self._url}/accounts')

        class _accounts(VaasSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.connection = self._connection(api_obj=self._api_obj, url=f'{self._url}/connection')
                self.credentials = self._credentials(api_obj=self._api_obj, url=f'{self._url}/credentials')
                self.configuration = self._configuration(api_obj=self._api_obj, url=f'{self._url}/configuration')

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def ACCOUNTID(self, accountid: str):
                return self._ACCOUNTID(api_obj=self._api_obj, url=f'{self._url}/{accountid}')

            def get(self, includeOptionsDetails: bool, reloadOptionsDetails: bool, includeObsoleteOptionsDetails: bool, edgeInstanceId: UUID):
                data = {
                    'includeOptionsDetails': includeOptionsDetails,
                    'reloadOptionsDetails': reloadOptionsDetails,
                    'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                    'edgeInstanceId': edgeInstanceId,
                }

                class Output(VaasSdkOutputModel):
                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

            def post(self, CertificateAuthorityAccountRequest: caoperations_service.CertificateAuthorityAccountRequest):
                data = {**CertificateAuthorityAccountRequest.dict()}

                class Output(VaasSdkOutputModel):
                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityAccountResponse', 202: 'CertificateAuthorityAccountResponse'})

            class _ID(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.certificateimportstatus = self._certificateimportstatus(
                        api_obj=self._api_obj, url=f'{self._url}/certificateimportstatus')
                    self.issuingrules = self._issuingrules(api_obj=self._api_obj, url=f'{self._url}/issuingrules')

                def get(self, includeOptionsDetails: bool, reloadOptionsDetails: bool, includeObsoleteOptionsDetails: bool, reloadAccountDetails: bool):
                    data = {
                        'includeOptionsDetails': includeOptionsDetails,
                        'reloadOptionsDetails': reloadOptionsDetails,
                        'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                        'reloadAccountDetails': reloadAccountDetails,
                    }

                    class Output(VaasSdkOutputModel):
                        ExtendedCertificateAuthorityAccountInformation: caoperations_service.ExtendedCertificateAuthorityAccountInformation
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ExtendedCertificateAuthorityAccountInformation'})

                def put(self, CertificateAuthorityAccountUpdateRequest: caoperations_service.CertificateAuthorityAccountUpdateRequest):
                    data = {**CertificateAuthorityAccountUpdateRequest.dict()}

                    class Output(VaasSdkOutputModel):
                        CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                    return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

                def delete(self):
                    class Output(VaasSdkOutputModel):
                        CertificateAuthorityAccountDeleteResponse: caoperations_service.CertificateAuthorityAccountDeleteResponse
                    return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'CertificateAuthorityAccountDeleteResponse'})

                class _certificateimportstatus(VaasSdkEndpoint):
                    def put(self, CertificateImportRequest: caoperations_service.CertificateImportRequest):
                        data = {**CertificateImportRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={204: 'CertificateAuthorityAccountResponse'})

                class _issuingrules(VaasSdkEndpoint):
                    def get(self):
                        class Output(VaasSdkOutputModel):
                            CertificateIssuingTemplateRulesInformation: caoperations_service.CertificateIssuingTemplateRulesInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateIssuingTemplateRulesInformation'})

            class _connection(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(VaasSdkEndpoint):
                    def post(self, CertificateAuthorityTestConnectionRequest: caoperations_service.CertificateAuthorityTestConnectionRequest):
                        data = {**CertificateAuthorityTestConnectionRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

            class _credentials(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(VaasSdkEndpoint):
                    def post(self, CertificateAuthorityCredentialsRequest: caoperations_service.CertificateAuthorityCredentialsRequest):
                        data = {**CertificateAuthorityCredentialsRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

            class _configuration(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(VaasSdkEndpoint):
                    def post(self, CertificateAuthorityAccountConfigurationRequest: caoperations_service.CertificateAuthorityAccountConfigurationRequest):
                        data = {**CertificateAuthorityAccountConfigurationRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse', 204: 'CertificateAuthorityAccountResponse'})

            class _ACCOUNTID(VaasSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.domains = self._domains(api_obj=self._api_obj, url=f'{self._url}/domains')
                    self.productoptions = self._productoptions(api_obj=self._api_obj, url=f'{self._url}/productoptions')
                    self.importoptions = self._importoptions(api_obj=self._api_obj, url=f'{self._url}/importoptions')
                    self.operations = self._operations(api_obj=self._api_obj, url=f'{self._url}/operations')

                class _domains(VaasSdkEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                    def post(self, CertificateAuthorityAccountDomainRequest: caoperations_service.CertificateAuthorityAccountDomainRequest):
                        data = {**CertificateAuthorityAccountDomainRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                    class _ID(VaasSdkEndpoint):
                        def get(self):
                            class Output(VaasSdkOutputModel):
                                CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                class _productoptions(VaasSdkEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.testissuance = self._testissuance(api_obj=self._api_obj, url=f'{self._url}/testissuance')

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionResponse'})

                    def post(self, CertificateAuthorityProductOptionRequest: caoperations_service.CertificateAuthorityProductOptionRequest):
                        data = {**CertificateAuthorityProductOptionRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation
                            CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityProductOptionInformation', 202: 'CertificateAuthorityProductOptionResponse'})

                    class _ID(VaasSdkEndpoint):
                        def get(self):
                            class Output(VaasSdkOutputModel):
                                CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionInformation'})

                        def delete(self):
                            class Output(VaasSdkOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

                    class _testissuance(VaasSdkEndpoint):
                        def get(self):
                            class Output(VaasSdkOutputModel):
                                CertificateAuthorityProductOptionsTestIssuanceResultsResponse: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceResultsResponse
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionsTestIssuanceResultsResponse'})

                        def post(self, CertificateAuthorityProductOptionsTestIssuanceRequest: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceRequest):
                            data = {**CertificateAuthorityProductOptionsTestIssuanceRequest.dict()}

                            class Output(VaasSdkOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._post(data=data))

                class _importoptions(VaasSdkEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountImportOptionResponse: caoperations_service.CertificateAuthorityAccountImportOptionResponse
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountImportOptionResponse'})

                    def post(self, CertificateAuthorityAccountImportOptionRequest: caoperations_service.CertificateAuthorityAccountImportOptionRequest):
                        data = {**CertificateAuthorityAccountImportOptionRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityImportOptionInformation'})

                    class _ID(VaasSdkEndpoint):
                        def get(self):
                            class Output(VaasSdkOutputModel):
                                CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityImportOptionInformation'})

                        def delete(self):
                            class Output(VaasSdkOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

                class _operations(VaasSdkEndpoint):
                    def post(self, CaOperationRequest: caoperations_service.CaOperationRequest):
                        data = {**CaOperationRequest.dict()}

                        class Output(VaasSdkOutputModel):
                            CertificateAuthorityAccountInformation: caoperations_service.CertificateAuthorityAccountInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountInformation'})


class _builtinca(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='builtinca')
        self.crl = self._crl(api_obj=self._api_obj, url=f'{self._url}/crl')
        self.ca = self._ca(api_obj=self._api_obj, url=f'{self._url}/ca')
        self.cachain = self._cachain(api_obj=self._api_obj, url=f'{self._url}/cachain')

    class _crl(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def CANAME(self, caname: str):
            return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

        class _CANAME(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    str: str
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})

    class _ca(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def CANAME(self, caname: str):
            return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

        class _CANAME(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    str: str
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})

    class _cachain(VaasSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def CANAME(self, caname: str):
            return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

        class _CANAME(VaasSdkEndpoint):
            def get(self):
                class Output(VaasSdkOutputModel):
                    str: str
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})
