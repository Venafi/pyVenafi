from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.enums.ssh_keyset import Field
from pytpp.plugins.api.aperture.models import ssh_keyset
from typing import List, Dict


class _SshKeysets(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SshKeysets')
        self.Filters = self._Filters(api_obj=self._api_obj, url=f'{self._url}/filters')

    class _Filters(ApertureEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Apply = self._Apply(api_obj=self._api_obj, url=f'{self._url}/apply')

        class _Apply(ApertureEndpoint):
            def post(self, fields: List[str] = None, filters: Dict[str, List] = None, is_sort_ascending: bool = True,
                     limit: int = 100, offset: int = 0, sort_field: str = 'Name'):
                fields = fields or [
                    Field.access,
                    Field.algorithm,
                    Field.is_unmatched,
                    Field.key_length,
                    Field.trusted_devices,
                    Field.host_key_devices,
                    Field.needs_to_be_provisioned,
                    Field.rotation_scheduled,
                    Field.rotation_error,
                    Field.guid,
                    Field.private_keys_count,
                    Field.public_keys_count,
                    Field.status,
                    Field.risks,
                    Field.fingerprint_md5,
                    Field.fingerprint_sha256,
                    Field.trust_id,
                    Field.unknown_passphrase
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
                    ssh_keysets: List[ssh_keyset.SSHKeyDetails] = ApiField(default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body), root_field='ssh_keysets')
