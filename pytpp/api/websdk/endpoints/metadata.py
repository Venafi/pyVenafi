from typing import List
from properties.response_objects.dataclasses import config, metadata
from pytpp.api.api_base import WebSdkEndpoint, WebSdkResponse, ResponseFactory, ResponseField


class _Metadata(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Log')
        self.DefineItem = self._DefineItem(api_obj=api_obj)
        self.Find = self._Find(api_obj=api_obj)
        self.FindItem = self._FindItem(api_obj=api_obj)
        self.Get = self._Get(api_obj=api_obj)
        self.GetItemGuids = self._GetItemGuids(api_obj=api_obj)
        self.GetItems = self._GetItems(api_obj=api_obj)
        self.GetItemsForClass = self._GetItemsForClass(api_obj=api_obj)
        self.GetPolicyItems = self._GetPolicyItems(api_obj=api_obj)
        self.Items = self._Items(api_obj=api_obj)
        self.LoadItem = self._LoadItem(api_obj=api_obj)
        self.LoadItemGuid = self._LoadItemGuid(api_obj=api_obj)
        self.ReadEffectiveValues = self._ReadEffectiveValues(api_obj=api_obj)
        self.ReadPolicy = self._ReadPolicy(api_obj=api_obj)
        self.Set = self._Set(api_obj=api_obj)
        self.SetPolicy = self._SetPolicy(api_obj=api_obj)
        self.UndefineItem = self._UndefineItem(api_obj=api_obj)
        self.UpdateItem = self._UpdateItem(api_obj=api_obj)

    class _DefineItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/DefineItem')

        def post(self, item: dict):
            body = {
                'Item': item
            }

            class Response(WebSdkResponse):
                dn: str = ResponseField(alias='DN')
                item: metadata.Item = ResponseField(alias='Item')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Find(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Find')

        def post(self, item: str = None, item_guid: str = None, value: str = None):
            body = {
                'Item': item,
                'ItemGuid': item_guid,
                'Value': value
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                objects: List[config.Object] = ResponseField(default_factory=list, alias='Objects')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _FindItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/FindItem')

        def post(self, name: str):
            body = {
                'Name': name
            }

            class Response(WebSdkResponse):
                item_guid: str = ResponseField(alias='ItemGuid')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Get(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Get')

        def post(self, dn: str, all_included: bool = None):
            body = {
                'DN': dn,
                'All': all_included
            }

            class Response(WebSdkResponse):
                data: metadata.Data = ResponseField(alias='Data')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetItemGuids(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemGuids')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkResponse):
                item_guids: List[str] = ResponseField(default_factory=list, alias='ItemGuids')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetItems(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkResponse):
                items: List[metadata.Item] = ResponseField(default_factory=list, alias='Items')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetItemsForClass(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemsForClass')

        def post(self, config_class: str):
            body = {
                'ConfigClass': config_class
            }

            class Response(WebSdkResponse):
                items: List[metadata.Item] = ResponseField(default_factory=list, alias='Items')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _GetPolicyItems(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetPolicyItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                policy_items: List[metadata.PolicyItem] = ResponseField(default_factory=list, alias='PolicyItems')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Items(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Items')

        def get(self):
            class Response(WebSdkResponse):
                items: List[metadata.Item] = ResponseField(default_factory=list, alias='Items')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._get())

    class _LoadItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItem')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkResponse):
                item: metadata.Item = ResponseField(alias='Item')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _LoadItemGuid(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItemGuid')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkResponse):
                item_guid: str = ResponseField(alias='ItemGuid')
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ReadEffectiveValues(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadEffectiveValues')

        def post(self, dn: str, item_guid: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                policy_dn: str = ResponseField(alias='PolicyDn')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ResponseField(default_factory=list, alias='Values')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ReadPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadPolicy')

        def post(self, dn: str, item_guid: str, obj_type: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid,
                'Type': obj_type
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ResponseField(default_factory=list, alias='Values')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Set(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Set')

        def post(self, dn: str, guid_data: list, keep_existing: bool = False):
            body = {
                'DN': dn,
                'GuidData': guid_data,
                'KeepExisting': keep_existing
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _SetPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/SetPolicy')

        def post(self, dn: str, config_class: str, guid_data: list, locked: bool = False):
            body = {
                'DN': dn,
                'ConfigClass': config_class,
                'GuidData': guid_data,
                'Locked': locked
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _UndefineItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UndefineItem')

        def post(self, item_guid: str, remove_data: bool = True):
            body = {
                'ItemGuid': item_guid,
                'RemoveData': remove_data
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _UpdateItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UpdateItem')

        def post(self, item: dict = None, update: dict = None):
            body = {
                'ItemGuid': item,
                'Update': update
            }

            class Response(WebSdkResponse):
                locked: bool = ResponseField(alias='Locked')
                result: metadata.Result = ResponseField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return ResponseFactory(response_cls=Response, response=self._post(data=body))
