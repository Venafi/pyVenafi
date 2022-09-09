from uuid import UUID
from typing import Union
from venafi.vaas.api.sdk.sdk import Sdk


class Authenticate:
    """
    Authenticates to TPP WebSDK.
    """

    def __init__(self, server: str, api_key: Union[UUID, str]):
        self.sdk = Sdk(server=server, api_key=api_key)

    def re_authenticate(self):
        pass
