from uuid import UUID
from typing import Union
from pyvenafi.cloud.api.cloud_api import CloudApi

class Authenticate:
    """
    Authenticates to Venafi Cloud API.
    """

    def __init__(
        self, server: str, api_key: Union[UUID, str], proxies: dict = None,
        verify_ssl: bool = True, connection_timeout: float = None,
        read_timeout: float = None
    ):
        self.cloud_api = CloudApi(
            server=server, api_key=api_key, proxies=proxies,
            verify_ssl=verify_ssl, connection_timeout=connection_timeout,
            read_timeout=read_timeout
        )
