from venafi.tpp.api.api_base import generate_output, ApiField
from venafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from datetime import datetime
from typing import List


class _Version(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/version')
        self.Schema = self._Schema(api_obj=self._api_obj, url=f'{self._url}/schema')

    class _Schema(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                additional_schema_info: List[str] = ApiField(alias='additionalSchemaInfo', default_factory=list)
                currentDbSchemaVersion: str = ApiField(alias='currentDbSchemaVersion')
                current_db_schema_version_installation_date: datetime = ApiField(alias='currentDbSchemaVersionInstallationDate')
                engine_name: str = ApiField(alias='EngineName')
                schema_version: str = ApiField(alias='schemaVersion')

            return generate_output(output_cls=Output, response=self._get())
