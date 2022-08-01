from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Permissions(PayloadModel):
    is_associate_allowed: bool = PayloadField(alias='IsAssociateAllowed')
    is_create_allowed: bool = PayloadField(alias='IsCreateAllowed')
    is_delete_allowed: bool = PayloadField(alias='IsDeleteAllowed')
    is_manage_permissions_allowed: bool = PayloadField(alias='IsManagePermissionsAllowed')
    is_policy_write_allowed: bool = PayloadField(alias='IsPolicyWriteAllowed')
    is_private_key_read_allowed: bool = PayloadField(alias='IsPrivateKeyReadAllowed')
    is_private_key_write_allowed: bool = PayloadField(alias='IsPrivateKeyWriteAllowed')
    is_read_allowed: bool = PayloadField(alias='IsReadAllowed')
    is_rename_allowed: bool = PayloadField(alias='IsRenameAllowed')
    is_revoke_allowed: bool = PayloadField(alias='IsRevokeAllowed')
    is_view_allowed: bool = PayloadField(alias='IsViewAllowed')
    is_write_allowed: bool = PayloadField(alias='IsWriteAllowed')
