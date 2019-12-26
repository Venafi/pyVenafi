from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.processing_engines import ProcessingEngines


class _ProcessingEngines(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/ProcessingEngines', valid_return_codes=[200])

        self.Engine = self._Engine(websdk_obj=websdk_obj)
        self.Folder = self._Folder(websdk_obj=websdk_obj)

    @property
    @json_response_property()
    def engines(self):
        return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

    def get(self):
        self.json_response = self._get()
        return self

    class _Engine:
        def __init__(self, websdk_obj):
            self._websdk_obj = websdk_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

        class _Guid(API):
            def __init__(self, guid: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Engine/{guid}', valid_return_codes=[200, 201, 204])

            @property
            @json_response_property(on_204=str)
            def added_count(self) -> int:
                return self._from_json('AddedCount')

            @property
            @json_response_property(on_204=list)
            def errors(self) -> List[str]:
                return self._from_json('Errors')

            @property
            @json_response_property(on_204=list)
            def folders(self):
                return [ProcessingEngines.Folder(folder) for folder in self._from_json('Folders')][0]

            def get(self):
                self.json_response = self._get()
                return self

            def post(self, folder_guids: list):
                body = {
                    'FolderGuids': folder_guids
                }

                self.json_response = self._post(data=body)
                return self

    class _Folder:
        def __init__(self, websdk_obj):
            self._websdk_obj = websdk_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

        class _Guid(API):
            def __init__(self, guid: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Folder/{guid}', valid_return_codes=[200, 204])
                self._folder_guid = guid

            @property
            @json_response_property(on_204=list)
            def engines(self):
                return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

            def delete(self):
                self.json_response = self._delete()
                return self

            def get(self):
                self.json_response = self._get()
                return self

            def put(self, engine_guids: list):
                body = {
                    'EngineGuids': engine_guids
                }

                self.json_response = self._put(data=body)
                return self

            def EngineGuid(self, guid):
                return self._EngineGuid(guid=self._folder_guid, engine_guid=guid, websdk_obj=self._api_obj)

            class _EngineGuid(API):
                def __init__(self, guid: str, engine_guid: str, websdk_obj):
                    super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Folder/{guid}/{engine_guid}', valid_return_codes=[200])

                def delete(self):
                    self.json_response = self.delete()
                    return self
