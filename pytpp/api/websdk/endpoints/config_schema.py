from typing import List
from pytpp.api.websdk.outputs import config_schema
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _ConfigSchema:
    def __init__(self, api_obj):
        self.Attributes = self._Attributes(api_obj=api_obj)
        self.Class = self._Class(api_obj=api_obj)

    class _Attributes(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Attributes')

        def post(self):
            class Response(WebSdkOutputModel):
                attribute_definitions: List[config_schema.AttributeDefinition] = ApiField(
                    default_factory=list, alias='AttributeDefinitions'
                )
                result: config_schema.Result = ApiField(alias='Result', converter=lambda x: config_schema.Result(code=x))

            return generate_output(response=self._post(data={}), response_cls=Response)

    class _Class(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Class')

        def post(self, class_name: str):
            body = {
                "Class": class_name
            }

            class Response(WebSdkOutputModel):
                class_definition: config_schema.ClassDefinition = ApiField(alias='ClassDefinition')
                result: config_schema.Result = ApiField(alias='Result', converter=lambda x: config_schema.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)
