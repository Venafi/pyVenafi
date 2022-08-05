from typing import List
from properties.response_objects.dataclasses import config_schema
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _ConfigSchema:
    def __init__(self, api_obj):
        self.Attributes = self._Attributes(api_obj=api_obj)
        self.Class = self._Class(api_obj=api_obj)

    class _Attributes(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Attributes')

        def post(self):
            class Response(APIResponse):
                attribute_definitions: List[config_schema.AttributeDefinition] = ResponseField(
                    default_factory=list, alias='AttributeDefinitions'
                )
                result: config_schema.Result = ResponseField(alias='Result', converter=lambda x: config_schema.Result(code=x))

            return ResponseFactory(response=self._post(data={}), response_cls=Response)

    class _Class(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Class')

        def post(self, class_name: str):
            body = {
                "Class": class_name
            }

            class Response(APIResponse):
                class_definition: config_schema.ClassDefinition = ResponseField(alias='ClassDefinition')
                result: config_schema.Result = ResponseField(alias='Result', converter=lambda x: config_schema.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)
