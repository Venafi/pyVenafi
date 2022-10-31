from venafi.tpp.api.api_base import generate_output, ApiField
from venafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from venafi.tpp.plugins.api.aperture.enums.credentials import Field
from venafi.tpp.plugins.api.aperture.models import credentials as creds
from typing import List, Dict


class _Credentials(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/credentials')
        self.Filters = self._Filters(api_obj=self._api_obj, url=f'{self._url}/filters')

    class _Filters(ApertureEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Apply = self._Apply(api_obj=self._api_obj, url=f'{self._url}/apply')

        class _Apply(ApertureEndpoint):
            def post(self, fields: List[str] = None, filters: Dict[str, List] = None, is_sort_ascending: bool = True,
                     limit: int = 100, offset: int = 0, sort_field: str = 'Name'):
                fields = fields or [
                    Field.id,
                    Field.name,
                    Field.schema_class,
                    Field.parent_dn,
                    Field.contacts,
                    Field.created_on,
                    Field.description,
                    Field.single_click_action,
                    Field.permissions,
                ]
                filters = filters or {}
                body = {
                    'fields'         : fields,
                    'filters'        : filters,
                    'isSortAscending': is_sort_ascending,
                    'limit'          : limit,
                    'offset'         : offset,
                    'sortField'      : sort_field
                }

                class Output(ApertureOutputModel):
                    credentials: List[creds.CredentialDetails] = ApiField(default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body), root_field='credentials')
