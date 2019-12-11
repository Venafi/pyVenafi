from api.api_base import API, response_property
from properties.response_objects.metadata import Metadata
from properties.response_objects.config import Config


class _Metadata(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Log', valid_return_codes=[200])
        self.DefineItem = self._DefineItem(websdk_obj=websdk_obj)
        self.Find = self._Find(websdk_obj=websdk_obj)
        self.FindItem = self._FindItem(websdk_obj=websdk_obj)
        self.Get = self._Get(websdk_obj=websdk_obj)
        self.GetItemGuids = self._GetItemGuids(websdk_obj=websdk_obj)
        self.GetItems = self._GetItems(websdk_obj=websdk_obj)
        self.GetItemsForClass = self._GetItemsForClass(websdk_obj=websdk_obj)
        self.GetPolicyItems = self._GetPolicyItems(websdk_obj=websdk_obj)
        self.Items = self._Items(websdk_obj=websdk_obj)
        self.LoadItem = self._LoadItem(websdk_obj=websdk_obj)
        self.LoadItemGuid = self._LoadItemGuid(websdk_obj=websdk_obj)
        self.ReadEffectiveValues = self._ReadEffectiveValues(websdk_obj=websdk_obj)
        self.ReadPolicy = self._ReadPolicy(websdk_obj=websdk_obj)
        self.Set = self._Set(websdk_obj=websdk_obj)
        self.SetPolicy = self._SetPolicy(websdk_obj=websdk_obj)
        self.UndefineItem = self._UndefineItem(websdk_obj=websdk_obj)
        self.UpdateItem = self._UpdateItem(websdk_obj=websdk_obj)

    class _DefineItem(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/DefineItem', valid_return_codes=[200])

        @property
        @response_property()
        def dn(self):
            return self.json_response('DN')

        @property
        @response_property()
        def item(self):
            return

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, item: dict):
            body = {
                'Item': item
            }

            self.response = self._post(data=body)

            return self

    class _Find(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/Find', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self.json_response('Objects')]

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, item: str = None, item_guid: str = None, value: str = None):
            body = {
                'Item': item,
                'ItemGuid': item_guid,
                'Value': value
            }

            self.response = self._post(data=body)

            return self

    class _FindItem(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/FindItem', valid_return_codes=[200])

        @property
        @response_property()
        def item_guid(self):
            return self.json_response('ItemGuid')

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, name: str):
            body = {
                'Name': name
            }

            self.response = self._post(data=body)

            return self

    class _Get(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/Get', valid_return_codes=[200])

        @property
        @response_property()
        def data(self):
            return [Metadata.Data(self.json_response('Data'))]

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str, all_included: bool = None):
            body = {
                'DN': dn,
                'All': all_included
            }

            self.response = self._post(data=body)

            return self

    class _GetItemGuids(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/GetItemGuids', valid_return_codes=[200])

        @property
        @response_property()
        def item_guids(self):
            return self.json_response('ItemGuids')

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            self.response = self._post(data=body)

            return self

    class _GetItems(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/GetItems', valid_return_codes=[200])

        @property
        @response_property()
        def items(self):
            return [Metadata.Item(item) for item in self.json_response('Items')]

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            self.response = self._post(data=body)

            return self

    class _GetItemsForClass(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/GetItemsForClass', valid_return_codes=[200])

        @property
        @response_property()
        def items(self):
            return [Metadata.Item(item) for item in self.json_response('Items')]

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, config_class: str):
            body = {
                'ConfigClass': config_class
            }

            self.response = self._post(data=body)

            return self

    class _GetPolicyItems(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/GetPolicyItems', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def policy_items(self):
            return [Metadata.PolicyItem(item) for item in self.json_response('PolicyItems')]

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            self.response = self._post(data=body)

            return self

    class _Items(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/Items', valid_return_codes=[200])

        @property
        @response_property()
        def items(self):
            return [Metadata.Item(item) for item in self.json_response('Items')]

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def get(self):
            self.response = self._get()
            return self

    class _LoadItem(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/LoadItem', valid_return_codes=[200])

        @property
        @response_property()
        def item(self):
            return Metadata.Item(self.json_response('Item'))

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            self.response = self._post(body)

            return self

    class _LoadItemGuid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/LoadItemGuid', valid_return_codes=[200])

        @property
        @response_property()
        def item_guid(self):
            return self.json_response('ItemGuid')

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            self.response = self._post(body)

            return self

    class _ReadEffectiveValues(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/ReadEffectiveValues', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def policy_dn(self):
            return self.json_response('PolicyDn')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        @property
        @response_property()
        def values(self):
            return self.json_response('Values')

        def post(self, dn: str, item_guid: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid
            }

            self.response = self._post(body)

            return self

    class _ReadPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/ReadPolicy', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        @property
        @response_property()
        def values(self):
            return self.json_response('Values')

        def post(self, dn: str, item_guid: str, obj_type: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid,
                'Type': obj_type
            }

            self.response = self._post(body)

            return self

    class _Set(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/Set', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str, guid_data: list, keep_existing: bool = False):
            body = {
                'DN': dn,
                'GuidData': guid_data,
                'KeepExisting': keep_existing
            }

            self.response = self._post(data=body)

            return self

    class _SetPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/SetPolicy', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, dn: str, config_class: str, guid_data: list, locked: bool = False):
            body = {
                'DN': dn,
                'ConfigClass': config_class,
                'GuidData': guid_data,
                'Locked': locked
            }

            self.response = self._post(data=body)

            return self

    class _UndefineItem(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/UndefineItem', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, item_guid: str, remove_data: bool = True):
            body = {
                'ItemGuid': item_guid,
                'RemoveData': remove_data
            }

            self.response = self._post(data=body)

            return self

    class _UpdateItem(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Metadata/UpdateItem', valid_return_codes=[200])

        @property
        @response_property()
        def locked(self):
            return self.json_response('Locked')

        @property
        @response_property()
        def result(self):
            return Metadata.Result(self.json_response('Result'))

        def post(self, item: dict = None, update: dict = None):
            body = {
                'ItemGuid': item,
                'Update': update
            }

            self.response = self._post(data=body)

            return self
