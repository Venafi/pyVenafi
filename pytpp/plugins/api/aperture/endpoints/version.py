from pytpp.api.api_base import ResponseFactory, ResponseField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from datetime import datetime
from typing import List


class _Version:
    def __init__(self, api_obj):
        self.Schema = self._Schema(api_obj=api_obj)

    class _Schema(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/version/schema')

        def get(self):
            class Response(ApertureResponse):
                additional_schema_info: List[str] = ResponseField(alias='additionalSchemaInfo', default_factory=list)
                currentDbSchemaVersion: str = ResponseField(alias='currentDbSchemaVersion')
                current_db_schema_version_installation_date: datetime = ResponseField(alias='currentDbSchemaVersionInstallationDate')
                engine_name: str = ResponseField(alias='EngineName')
                schema_version: str = ResponseField(alias='schemaVersion')

            return ResponseFactory(response_cls=Response, response=self._get())
