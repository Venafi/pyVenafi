from __future__ import annotations
from venafi.cloud.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output
from venafi.cloud.api.models import activitylog_service
from typing import List


class _activitylogsearch(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/activitylogsearch')
        self.export = self._export(api_obj=self._api_obj, url=f'{self._url}/export')

    def post(self, ActivityLogSearchRequest: activitylog_service.ActivityLogSearchRequest):
        data = {**ActivityLogSearchRequest.dict()}

        class Output(VaasSdkOutputModel):
            ActivityLogEntriesResponse: activitylog_service.ActivityLogEntriesResponse
        return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'ActivityLogEntriesResponse'})

    class _export(VaasSdkEndpoint):
        def post(self, ActivityLogSearchRequest: activitylog_service.ActivityLogSearchRequest):
            data = {**ActivityLogSearchRequest.dict()}

            class Output(VaasSdkOutputModel):
                ActivityLogEntriesResponse: activitylog_service.ActivityLogEntriesResponse
            return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'ActivityLogEntriesResponse'})


class _activitytypes(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/activitytypes')

    def get(self):
        class Output(VaasSdkOutputModel):
            ActivityLogTypeList: List[activitylog_service.ActivityLogType]
        return generate_output(output_cls=Output, response=self._get(params={}), root_field='ActivityLogTypeList')
