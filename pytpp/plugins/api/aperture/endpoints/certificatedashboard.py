from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.aperture.outputs import certificate_dashboard
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from typing import List


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

    class _GetCertificateKeyLength(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateKeyLength')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetCertificateIssuers(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateIssuers')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetCertificateSigningAlgorithms(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateSigningAlgorithms')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetCertificateValidityPeriods(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateValidityPeriods')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetValidationEndEntity(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationEndEntity')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetValidationChain(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationChain')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetCertificateExpireDates(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetCertificateExpireDates')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetValidationProtocols(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetValidationProtocols')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _GetProtectionStatus(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetProtectionStatus')

        def get(self):
            class Response(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='records')

    class _Trends(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/Trends')

        def get(self):
            class Response(ApertureOutputModel):
                trends: List[certificate_dashboard.Trend] = ApiField(default_factory=list)

            return generate_output(response_cls=Response, response=self._get(), root_field='trends')

    class _CountCertsWithStatus(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/CountCertsWithStatus')

        def get(self, status):
            params = {
                'status': status
            }

            class Response(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(response_cls=Response, response=self._get(params=params), root_field='value')

    class _GetTotalCount(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalCount')

        def get(self):
            class Response(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(response_cls=Response, response=self._get(), root_field='value')

    class _GetTotalDisabledCount(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalDisabledCount')

        def get(self):
            class Response(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(response_cls=Response, response=self._get(), root_field='value')

    class _GetTotalManagedCount(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/CertificateDashboard/GetTotalManagedCount')

        def get(self):
            class Response(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(response_cls=Response, response=self._get(), root_field='value')
