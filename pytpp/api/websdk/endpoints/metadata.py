from typing import List
from pytpp.api.websdk.outputs import config, metadata
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


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

            class Response(WebSdkOutputModel):
                dn: str = ApiField(alias='DN')
                item: metadata.Item = ApiField(alias='Item')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Find(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Find')

        def post(self, item: str = None, item_guid: str = None, value: str = None):
            body = {
                'Item': item,
                'ItemGuid': item_guid,
                'Value': value
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                objects: List[config.Object] = ApiField(default_factory=list, alias='Objects')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _FindItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/FindItem')

        def post(self, name: str):
            body = {
                'Name': name
            }

            class Response(WebSdkOutputModel):
                item_guid: str = ApiField(alias='ItemGuid')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Get(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Get')

        def post(self, dn: str, all_included: bool = None):
            body = {
                'DN': dn,
                'All': all_included
            }

            class Response(WebSdkOutputModel):
                data: metadata.Data = ApiField(alias='Data')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _GetItemGuids(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemGuids')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkOutputModel):
                item_guids: List[str] = ApiField(default_factory=list, alias='ItemGuids')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _GetItems(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _GetItemsForClass(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemsForClass')

        def post(self, config_class: str):
            body = {
                'ConfigClass': config_class
            }

            class Response(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _GetPolicyItems(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetPolicyItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_items: List[metadata.PolicyItem] = ApiField(default_factory=list, alias='PolicyItems')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Items(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Items')

        def get(self):
            class Response(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._get())

    class _LoadItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItem')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkOutputModel):
                item: metadata.Item = ApiField(alias='Item')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _LoadItemGuid(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItemGuid')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Response(WebSdkOutputModel):
                item_guid: str = ApiField(alias='ItemGuid')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _ReadEffectiveValues(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadEffectiveValues')

        def post(self, dn: str, item_guid: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_dn: str = ApiField(alias='PolicyDn')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ApiField(default_factory=list, alias='Values')

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _ReadPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadPolicy')

        def post(self, dn: str, item_guid: str, obj_type: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid,
                'Type': obj_type
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ApiField(default_factory=list, alias='Values')

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Set(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Set')

        def post(self, dn: str, guid_data: list, keep_existing: bool = False):
            body = {
                'DN': dn,
                'GuidData': guid_data,
                'KeepExisting': keep_existing
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

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

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _UndefineItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UndefineItem')

        def post(self, item_guid: str, remove_data: bool = True):
            body = {
                'ItemGuid': item_guid,
                'RemoveData': remove_data
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _UpdateItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UpdateItem')

        def post(self, item: dict = None, update: dict = None):
            body = {
                'ItemGuid': item,
                'Update': update
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(response_cls=Response, response=self._post(data=body))
