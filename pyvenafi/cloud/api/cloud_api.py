from pyvenafi.cloud.api.session import Session
from pyvenafi.cloud.api.endpoints.account_service import (
    _teams, _users, _preferences, _useraccounts, _notifications, _ssoconfigurations, 
    _dataencryptionkeys
)
from pyvenafi.cloud.api.endpoints.activitylog_service import (
    _activitytypes, _activitylogsearch
)
from pyvenafi.cloud.api.endpoints.caoperations_service import (
    _builtinca, _certificateissuingtemplates, _certificateauthorities
)
from pyvenafi.cloud.api.endpoints.connectors_service import (
    _connectors
)
from pyvenafi.cloud.api.endpoints.edgemanagement_service import (
    _pairingcodes, _edgeworkers, _edgeinstances, _billofmaterials, _edgeencryptionkeys
)
from pyvenafi.cloud.api.endpoints.integrations_service import (
    _environments, _integrationservices, _integrationservicesaggregates
)
from pyvenafi.cloud.api.endpoints.outagedetection_service import (
    _outagedetection
)
from pyvenafi.cloud.api.endpoints.provisioning_service import (
    _machines, _machinesearch, _machinetypes, _machineidentities, _machineidentitysearch
)


class CloudApi:
    def __init__(self, server: str, api_key: str, proxies: dict = None, verify_ssl: bool = False,
                 connection_timeout: float = None, read_timeout: float = None):
        self._api_key = api_key
        self._proxies = proxies
        self._verify_ssl = verify_ssl
        self._connection_timeout = connection_timeout
        self._read_timeout = read_timeout
        self._scheme = 'https'

        # region Authentication
        self._base_url = f'{self._scheme}://{server}'
        self._app_url = self._base_url
        self._session = Session(
            headers={
                'Content-Type': 'application/json',
                'tppl-api-key': api_key
            },
            proxies=self._proxies,
            verify_ssl=verify_ssl,
            connection_timeout=connection_timeout,
            read_timeout=read_timeout
        )
        # endregion Authentication

        # region Endpoints
        self.activitylogsearch = _activitylogsearch(self)
        self.activitytypes = _activitytypes(self)
        self.billofmaterials = _billofmaterials(self)
        self.builtinca = _builtinca(self)
        self.certificateauthorities = _certificateauthorities(self)
        self.certificateissuingtemplates = _certificateissuingtemplates(self)
        self.connectors = _connectors(self)
        self.dataencryptionkeys = _dataencryptionkeys(self)
        self.edgeencryptionkeys = _edgeencryptionkeys(self)
        self.edgeinstances = _edgeinstances(self)
        self.edgeworkers = _edgeworkers(self)
        self.environments = _environments(self)
        self.integrationservices = _integrationservices(self)
        self.integrationservicesaggregates = _integrationservicesaggregates(self)
        self.machineidentities = _machineidentities(self)
        self.machineidentitysearch = _machineidentitysearch(self)
        self.machines = _machines(self)
        self.machinesearch = _machinesearch(self)
        self.machinetypes = _machinetypes(self)
        self.notifications = _notifications(self)
        self.outagedetection = _outagedetection(self)
        self.pairingcodes = _pairingcodes(self)
        self.preferences = _preferences(self)
        self.ssoconfigurations = _ssoconfigurations(self)
        self.teams = _teams(self)
        self.useraccounts = _useraccounts(self)
        self.users = _users(self)
        # endregion Endpoints
