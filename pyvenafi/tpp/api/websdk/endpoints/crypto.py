from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)

class _Crypto:
    def __init__(self, api_obj):
        self.AvailableKeys = self._AvailableKeys(api_obj=api_obj, url='/Crypto/AvailableKeys')
        self.DefaultKey = self._DefaultKey(api_obj=api_obj, url='/Crypto/DefaultKey')

    class _AvailableKeys(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                keynames: list[str] = ApiField(alias='Keynames', default_factory=list)

            return generate_output(response=self._get(), output_cls=Output)

    class _DefaultKey(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                default_key: str = ApiField(alias='DefaultKey')

            return generate_output(response=self._get(), output_cls=Output)
