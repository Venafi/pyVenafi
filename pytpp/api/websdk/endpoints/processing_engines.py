from typing import List
from properties.response_objects.dataclasses import processing_engines
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _ProcessingEngines(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/ProcessingEngines')

        self.Engine = self._Engine(api_obj=api_obj)
        self.Folder = self._Folder(api_obj=api_obj)

    def get(self):
        class Response(APIResponse):
            engines: List[processing_engines.Engine] = ResponseField(alias='Engines', default_factory=list)

        return ResponseFactory(response_cls=Response, response=self._get())

    class _Engine:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Engine/{guid}')

            def get(self):
                class Response(APIResponse):
                    folders: List[processing_engines.Folder] = ResponseField(alias='Folders', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._get())

            def post(self, folder_guids: list):
                body = {
                    'FolderGuids': folder_guids
                }

                class Response(APIResponse):
                    added_count: int = ResponseField(alias='AddedCount')
                    errors: List[str] = ResponseField(alias='Errors', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Folder:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Folder/{guid}')
                self._folder_guid = guid

            def delete(self):
                return ResponseFactory(response_cls=APIResponse, response=self._delete())

            def get(self):
                class Response(APIResponse):
                    engines: List[processing_engines.Engine] = ResponseField(alias='Engines', default_factory=list)

                return ResponseFactory(response_cls=Response, response=self._get())

            def put(self, engine_guids: list):
                body = {
                    'EngineGuids': engine_guids
                }

                return ResponseFactory(response_cls=APIResponse, response=self._put(data=body))

            def EngineGuid(self, guid):
                return self._EngineGuid(guid=self._folder_guid, engine_guid=guid, api_obj=self._api_obj)

            class _EngineGuid(API):
                def __init__(self, guid: str, engine_guid: str, api_obj):
                    super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Folder/{guid}/{engine_guid}')

                def delete(self):
                    return ResponseFactory(response_cls=APIResponse, response=self._delete())
