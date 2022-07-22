from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Permissions(PayloadModel):
    is_associate_allowed: bool = PayloadField(alias='IsAssociateAllowed', default=None)
    is_create_allowed: bool = PayloadField(alias='IsCreateAllowed', default=None)
    is_delete_allowed: bool = PayloadField(alias='IsDeleteAllowed', default=None)
    is_manage_permissions_allowed: bool = PayloadField(alias='IsManagePermissionsAllowed', default=None)
    is_policy_write_allowed: bool = PayloadField(alias='IsPolicyWriteAllowed', default=None)
    is_private_key_read_allowed: bool = PayloadField(alias='IsPrivateKeyReadAllowed', default=None)
    is_private_key_write_allowed: bool = PayloadField(alias='IsPrivateKeyWriteAllowed', default=None)
    is_read_allowed: bool = PayloadField(alias='IsReadAllowed', default=None)
    is_rename_allowed: bool = PayloadField(alias='IsRenameAllowed', default=None)
    is_revoke_allowed: bool = PayloadField(alias='IsRevokeAllowed', default=None)
    is_view_allowed: bool = PayloadField(alias='IsViewAllowed', default=None)
    is_write_allowed: bool = PayloadField(alias='IsWriteAllowed', default=None)
