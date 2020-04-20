from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.processing_engines import ProcessingEngines


class _ProcessingEngines(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/ProcessingEngines')

        self.Engine = self._Engine(websdk_obj=websdk_obj)
        self.Folder = self._Folder(websdk_obj=websdk_obj)

    def get(self):
        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property()
            def engines(self):
                return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

        return _Response(
            response=self._get(),
            expected_return_codes=[200],
            api_source=self._api_source
        )

    class _Engine:
        def __init__(self, websdk_obj):
            self._websdk_obj = websdk_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

        class _Guid(API):
            def __init__(self, guid: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Engine/{guid}')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property(return_on_204=list)
                    def folders(self):
                        return [ProcessingEngines.Folder(folder) for folder in self._from_json('Folders')][0]

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200, 204],
                    api_source=self._api_source
                )

            def post(self, folder_guids: list):
                body = {
                    'FolderGuids': folder_guids
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)@property

                    @json_response_property(return_on_204=str)
                    def added_count(self) -> int:
                        return self._from_json('AddedCount')

                    @property
                    @json_response_property(return_on_204=list)
                    def errors(self) -> List[str]:
                        return self._from_json('Errors')

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

    class _Folder:
        def __init__(self, websdk_obj):
            self._websdk_obj = websdk_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

        class _Guid(API):
            def __init__(self, guid: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Folder/{guid}')
                self._folder_guid = guid

            def delete(self):
                return APIResponse(
                    response=self._delete(),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property(return_on_204=list)
                    def engines(self):
                        return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200, 204],
                    api_source=self._api_source
                )

            def put(self, engine_guids: list):
                body = {
                    'EngineGuids': engine_guids
                }

                return APIResponse(
                    response=self._put(data=body),
                    expected_return_codes=[200, 204],
                    api_source=self._api_source
                )

            def EngineGuid(self, guid):
                return self._EngineGuid(guid=self._folder_guid, engine_guid=guid, websdk_obj=self._api_obj)

            class _EngineGuid(API):
                def __init__(self, guid: str, engine_guid: str, websdk_obj):
                    super().__init__(api_obj=websdk_obj, url=f'/ProcessingEngines/Folder/{guid}/{engine_guid}')

                def delete(self):
                    return APIResponse(
                        response=self._delete(),
                        expected_return_codes=[200],
                        api_source=self._api_source
                    )
