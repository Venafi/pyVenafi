from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import caoperations_service
from uuid import UUID


class _certificateauthorities(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/certificateauthorities')

    def CERTIFICATEAUTHORITY(self, certificateauthority: str):
        return self._CERTIFICATEAUTHORITY(api_obj=self._api_obj, url=f'{self._url}/{certificateauthority}')

    def get(self, includeSystemGenerated: bool):
        data = {
            'includeSystemGenerated': includeSystemGenerated,
        }

        class Output(CloudApiOutputModel):
            CertificateAuthorityResponse: caoperations_service.CertificateAuthorityResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateAuthorityResponse'})

    class _CERTIFICATEAUTHORITY(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.accounts = self._accounts(api_obj=self._api_obj, url=f'{self._url}/accounts')

        class _accounts(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.configuration = self._configuration(api_obj=self._api_obj, url=f'{self._url}/configuration')
                self.connection = self._connection(api_obj=self._api_obj, url=f'{self._url}/connection')
                self.credentials = self._credentials(api_obj=self._api_obj, url=f'{self._url}/credentials')

            def ACCOUNTID(self, accountid: str):
                return self._ACCOUNTID(api_obj=self._api_obj, url=f'{self._url}/{accountid}')

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def get(self, edgeInstanceId: UUID, includeObsoleteOptionsDetails: bool, includeOptionsDetails: bool, reloadOptionsDetails: bool):
                data = {
                    'edgeInstanceId': edgeInstanceId,
                    'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                    'includeOptionsDetails': includeOptionsDetails,
                    'reloadOptionsDetails': reloadOptionsDetails,
                }

                class Output(CloudApiOutputModel):
                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

            def post(self, CertificateAuthorityAccountRequest: caoperations_service.CertificateAuthorityAccountRequest):
                data = {**CertificateAuthorityAccountRequest.dict()}

                class Output(CloudApiOutputModel):
                    CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityAccountResponse', 202: 'CertificateAuthorityAccountResponse'})

            class _ACCOUNTID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.domains = self._domains(api_obj=self._api_obj, url=f'{self._url}/domains')
                    self.importoptions = self._importoptions(api_obj=self._api_obj, url=f'{self._url}/importoptions')
                    self.operations = self._operations(api_obj=self._api_obj, url=f'{self._url}/operations')
                    self.productoptions = self._productoptions(api_obj=self._api_obj, url=f'{self._url}/productoptions')

                class _domains(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                    def post(self, CertificateAuthorityAccountDomainRequest: caoperations_service.CertificateAuthorityAccountDomainRequest):
                        data = {**CertificateAuthorityAccountDomainRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                    class _ID(CloudApiEndpoint):
                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateAuthorityAccountDomainInformation: caoperations_service.CertificateAuthorityAccountDomainInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountDomainInformation'})

                class _importoptions(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountImportOptionResponse: caoperations_service.CertificateAuthorityAccountImportOptionResponse
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityAccountImportOptionResponse'})

                    def post(self, CertificateAuthorityAccountImportOptionRequest: caoperations_service.CertificateAuthorityAccountImportOptionRequest):
                        data = {**CertificateAuthorityAccountImportOptionRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityImportOptionInformation'})

                    class _ID(CloudApiEndpoint):
                        def delete(self):
                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateAuthorityImportOptionInformation: caoperations_service.CertificateAuthorityImportOptionInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityImportOptionInformation'})

                class _operations(CloudApiEndpoint):
                    def post(self, CaOperationRequest: caoperations_service.CaOperationRequest):
                        data = {**CaOperationRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountInformation: caoperations_service.CertificateAuthorityAccountInformation
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountInformation'})

                class _productoptions(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.testissuance = self._testissuance(api_obj=self._api_obj, url=f'{self._url}/testissuance')

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionResponse'})

                    def post(self, CertificateAuthorityProductOptionRequest: caoperations_service.CertificateAuthorityProductOptionRequest):
                        data = {**CertificateAuthorityProductOptionRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation
                            CertificateAuthorityProductOptionResponse: caoperations_service.CertificateAuthorityProductOptionResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateAuthorityProductOptionInformation', 202: 'CertificateAuthorityProductOptionResponse'})

                    class _ID(CloudApiEndpoint):
                        def delete(self):
                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateAuthorityProductOptionInformation: caoperations_service.CertificateAuthorityProductOptionInformation
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionInformation'})

                    class _testissuance(CloudApiEndpoint):
                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateAuthorityProductOptionsTestIssuanceResultsResponse: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceResultsResponse
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateAuthorityProductOptionsTestIssuanceResultsResponse'})

                        def post(self, CertificateAuthorityProductOptionsTestIssuanceRequest: caoperations_service.CertificateAuthorityProductOptionsTestIssuanceRequest):
                            data = {**CertificateAuthorityProductOptionsTestIssuanceRequest.dict()}

                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._post(data=data))

            class _ID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.certificateimportstatus = self._certificateimportstatus(
                        api_obj=self._api_obj, url=f'{self._url}/certificateimportstatus')
                    self.issuingrules = self._issuingrules(api_obj=self._api_obj, url=f'{self._url}/issuingrules')

                def delete(self):
                    class Output(CloudApiOutputModel):
                        CertificateAuthorityAccountDeleteResponse: caoperations_service.CertificateAuthorityAccountDeleteResponse
                    return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'CertificateAuthorityAccountDeleteResponse'})

                def get(self, includeObsoleteOptionsDetails: bool, includeOptionsDetails: bool, reloadAccountDetails: bool, reloadOptionsDetails: bool):
                    data = {
                        'includeObsoleteOptionsDetails': includeObsoleteOptionsDetails,
                        'includeOptionsDetails': includeOptionsDetails,
                        'reloadAccountDetails': reloadAccountDetails,
                        'reloadOptionsDetails': reloadOptionsDetails,
                    }

                    class Output(CloudApiOutputModel):
                        ExtendedCertificateAuthorityAccountInformation: caoperations_service.ExtendedCertificateAuthorityAccountInformation
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'ExtendedCertificateAuthorityAccountInformation'})

                def put(self, CertificateAuthorityAccountUpdateRequest: caoperations_service.CertificateAuthorityAccountUpdateRequest):
                    data = {**CertificateAuthorityAccountUpdateRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                    return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

                class _certificateimportstatus(CloudApiEndpoint):
                    def put(self, CertificateImportRequest: caoperations_service.CertificateImportRequest):
                        data = {**CertificateImportRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={204: 'CertificateAuthorityAccountResponse'})

                class _issuingrules(CloudApiEndpoint):
                    def get(self):
                        class Output(CloudApiOutputModel):
                            CertificateIssuingTemplateRulesInformation: caoperations_service.CertificateIssuingTemplateRulesInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateIssuingTemplateRulesInformation'})

            class _configuration(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(CloudApiEndpoint):
                    def post(self, CertificateAuthorityAccountConfigurationRequest: caoperations_service.CertificateAuthorityAccountConfigurationRequest):
                        data = {**CertificateAuthorityAccountConfigurationRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse', 204: 'CertificateAuthorityAccountResponse'})

            class _connection(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(CloudApiEndpoint):
                    def post(self, CertificateAuthorityTestConnectionRequest: caoperations_service.CertificateAuthorityTestConnectionRequest):
                        data = {**CertificateAuthorityTestConnectionRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})

            class _credentials(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.validation = self._validation(api_obj=self._api_obj, url=f'{self._url}/validation')

                class _validation(CloudApiEndpoint):
                    def post(self, CertificateAuthorityCredentialsRequest: caoperations_service.CertificateAuthorityCredentialsRequest):
                        data = {**CertificateAuthorityCredentialsRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateAuthorityAccountResponse: caoperations_service.CertificateAuthorityAccountResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateAuthorityAccountResponse'})


class _certificateissuingtemplates(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/certificateissuingtemplates')

    def ID(self, id: str):
        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

    def get(self, certificateAuthorityAccountId: UUID):
        data = {
            'certificateAuthorityAccountId': certificateAuthorityAccountId,
        }

        class Output(CloudApiOutputModel):
            CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse
        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateIssuingTemplateResponse'})

    def post(self, CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest):
        data = {**CertificateIssuingTemplateRequest.dict()}

        class Output(CloudApiOutputModel):
            CertificateIssuingTemplateResponse: caoperations_service.CertificateIssuingTemplateResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateIssuingTemplateResponse'})

    class _ID(CloudApiEndpoint):
        def delete(self):
            class Output(CloudApiOutputModel):
                CertificateIssuingTemplateDeleteResponse: caoperations_service.CertificateIssuingTemplateDeleteResponse
            return generate_output(output_cls=Output, response=self._delete(params={}), rc_mapping={204: 'CertificateIssuingTemplateDeleteResponse'})

        def get(self):
            class Output(CloudApiOutputModel):
                CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation
            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateIssuingTemplateInformation'})

        def put(self, CertificateIssuingTemplateRequest: caoperations_service.CertificateIssuingTemplateRequest):
            data = {**CertificateIssuingTemplateRequest.dict()}

            class Output(CloudApiOutputModel):
                CertificateIssuingTemplateInformation: caoperations_service.CertificateIssuingTemplateInformation
            return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'CertificateIssuingTemplateInformation', 202: 'CertificateIssuingTemplateInformation'})


class _builtinca(CloudApiEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='builtinca')
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
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})

    class _cachain(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def CANAME(self, caname: str):
            return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

        class _CANAME(CloudApiEndpoint):
            def get(self):
                class Output(CloudApiOutputModel):
                    str: str
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})

    class _crl(CloudApiEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def CANAME(self, caname: str):
            return self._CANAME(api_obj=self._api_obj, url=f'{self._url}/{caname}')

        class _CANAME(CloudApiEndpoint):
            def get(self):
                class Output(CloudApiOutputModel):
                    str: str
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})
