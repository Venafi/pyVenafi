from typing import List
from pytpp.properties.response_objects.dataclasses import preferences as prefs
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _Preferences(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Preferences')

    def get(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name': name,
            'Product': product
        }

        class Response(APIResponse):
            preferences: List[prefs.Preference] = ResponseField(alias='Preferences', default_factory=list)

        return ResponseFactory(response_cls=Response, response=self._get(params=params))

    def post(self, preferences: list):
        body = {
            'Preferences': preferences
        }

        return ResponseFactory(response_cls=APIResponse, response=self._post(data=body))

    def delete(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name': name,
            'Product': product
        }

        return ResponseFactory(response_cls=APIResponse, response=self._delete(params=params))
