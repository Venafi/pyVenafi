from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import tagging_service


class _tagging_service:
    def __init__(self, api_obj):
        self.v1 = self._v1(api_obj=api_obj)

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.tags = self._tags(api_obj=self._api_obj, url=f'{self._url}/tags')
            self.tagsassignment = self._tagsassignment(api_obj=self._api_obj, url=f'{self._url}/tagsassignment')

        class _tags(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.values = self._values(api_obj=self._api_obj, url=f'{self._url}/values')

            def NAME(self, name: str):
                return self._NAME(api_obj=self._api_obj, url=f'{self._url}/{name}')

            def get(self):
                class Output(CloudApiOutputModel):
                    TagResponse: tagging_service.TagResponse
                return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TagResponse'})

            def post(self, TagRequest: tagging_service.TagRequest):
                data = {**TagRequest.dict()}

                class Output(CloudApiOutputModel):
                    TagInformation: tagging_service.TagInformation
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'TagInformation'})

            class _NAME(CloudApiEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.values = self._values(api_obj=self._api_obj, url=f'{self._url}/values')

                def delete(self):
                    class Output(CloudApiOutputModel):
                        pass
                    return generate_output(output_cls=Output, response=self._delete(params={}))

                def get(self):
                    class Output(CloudApiOutputModel):
                        TagInformation: tagging_service.TagInformation
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TagInformation'})

                class _values(CloudApiEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    def VALUE(self, value: str):
                        return self._VALUE(api_obj=self._api_obj, url=f'{self._url}/{value}')

                    def get(self):
                        class Output(CloudApiOutputModel):
                            TagValuesResponse: tagging_service.TagValuesResponse
                        return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TagValuesResponse'})

                    def post(self, TagValuesRequest: tagging_service.TagValuesRequest):
                        data = {**TagValuesRequest.dict()}

                        class Output(CloudApiOutputModel):
                            TagValuesResponse: tagging_service.TagValuesResponse
                        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={201: 'TagValuesResponse'})

                    class _VALUE(CloudApiEndpoint):
                        def delete(self):
                            class Output(CloudApiOutputModel):
                                pass
                            return generate_output(output_cls=Output, response=self._delete(params={}))

            class _values(CloudApiEndpoint):
                def get(self):
                    class Output(CloudApiOutputModel):
                        TagValuesResponse: tagging_service.TagValuesResponse
                    return generate_output(output_cls=Output, response=self._get(params={}), rc_mapping={200: 'TagValuesResponse'})

        class _tagsassignment(CloudApiEndpoint):
            def patch(self, TagsAssignRequest: tagging_service.TagsAssignRequest):
                data = {**TagsAssignRequest.dict()}

                class Output(CloudApiOutputModel):
                    TagsAssignResponse: tagging_service.TagsAssignResponse
                return generate_output(output_cls=Output, response=self._patch(data=data), rc_mapping={200: 'TagsAssignResponse'})
