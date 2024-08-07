from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import preferences as prefs

class _Preferences(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Preferences')

    def get(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name'    : name,
            'Product' : product
        }

        class Output(WebSdkOutputModel):
            preferences: list[prefs.Preference] = ApiField(alias='Preferences', default_factory=list)

        return generate_output(output_cls=Output, response=self._get(params=params))

    def post(self, preferences: list[prefs.Preference]):
        body = {
            'Preferences': preferences
        }

        return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

    def delete(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name'    : name,
            'Product' : product
        }

        return generate_output(output_cls=WebSdkOutputModel, response=self._delete(params=params))
