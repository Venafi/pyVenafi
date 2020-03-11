from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.certificate_dashboard import CertificateDashboard


class _CertificateDashboard:
    def __init__(self, aperture_obj):
        self.GetCertificateExpireDates = self._GetCertificateExpireDates(aperture_obj=aperture_obj)
        self.GetCertificateIssuers = self._GetCertificateIssuers(aperture_obj=aperture_obj)
        self.GetCertificateKeyLength = self._GetCertificateKeyLength(aperture_obj=aperture_obj)
        self.GetCertificateSigningAlgorithm = self._GetCertificateSigningAlgorithm(aperture_obj=aperture_obj)
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
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateKeyLength',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetCertificateIssuers(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateIssuers',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetCertificateSigningAlgorithms(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateSigningAlgorithms',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetCertificateValidityPeriods(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateValidityPeriods',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetValidationEndEntity(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationEndEntity',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetValidationChain(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationChain',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetCertificateExpireDates(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetCertificateExpireDates',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetValidationProtocols(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetValidationProtocols',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _GetProtectionStatus(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetProtectionStatus',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def records(self):
            return [CertificateDashboard.Record(record) for record in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _Trends(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/Trends',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def trends(self):
            return [CertificateDashboard.Trend(trend) for trend in self._from_json()]

        def get(self):
            self.json_response = self._get()
            return self

    class _CountCertsWithStatus(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/CountCertsWithStatus',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def value(self):
            return self._from_json()

        def get(self, status):
            params = {
                'status': status
            }
            self.json_response = self._get(params=params)
            return self

    class _GetTotalCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalCount',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def value(self):
            return self._from_json()

        def get(self):
            self.json_response = self._get()
            return self

    class _GetTotalDisabledCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalDisabledCount',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def value(self):
            return self._from_json()

        def get(self):
            self.json_response = self._get()
            return self

    class _GetTotalManagedCount(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/CertificateDashboard/GetTotalManagedCount',
                             valid_return_codes=[200])

        @property
        @json_response_property()
        def value(self):
            return self._from_json()

        def get(self):
            self.json_response = self._get()
            return self
