from uuid import UUID
from typing import Union
from venafi.cloud.api.cloud_api import CloudApi


class Authenticate:
    """
    Authenticates to TPP WebSDK.
    """

    def __init__(self, server: str, api_key: Union[UUID, str]):
        self.cloud_api = CloudApi(server=server, api_key=api_key)

    def re_authenticate(self):
        pass
