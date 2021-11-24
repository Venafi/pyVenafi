from pytpp.api.api_base import api_response_property
from pytpp.plugins.api.api_base import API, APIResponse
from pytpp.plugins.properties.response_objects.ssh_dashboard import SshDashboard


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

    class _CountAccessOrphan(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountAccessOrphan')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountKeysetsInError(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountKeysetsInError')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountNeedsActionFromMe(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountNeedsActionFromMe')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountNistNonComplaint(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountNistNonComplaint')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def total(self):
                    return self._from_json(key='total')

                @property
                @api_response_property()
                def all_codes(self):
                    return self._from_json(key='allCodes')

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountPendingMyApprovalKeys(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountPendingMyApprovalKeys')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountPrivateKeyOrphans(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountPrivateKeyOrphans')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountRootAuthorization(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountRootAuthorization')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountSmallKeyLength(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountSmallKeyLength')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountTotal(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountTotal')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountUnknownClientAccess(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUnknownClientAccess')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountUntrackedKeys(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUntrackedKeys')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _CountUnusedAuthorizedKeys(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/CountUnusedAuthorizedKeys')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def value(self):
                    return self._from_json()

            return _Response(response=self._get(), api_source=self._api_source)

    class _GetCriticalAlertsPrefs(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/GetCriticalAlertsPrefs')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def hide_zeros(self):
                    return self._from_json(key='hideZeros')

                @property
                @api_response_property()
                def key_length(self):
                    return self._from_json(key='keyLength')

                @property
                @api_response_property()
                def last_used(self):
                    return self._from_json(key='lastUsed')

                @property
                @api_response_property()
                def has_permissions_to_lock(self):
                    return self._from_json(key='hasPermissionsToLock')

            return _Response(response=self._get(), api_source=self._api_source)

    class _KeyAlgorithms(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/KeyAlgorithms')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [SshDashboard.Record(record) for record in self._from_json()]

            return _Response(response=self._get(), api_source=self._api_source)

    class _KeyLengths(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/keylengths')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [SshDashboard.Record(record) for record in self._from_json()]

            return _Response(response=self._get(), api_source=self._api_source)

    class _PolicyViolations(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/PolicyViolations')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def policy_violations(self):
                    return [SshDashboard.PolicyViolation(violation) for violation in self._from_json()]

            return _Response(response=self._get(), api_source=self._api_source)

    class _Trends(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/Trends')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def trends(self):
                    return [SshDashboard.Trend(trend) for trend in self._from_json()]

            return _Response(response=self._get(), api_source=self._api_source)

    class _TrustsPerUserKeyset(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SshDashboard/TrustsPerUserKeyset')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def records(self):
                    return [SshDashboard.Record(record) for record in self._from_json()]

            return _Response(response=self._get(), api_source=self._api_source)













