from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import config_schema

class _ConfigSchema(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/ConfigSchema')
        self.Attributes = self._Attributes(api_obj=api_obj, url=f'{self._url}/Attributes')
        self.Class = self._Class(api_obj=api_obj, url=f'{self._url}/Class')

    class _Attributes(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                attribute_definitions: list[config_schema.AttributeDefinition] = ApiField(
                    default_factory=list, alias='AttributeDefinitions'
                )
                result: config_schema.Result = ApiField(
                    alias='Result',
                    converter=lambda x: config_schema.Result(code=x)
                )

            return generate_output(response=self._post(data={}), output_cls=Output)

    class _Class(WebSdkEndpoint):
        def post(self, class_name: str):
            body = {
                "Class": class_name
            }

            class Output(WebSdkOutputModel):
                class_definition: config_schema.ClassDefinition = ApiField(alias='ClassDefinition')
                result: config_schema.Result = ApiField(
                    alias='Result',
                    converter=lambda x: config_schema.Result(code=x)
                )

            return generate_output(response=self._post(data=body), output_cls=Output)
