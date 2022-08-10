from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from datetime import datetime
from typing import List


class _Version:
    def __init__(self, api_obj):
        self.Schema = self._Schema(api_obj=api_obj)

    class _Schema(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/version/schema')

        def get(self):
            class Response(ApertureOutputModel):
                additional_schema_info: List[str] = ApiField(alias='additionalSchemaInfo', default_factory=list)
                currentDbSchemaVersion: str = ApiField(alias='currentDbSchemaVersion')
                current_db_schema_version_installation_date: datetime = ApiField(alias='currentDbSchemaVersionInstallationDate')
                engine_name: str = ApiField(alias='EngineName')
                schema_version: str = ApiField(alias='schemaVersion')

            return generate_output(response_cls=Response, response=self._get())
