from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import certificate_service
from typing import Literal


class _certificate_service:
    def __init__(self, api_obj):
        self.admin = self._admin(api_obj=api_obj)
        self.outagedetection = self._outagedetection(api_obj=api_obj)
        self.v1 = self._v1(api_obj=api_obj)

    class _admin(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='admin')
            self.v1 = self._v1(api_obj=self._api_obj, url=f'{self._url}/v1')

        class _v1(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
                self.trustedauthorities = self._trustedauthorities(api_obj=self._api_obj, url=f'{self._url}/trustedauthorities')

            class _certificates(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.cacheload = self._cacheload(api_obj=self._api_obj, url=f'{self._url}/cacheload')

                class _cacheload(CloudApiEndpoint):
                    def post(self):
                        class Output(CloudApiOutputModel):
                            pass
                        return generate_output(output_cls=Output, response=self._post(data={}))

            class _trustedauthorities(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')

                class _certificates(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.cacheload = self._cacheload(api_obj=self._api_obj, url=f'{self._url}/cacheload')

                    def FINGERPRINT(self, fingerprint: str):
                        return self._FINGERPRINT(api_obj=self._api_obj, url=f'{self._url}/{fingerprint}')

                    def post(self):
                        class Output(CloudApiOutputModel):
                            pass
                        return generate_output(output_cls=Output, response=self._post(data={}))

                    class _FINGERPRINT(CloudApiEndpoint):
                        def delete(self):
                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

                    class _cacheload(CloudApiEndpoint):
                        def post(self):
                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._post(data={}))

    class _outagedetection(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='outagedetection')
            self.admin = self._admin(api_obj=self._api_obj, url=f'{self._url}/admin')
            self.v1 = self._v1(api_obj=self._api_obj, url=f'{self._url}/v1')

        class _admin(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.v1 = self._v1(api_obj=self._api_obj, url=f'{self._url}/v1')

            class _v1(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.companies = self._companies(api_obj=self._api_obj, url=f'{self._url}/companies')

                class _companies(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def COMPANYID(self, companyid: str):
                        return self._COMPANYID(api_obj=self._api_obj, url=f'{self._url}/{companyid}')

                    class _COMPANYID(CloudApiEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.companydomains = self._companydomains(api_obj=self._api_obj, url=f'{self._url}/companydomains')

                        class _companydomains(CloudApiEndpoint):
                            def get(self):
                                class Output(CloudApiOutputModel):
                                    AdminCompanyDomainResponse: certificate_service.AdminCompanyDomainResponse
                                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'AdminCompanyDomainResponse'})

        class _v1(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
                self.companydomains = self._companydomains(api_obj=self._api_obj, url=f'{self._url}/companydomains')

            class _certificates(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.imports = self._imports(api_obj=self._api_obj, url=f'{self._url}/imports')

                class _imports(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def ID(self, id: str):
                        return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                    def post(self, CertificateImportRequest: certificate_service.CertificateImportRequest):
                        data = {**CertificateImportRequest.dict()}

                        class Output(CloudApiOutputModel):
                            CertificateImportResponse: certificate_service.CertificateImportResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CertificateImportResponse'})

                    class _ID(CloudApiEndpoint):
                        def get(self):
                            class Output(CloudApiOutputModel):
                                CertificateImportStatusDetailResponse: certificate_service.CertificateImportStatusDetailResponse
                            return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CertificateImportStatusDetailResponse'})

            class _companydomains(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                def ID(self, id: str):
                    return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

                def get(self, status: Literal['AUTHORIZED', 'EXPIRED', 'PENDING']):
                    data = {
                        'status': status,
                    }

                    class Output(CloudApiOutputModel):
                        CompanyDomainResponse: certificate_service.CompanyDomainResponse
                    return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CompanyDomainResponse'})

                def post(self, CompanyDomainRequest: certificate_service.CompanyDomainRequest):
                    data = {**CompanyDomainRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CompanyDomainResponse: certificate_service.CompanyDomainResponse
                    return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'CompanyDomainResponse', 202: 'CompanyDomainResponse'})

                class _ID(CloudApiEndpoint):
                    def delete(self, retireCertificates: bool):
                        data = {
                            'retireCertificates': retireCertificates,
                        }

                        class Output(CloudApiOutputModel):
                            pass
                        return generate_output(output_cls=Output, response=self._delete(params=data))

                    def get(self):
                        class Output(CloudApiOutputModel):
                            CompanyDomainInformation: certificate_service.CompanyDomainInformation
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CompanyDomainInformation'})

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.certificateblocklist = self._certificateblocklist(api_obj=self._api_obj, url=f'{self._url}/certificateblocklist')
            self.certificates = self._certificates(api_obj=self._api_obj, url=f'{self._url}/certificates')
            self.companyproperties = self._companyproperties(api_obj=self._api_obj, url=f'{self._url}/companyproperties')
            self.trustedcacertificates = self._trustedcacertificates(api_obj=self._api_obj, url=f'{self._url}/trustedcacertificates')

        class _certificateblocklist(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def FINGERPRINT(self, fingerprint: str):
                return self._FINGERPRINT(api_obj=self._api_obj, url=f'{self._url}/{fingerprint}')

            def delete(self):
                class Output(CloudApiOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._delete(params={}))

            def get(self, limit: int, page: str):
                data = {
                    'limit': limit,
                    'page': page,
                }

                class Output(CloudApiOutputModel):
                    CertificateBlockListPageResponse: certificate_service.CertificateBlockListPageResponse
                return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'CertificateBlockListPageResponse'})

            def post(self, CertificateBlockListRequest: certificate_service.CertificateBlockListRequest):
                data = {**CertificateBlockListRequest.dict()}

                class Output(CloudApiOutputModel):
                    CertificateBlockListResponse: certificate_service.CertificateBlockListResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CertificateBlockListResponse', 201: 'CertificateBlockListResponse'})

            class _FINGERPRINT(CloudApiEndpoint):
                def delete(self):
                    class Output(CloudApiOutputModel):
                        pass
                    return generate_output(output_cls=Output, response=self._delete(params={}))

                def get(self):
                    class Output(CloudApiOutputModel):
                        str: str
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'str'})

        class _certificates(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            class _ID(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.encoded = self._encoded(api_obj=self._api_obj, url=f'{self._url}/encoded')

                class _encoded(CloudApiEndpoint):
                    def get(self, chainOrder: Literal['EE_FIRST', 'EE_ONLY', 'ROOT_FIRST'], format: Literal['DER', 'PEM']):
                        data = {
                            'chainOrder': chainOrder,
                            'format': format,
                        }

                        class Output(CloudApiOutputModel):
                            str: str
                        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'str'})

        class _companyproperties(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def ID(self, id: str):
                return self._ID(api_obj=self._api_obj, url=f'{self._url}/{id}')

            def TYPE(self, type: str):
                return self._TYPE(api_obj=self._api_obj, url=f'{self._url}/{type}')

            def get(self):
                class Output(CloudApiOutputModel):
                    CompanyPropertyResponse: certificate_service.CompanyPropertyResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CompanyPropertyResponse'})

            def post(self, CompanyPropertyRequest: certificate_service.CompanyPropertyRequest):
                data = {**CompanyPropertyRequest.dict()}

                class Output(CloudApiOutputModel):
                    CompanyPropertyInformation: certificate_service.CompanyPropertyInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'CompanyPropertyInformation'})

            class _ID(CloudApiEndpoint):
                def put(self, CompanyPropertyRequest: certificate_service.CompanyPropertyRequest):
                    data = {**CompanyPropertyRequest.dict()}

                    class Output(CloudApiOutputModel):
                        CompanyPropertyInformation: certificate_service.CompanyPropertyInformation
                    return generate_output(output_cls=Output, response=self._put(data=data), rc_mapping={200: 'CompanyPropertyInformation'})

            class _TYPE(CloudApiEndpoint):
                def get(self):
                    class Output(CloudApiOutputModel):
                        CompanyPropertyInformation: certificate_service.CompanyPropertyInformation
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'CompanyPropertyInformation'})

        class _trustedcacertificates(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.deletion = self._deletion(api_obj=self._api_obj, url=f'{self._url}/deletion')

            def FINGERPRINT(self, fingerprint: str):
                return self._FINGERPRINT(api_obj=self._api_obj, url=f'{self._url}/{fingerprint}')

            def get(self):
                class Output(CloudApiOutputModel):
                    pass
                return generate_output(output_cls=Output, response=self._get(params={}))

            def post(self, TrustedCACertificatesRequest: certificate_service.TrustedCACertificatesRequest):
                data = {**TrustedCACertificatesRequest.dict()}

                class Output(CloudApiOutputModel):
                    TrustedCACertificateResponse: certificate_service.TrustedCACertificateResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'TrustedCACertificateResponse', 201: 'TrustedCACertificateResponse'})

            class _FINGERPRINT(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.contents = self._contents(api_obj=self._api_obj, url=f'{self._url}/contents')

                def get(self):
                    class Output(CloudApiOutputModel):
                        ExtendedTrustedCACertificateInformation: certificate_service.ExtendedTrustedCACertificateInformation
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'ExtendedTrustedCACertificateInformation'})

                class _contents(CloudApiEndpoint):
                    def get(self, chainOrder: Literal['EE_FIRST', 'EE_ONLY', 'ROOT_FIRST'], format: Literal['DER', 'PEM']):
                        data = {
                            'chainOrder': chainOrder,
                            'format': format,
                        }

                        class Output(CloudApiOutputModel):
                            str: str
                        return generate_output(output_cls=Output, response=self._get(params=data), rc_mapping={200: 'str'})

            class _deletion(CloudApiEndpoint):
                def post(self, TrustedCACertificateDeletionRequest: certificate_service.TrustedCACertificateDeletionRequest):
                    data = {**TrustedCACertificateDeletionRequest.dict()}

                    class Output(CloudApiOutputModel):
                        pass
                    return generate_output(output_cls=Output, response=self._post(data=data))
