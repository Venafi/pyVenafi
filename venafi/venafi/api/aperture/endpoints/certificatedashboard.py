from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.certificate_dashboard import CertificateDashboard


class _CertificateDashboard:
    def __init__(self, aperture_obj):
        self.GetCertificateExpireDates = self._GetCertificateExpireDates(aperture_obj=aperture_obj)
        self.GetCertificateIssuers = self._GetCertificateIssuers(aperture_obj=aperture_obj)
        self.GetCertificateKeyLength = self._GetCertificateKeyLength(aperture_obj=aperture_obj)
        self.GetCertificateSigningAlgorithms = self._GetCertificateSigningAlgorithms(aperture_obj=aperture_obj)
        self.GetCertificateValidityPeriods = self._GetCertificateValidityPeriods(aperture_obj=aperture_obj)
        self.GetProtectionStatus = self._GetProtectionStatus(aperture_obj=aperture_obj)
        self.GetValidationChain = self._GetValidationChain(aperture_obj=aperture_obj)
        self.GetValidationEndEntity = self._GetValidationEndEntity(aperture_obj=aperture_obj)
        self.GetValidationProtocols = self._GetValidationProtocols(aperture_obj=aperture_obj)
        self.Trends = self._Trends(aperture_obj=aperture_obj)
        self.CountCertsWithStatus = self._CountCertsWithStatus(aperture_obj=aperture_obj)
        self.GetTotalCount = self._GetTotalCount(aperture_obj=aperture_obj)
        self.GetTotalDisabledCount = self._GetTotalDisabledCount(aperture_obj=aperture_obj)
        self.GetTotalManagedCount = self._GetTotalManagedCount(aperture_obj=aperture_obj)

    class _GetCertificateKeyLength(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateKeyLength')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetCertificateIssuers(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateIssuers')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetCertificateSigningAlgorithms(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateSigningAlgorithms')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetCertificateValidityPeriods(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateValidityPeriods')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetValidationEndEntity(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationEndEntity')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetValidationChain(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationChain')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetCertificateExpireDates(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateExpireDates')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetValidationProtocols(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationProtocols')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetProtectionStatus(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetProtectionStatus')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def records(self):
                    return [CertificateDashboard.Record(record) for record in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Trends(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/Trends')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def trends(self):
                    return [CertificateDashboard.Trend(trend) for trend in self._from_json()]
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _CountCertsWithStatus(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/CountCertsWithStatus')

        def get(self, status):
            params = {
                'status': status
            }
            
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def value(self):
                    return self._from_json()
            
            return _Response(
                response=self._get(params=params),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetTotalCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalCount')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def value(self):
                    return self._from_json()
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetTotalDisabledCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalDisabledCount')

        def get(self):
            
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def value(self):
                    return self._from_json()
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetTotalManagedCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalManagedCount')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def value(self):
                    return self._from_json()
            
            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )
