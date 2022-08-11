from pytpp.api.websdk.outputs import recycle_bin
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from typing import List


class _RecycleBin:
    def __init__(self, api_obj):
        self.DeletionTask = self._DeletionTask(api_obj=api_obj)
        self.Empty = self._Empty(api_obj=api_obj)
        self.GetConfiguration = self._GetConfiguration(api_obj=api_obj)
        self.GetContents = self._GetContents(api_obj=api_obj)
        self.GetItem = self._GetItem(api_obj=api_obj)
        self.Purge = self._Purge(api_obj=api_obj)
        self.PurgeTask = self._PurgeTask(api_obj=api_obj)
        self.Restore = self._Restore(api_obj=api_obj)
        self.SetConfiguration = self._SetConfiguration(api_obj=api_obj)

    class _DeletionTask(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/DeletionTask')
        
        def post(self, start: bool = None, stop: bool = None):
            body = {
                'Start': start,
                'Stop': stop
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Empty(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/Empty')

        def post(self):
            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetConfiguration(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/GetConfiguration')

        def post(self):
            class Output(WebSdkOutputModel):
                deletion: recycle_bin.Deletion = ApiField(alias='Deletion')
                purge: recycle_bin.Purge = ApiField(alias='Purge')
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetContents(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/GetContents')

        def post(self, limit: int):
            body = {
                'Limit': limit
            }

            class Output(WebSdkOutputModel):
                items: List[recycle_bin.Item] = ApiField(alias='Items', default_factory=list)
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))
                total: int = ApiField(alias='Total')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetItem(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/GetItem')

        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                item: recycle_bin.Item = ApiField(alias='Item')
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Purge(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/Purge')

        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _PurgeTask(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/PurgeTask')

        def post(self, purge_all: bool, start: bool = None, stop: bool = None):
            body = {
                'PurgeAll': purge_all,
                'Start': start,
                'Stop': stop
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Restore(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/Restore')

        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SetConfiguration(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='RecycleBin/SetConfiguration')

        def post(self, deletion: dict, purge: dict = None):
            body = {
                'Deletion': deletion,
                'Purge': purge
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))
