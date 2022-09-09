from datetime import datetime
from venafi.tpp.api.api_base import generate_output, ApiField
from venafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from venafi.tpp.plugins.api.aperture.models import ssh_dashboard
from typing import List


class _SshDashboard(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SshDashboard')
        self.CountAccessOrphan = self._CountAccessOrphan(api_obj=self._api_obj, url=f'{self._url}/CountAccessOrphan')
        self.CountKeysetsInError = self._CountKeysetsInError(api_obj=self._api_obj, url=f'{self._url}/CountKeysetsInError')
        self.CountNeedsActionFromMe = self._CountNeedsActionFromMe(api_obj=self._api_obj, url=f'{self._url}/CountNeedsActionFromMe')
        self.CountNistNonComplaint = self._CountNistNonComplaint(api_obj=self._api_obj, url=f'{self._url}/CountNistNonComplaint')
        self.CountPendingMyApprovalKeys = self._CountPendingMyApprovalKeys(api_obj=self._api_obj, url=f'{self._url}/CountPendingMyApprovalKeys')
        self.CountPrivateKeyOrphans = self._CountPrivateKeyOrphans(api_obj=self._api_obj, url=f'{self._url}/CountPrivateKeyOrphans')
        self.CountRootAuthorization = self._CountRootAuthorization(api_obj=self._api_obj, url=f'{self._url}/CountRootAuthorization')
        self.CountSmallKeyLength = self._CountSmallKeyLength(api_obj=self._api_obj, url=f'{self._url}/CountSmallKeyLength')
        self.CountTotal = self._CountTotal(api_obj=self._api_obj, url=f'{self._url}/CountTotal')
        self.CountUnknownClientAccess = self._CountUnknownClientAccess(api_obj=self._api_obj, url=f'{self._url}/CountUnknownClientAccess')
        self.CountUntrackedKeys = self._CountUntrackedKeys(api_obj=self._api_obj, url=f'{self._url}/CountUntrackedKeys')
        self.CountUnusedAuthorizedKeys = self._CountUnusedAuthorizedKeys(api_obj=self._api_obj, url=f'{self._url}/CountUnusedAuthorizedKeys')
        self.GetCriticalAlertsPrefs = self._GetCriticalAlertsPrefs(api_obj=self._api_obj, url=f'{self._url}/GetCriticalAlertsPrefs')
        self.KeyAlgorithms = self._KeyAlgorithms(api_obj=self._api_obj, url=f'{self._url}/KeyAlgorithms')
        self.KeyLengths = self._KeyLengths(api_obj=self._api_obj, url=f'{self._url}/keylengths')
        self.PolicyViolations = self._PolicyViolations(api_obj=self._api_obj, url=f'{self._url}/PolicyViolations')
        self.Trends = self._Trends(api_obj=self._api_obj, url=f'{self._url}/Trends')
        self.TrustsPerUserKeyset = self._TrustsPerUserKeyset(api_obj=self._api_obj, url=f'{self._url}/TrustsPerUserKeyset')

    class _CountAccessOrphan(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountKeysetsInError(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountNeedsActionFromMe(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountNistNonComplaint(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                total: int = ApiField(alias='total')
                all_codes: List[int] = ApiField(alias='allCodes', default_factory=list)

            return generate_output(output_cls=Output, response=self._get())

    class _CountPendingMyApprovalKeys(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountPrivateKeyOrphans(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountRootAuthorization(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountSmallKeyLength(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountTotal(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountUnknownClientAccess(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountUntrackedKeys(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _CountUnusedAuthorizedKeys(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                value: int = ApiField()

            return generate_output(output_cls=Output, response=self._get(), root_field='value')

    class _GetCriticalAlertsPrefs(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                hide_zeros: bool = ApiField(alias='hideZeros')
                key_length: int = ApiField(alias='keyLength')
                last_used: datetime = ApiField(alias='lastUsed')
                has_permissions_to_lock: bool = ApiField(alias='hasPermissionsToLock')

            return generate_output(output_cls=Output, response=self._get())

    class _KeyAlgorithms(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[ssh_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _KeyLengths(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[ssh_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')

    class _PolicyViolations(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                policy_violations: List[ssh_dashboard.PolicyViolation] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='policy_violations')

    class _Trends(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                trends: List[ssh_dashboard.Trend] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='trends')

    class _TrustsPerUserKeyset(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                records: List[ssh_dashboard.Record] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._get(), root_field='records')
