from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.config_schema import ConfigSchema


class _ConfigSchema:
    def __init__(self, websdk_obj):
        self.Attributes = self._Attributes(websdk_obj=websdk_obj)
        self.Class = self._Class(websdk_obj=websdk_obj)

    class _Attributes(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/ConfigSchema/Attributes', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return ConfigSchema.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def attribute_definitions(self):
            return [ConfigSchema.AttributeDefinition(attr) for attr in self._from_json('AttributeDefinitions')]

        def post(self):
            self.json_response = self._post(data={})
            return self

    class _Class(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/ConfigSchema/Class', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return ConfigSchema.Result(self._from_json(key='Result'))

        @property
        @json_response_property()
        def class_definition(self):
            return ConfigSchema.ClassDefinition(self._from_json('ClassDefinition'))

        def post(self, class_name: str):
            body = {
                "Class": class_name
            }

            self.json_response = self._post(data=body)
            return self
