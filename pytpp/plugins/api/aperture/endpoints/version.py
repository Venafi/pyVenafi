from pytpp.plugins.api.api_base import API, APIResponse, api_response_property
from pytpp.tools.helpers.date_converter import from_date_string
from typing import List


class _Version:
    def __init__(self, api_obj):
        self.Schema = self._Schema(api_obj=api_obj)

    class _Schema(API):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url='/version/schema'
            )

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(
                        response=response, 
                        api_source=api_source
                    )
                
                @property
                @api_response_property()
                def additional_schema_info(self) -> List[str]:
                    return self._from_json(key='additionalSchemaInfo')

                @property
                @api_response_property()
                def currentDbSchemaVersion(self) -> str:
                    return self._from_json(key='currentDbSchemaVersion')

                @property
                @api_response_property()
                def current_db_schema_version_installation_date(self):
                    return from_date_string(self._from_json(key='currentDbSchemaVersionInstallationDate'))

                @property
                @api_response_property()
                def engine_name(self) -> str:
                    return self._from_json(key='EngineName')

                @property
                @api_response_property()
                def schema_version(self) -> str:
                    return self._from_json(key='schemaVersion')

            return _Response(
                response=self._get(),
                api_source=self._api_source
            )
