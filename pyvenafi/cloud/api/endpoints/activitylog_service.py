from __future__ import annotations
from pyvenafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output
from pyvenafi.cloud.api.models import activitylog_service
from typing import List


class _activitylog_service:
    def __init__(self, api_obj):
        self.v1 = self._v1(api_obj=api_obj)

    class _v1(CloudApiEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='v1')
            self.activitylogsearch = self._activitylogsearch(api_obj=self._api_obj, url=f'{self._url}/activitylogsearch')
            self.activitytypes = self._activitytypes(api_obj=self._api_obj, url=f'{self._url}/activitytypes')

        class _activitylogsearch(CloudApiEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.export = self._export(api_obj=self._api_obj, url=f'{self._url}/export')

            def post(self, ActivityLogSearchRequest: activitylog_service.ActivityLogSearchRequest):
                data = {**ActivityLogSearchRequest.dict()}

                class Output(CloudApiOutputModel):
                    ActivityLogEntriesResponse: activitylog_service.ActivityLogEntriesResponse
                return generate_output(output_cls=Output, response=self._post(data=data), rc_mapping={200: 'ActivityLogEntriesResponse'})

            class _export(CloudApiEndpoint):
                def post(self, ActivityLogSearchRequest: activitylog_service.ActivityLogSearchRequest):
                    data = {**ActivityLogSearchRequest.dict()}

                    class Output(CloudApiOutputModel):
                        ActivityLogEntryInformationList: List[activitylog_service.ActivityLogEntryInformation]
                    return generate_output(output_cls=Output, response=self._post(data=data), root_field='ActivityLogEntryInformationList')

        class _activitytypes(CloudApiEndpoint):
            def get(self):
                class Output(CloudApiOutputModel):
                    ActivityLogTypeList: List[activitylog_service.ActivityLogType]
                return generate_output(output_cls=Output, response=self._get(params={}), root_field='ActivityLogTypeList')
