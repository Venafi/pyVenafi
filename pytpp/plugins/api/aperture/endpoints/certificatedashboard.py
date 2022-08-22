from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.aperture.models import certificate_dashboard
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from typing import List


class _CertificateDashboard(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/CertificateDashboard')
        self.GetCertificateExpireDates = self._GetCertificateExpireDates(api_obj=self._api_obj, url=f'{self._url}/GetCertificateExpireDates')
        self.GetCertificateIssuers = self._GetCertificateIssuers(api_obj=self._api_obj, url=f'{self._url}/GetCertificateIssuers')
        self.GetCertificateKeyLength = self._GetCertificateKeyLength(api_obj=self._api_obj, url=f'{self._url}/GetCertificateKeyLength')
        self.GetCertificateSigningAlgorithms = self._GetCertificateSigningAlgorithms(api_obj=self._api_obj, url=f'{self._url}/GetCertificateSigningAlgorithms')
        self.GetCertificateValidityPeriods = self._GetCertificateValidityPeriods(api_obj=self._api_obj, url=f'{self._url}/GetCertificateValidityPeriods')
        self.GetProtectionStatus = self._GetProtectionStatus(api_obj=self._api_obj, url=f'{self._url}/GetProtectionStatus')
        self.GetValidationChain = self._GetValidationChain(api_obj=self._api_obj, url=f'{self._url}/GetValidationChain')
        self.GetValidationEndEntity = self._GetValidationEndEntity(api_obj=self._api_obj, url=f'{self._url}/GetValidationEndEntity')
        self.GetValidationProtocols = self._GetValidationProtocols(api_obj=self._api_obj, url=f'{self._url}/GetValidationProtocols')
        self.Trends = self._Trends(api_obj=self._api_obj, url=f'{self._url}/Trends')
        self.CountCertsWithStatus = self._CountCertsWithStatus(api_obj=self._api_obj, url=f'{self._url}/CountCertsWithStatus')
        self.GetTotalCount = self._GetTotalCount(api_obj=self._api_obj, url=f'{self._url}/GetTotalCount')
        self.GetTotalDisabledCount = self._GetTotalDisabledCount(api_obj=self._api_obj, url=f'{self._url}/GetTotalDisabledCount')
        self.GetTotalManagedCount = self._GetTotalManagedCount(api_obj=self._api_obj, url=f'{self._url}/GetTotalManagedCount')

    class _GetCertificateKeyLength(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetCertificateIssuers(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetCertificateSigningAlgorithms(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetCertificateValidityPeriods(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetValidationEndEntity(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetValidationChain(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetCertificateExpireDates(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetValidationProtocols(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _GetProtectionStatus(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[certificate_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _Trends(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                trends: List[certificate_dashboard.Trend] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='trends')

    class _CountCertsWithStatus(ApertureEndpoint):
        def get(self, status):
            params = {
                'status': status
            }

            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(params=params), root_field='value')

    class _GetTotalCount(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _GetTotalDisabledCount(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _GetTotalManagedCount(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')
