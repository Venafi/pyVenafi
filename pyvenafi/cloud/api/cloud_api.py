from pyvenafi.cloud.api.session import Session
from pyvenafi.cloud.api.endpoints.account_service import _account_service
from pyvenafi.cloud.api.endpoints.activitylog_service import _activitylog_service
from pyvenafi.cloud.api.endpoints.caoperations_service import _caoperations_service
from pyvenafi.cloud.api.endpoints.certificate_service import _certificate_service
from pyvenafi.cloud.api.endpoints.connectors_service import _connectors_service
from pyvenafi.cloud.api.endpoints.edgemanagement_service import _edgemanagement_service
from pyvenafi.cloud.api.endpoints.integrations_service import _integrations_service
from pyvenafi.cloud.api.endpoints.outagedetection_service import _outagedetection_service
from pyvenafi.cloud.api.endpoints.provisioning_service import _provisioning_service
from pyvenafi.cloud.api.endpoints.tagging_service import _tagging_service


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
        self.account_service = _account_service(self)
        self.activitylog_service = _activitylog_service(self)
        self.caoperations_service = _caoperations_service(self)
        self.certificate_service = _certificate_service(self)
        self.connectors_service = _connectors_service(self)
        self.edgemanagement_service = _edgemanagement_service(self)
        self.integrations_service = _integrations_service(self)
        self.outagedetection_service = _outagedetection_service(self)
        self.provisioning_service = _provisioning_service(self)
        self.tagging_service = _tagging_service(self)
        # endregion Endpoints
