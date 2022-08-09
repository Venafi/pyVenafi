from datetime import datetime

from pytpp.api.api_base import ResponseFactory, ResponseField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.plugins.properties.response_objects.dataclasses import ssh_dashboard
from typing import List


class _SshDashboard:
    def __init__(self, api_obj):
        self.CountAccessOrphan = self._CountAccessOrphan(api_obj=api_obj)
        self.CountKeysetsInError = self._CountKeysetsInError(api_obj=api_obj)
        self.CountNeedsActionFromMe = self._CountNeedsActionFromMe(api_obj=api_obj)
        self.CountNistNonComplaint = self._CountNistNonComplaint(api_obj=api_obj)
        self.CountPendingMyApprovalKeys = self._CountPendingMyApprovalKeys(api_obj=api_obj)
        self.CountPrivateKeyOrphans = self._CountPrivateKeyOrphans(api_obj=api_obj)
        self.CountRootAuthorization = self._CountRootAuthorization(api_obj=api_obj)
        self.CountSmallKeyLength = self._CountSmallKeyLength(api_obj=api_obj)
        self.CountTotal = self._CountTotal(api_obj=api_obj)
        self.CountUnknownClientAccess = self._CountUnknownClientAccess(api_obj=api_obj)
        self.CountUntrackedKeys = self._CountUntrackedKeys(api_obj=api_obj)
        self.CountUnusedAuthorizedKeys = self._CountUnusedAuthorizedKeys(api_obj=api_obj)
        self.GetCriticalAlertsPrefs = self._GetCriticalAlertsPrefs(api_obj=api_obj)
        self.KeyAlgorithms = self._KeyAlgorithms(api_obj=api_obj)
        self.KeyLengths = self._KeyLengths(api_obj=api_obj)
        self.PolicyViolations = self._PolicyViolations(api_obj=api_obj)
        self.Trends = self._Trends(api_obj=api_obj)
        self.TrustsPerUserKeyset = self._TrustsPerUserKeyset(api_obj=api_obj)

    class _CountAccessOrphan(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountAccessOrphan')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountKeysetsInError(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountKeysetsInError')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountNeedsActionFromMe(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountNeedsActionFromMe')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountNistNonComplaint(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountNistNonComplaint')

        def get(self):
            class Response(ApertureResponse):
                total: int = ResponseField(alias='total')
                all_codes: List[int] = ResponseField(alias='allCodes', default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get())

    class _CountPendingMyApprovalKeys(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountPendingMyApprovalKeys')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountPrivateKeyOrphans(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountPrivateKeyOrphans')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountRootAuthorization(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountRootAuthorization')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountSmallKeyLength(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountSmallKeyLength')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountTotal(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountTotal')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountUnknownClientAccess(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUnknownClientAccess')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountUntrackedKeys(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUntrackedKeys')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _CountUnusedAuthorizedKeys(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUnusedAuthorizedKeys')

        def get(self):
            class Response(ApertureResponse):
                value: int = ResponseField()

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='value')

    class _GetCriticalAlertsPrefs(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/GetCriticalAlertsPrefs')

        def get(self):
            class Response(ApertureResponse):
                hide_zeros: bool = ResponseField(alias='hideZeros')
                key_length: int = ResponseField(alias='keyLength')
                last_used: datetime = ResponseField(alias='lastUsed')
                has_permissions_to_lock: bool = ResponseField(alias='hasPermissionsToLock')

            return ResponseFactory(response_cls=Response, response=self._get())

    class _KeyAlgorithms(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/KeyAlgorithms')

        def get(self):
            class Response(ApertureResponse):
                records: List[ssh_dashboard.Record] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='records')

    class _KeyLengths(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/keylengths')

        def get(self):
            class Response(ApertureResponse):
                records: List[ssh_dashboard.Record] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='records')

    class _PolicyViolations(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/PolicyViolations')

        def get(self):
            class Response(ApertureResponse):
                policy_violations : List[ssh_dashboard.PolicyViolation] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='policy_violations')

    class _Trends(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/Trends')

        def get(self):
            class Response(ApertureResponse):
                trends: List[ssh_dashboard.Trend] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='trends')

    class _TrustsPerUserKeyset(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/TrustsPerUserKeyset')

        def get(self):
            class Response(ApertureResponse):
                records: List[ssh_dashboard.Record] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._get(), root_field='records')













