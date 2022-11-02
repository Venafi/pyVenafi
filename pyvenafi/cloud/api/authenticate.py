from uuid import UUID
from typing import Union
from pyvenafi.cloud.api.cloud_api import CloudApi


class Authenticate:
    """
    Authenticates to Venafi Cloud API.
    """

    def __init__(self, server: str, api_key: Union[UUID, str]):
        self.cloud_api = CloudApi(server=server, api_key=api_key)
