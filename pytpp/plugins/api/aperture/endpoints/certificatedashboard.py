from pytpp.plugins.api.api_base import API, APIResponse, api_response_property
from pytpp.plugins.properties.response_objects.certificate_dashboard import CertificateDashboard


class _CertificateDashboard:
    def __init__(self, api_obj):
        self.GetCertificateExpireDates = self._GetCertificateExpireDates(api_obj=api_obj)
        self.GetCertificateIssuers = self._GetCertificateIssuers(api_obj=api_obj)
        self.GetCertificateKeyLength = self._GetCertificateKeyLength(api_obj=api_obj)
        self.GetCertificateSigningAlgorithms = self._GetCertificateSigningAlgorithms(api_obj=api_obj)
        self.GetCertificateValidityPeriods = self._GetCertificateValidityPeriods(api_obj=api_obj)
        self.GetProtectionStatus = self._GetProtectionStatus(api_obj=api_obj)
        self.GetValidationChain = self._GetValidationChain(api_obj=api_obj)
        self.GetValidationEndEntity = self._GetValidationEndEntity(api_obj=api_obj)
        self.GetValidationProtocols = self._GetValidationProtocols(api_obj=api_obj)
        self.Trends = self._Trends(api_obj=api_obj)
        self.CountCertsWithStatus = self._CountCertsWithStatus(api_obj=api_obj)
        self.GetTotalCount = self._GetTotalCount(api_obj=api_obj)
        self.GetTotalDisabledCount = self._GetTotalDisabledCount(api_obj=api_obj)
        self.GetTotalManagedCount = self._GetTotalManagedCount(api_obj=api_obj)

    class _GetCertificateKeyLength(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateKeyLength')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetCertificateIssuers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateIssuers')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetCertificateSigningAlgorithms(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateSigningAlgorithms')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetCertificateValidityPeriods(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateValidityPeriods')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetValidationEndEntity(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationEndEntity')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetValidationChain(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationChain')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetCertificateExpireDates(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateExpireDates')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetValidationProtocols(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationProtocols')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetProtectionStatus(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetProtectionStatus')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _Trends(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/Trends')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def trends(self):
                    return [CertificateDashboard.Trend(trend) for trend in self._from_json()]
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _CountCertsWithStatus(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/CountCertsWithStatus')

        def get(self, status):
            params = {
                'status': status
            }
            
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()
            
            return Response(response_cls=Response, response=self._get(params=params), api_source=self._api_source)

    class _GetTotalCount(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalCount')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetTotalDisabledCount(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalDisabledCount')

        def get(self):
            
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)

    class _GetTotalManagedCount(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalManagedCount')

        def get(self):
            class Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()
            
            return Response(response_cls=Response, response=self._get(), api_source=self._api_source)
