from pyvenafi.tpp.api.websdk.websdk import *
from pyvenafi.tpp.plugins.api.websdk.endpoints.rights import _Rights


class WebSDK(WebSDK):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Rights = _Rights(self)
