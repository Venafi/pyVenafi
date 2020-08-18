from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.config_schema import ConfigSchema


class _ConfigSchema:
    def __init__(self, api_obj):
        self.Attributes = self._Attributes(api_obj=api_obj)
        self.Class = self._Class(api_obj=api_obj)

    class _Attributes(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Attributes')

        def post(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return ConfigSchema.Result(self._from_json(key='Result'))

                @property
                @json_response_property()
                def attribute_definitions(self):
                    return [ConfigSchema.AttributeDefinition(attr) for attr in self._from_json('AttributeDefinitions')]

            return _Response(response=self._post(data={}), api_source=self._api_source)

    class _Class(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/ConfigSchema/Class')

        def post(self, class_name: str):
            body = {
                "Class": class_name
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return ConfigSchema.Result(self._from_json(key='Result'))

                @property
                @json_response_property()
                def class_definition(self):
                    return ConfigSchema.ClassDefinition(self._from_json('ClassDefinition'))

            return _Response(response=self._post(data=body), api_source=self._api_source)
