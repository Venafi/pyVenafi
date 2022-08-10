from pytpp.api.api_base import OutputModel, ApiField


class Permissions(OutputModel):
    delete: bool = ApiField(alias='Delete')
    discover: bool = ApiField(alias='Discover')
    manage: bool = ApiField(alias='Manage')
    read: bool = ApiField(alias='Read')
    revoke: bool = ApiField(alias='Revoke')
