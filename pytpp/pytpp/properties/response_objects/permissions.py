class Permissions:
    class Permissions:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.is_associate_allowed = response_object.get('IsAssociateAllowed')
            self.is_create_allowed = response_object.get('IsCreateAllowed')
            self.is_delete_allowed = response_object.get('IsDeleteAllowed')
            self.is_manage_permissions_allowed = response_object.get('IsManagePermissionsAllowed')
            self.is_policy_write_allowed = response_object.get('IsPolicyWriteAllowed')
            self.is_private_key_read_allowed = response_object.get('IsPrivateKeyReadAllowed')
            self.is_private_key_write_allowed = response_object.get('IsPrivateKeyWriteAllowed')
            self.is_read_allowed = response_object.get('IsReadAllowed')
            self.is_rename_allowed = response_object.get('IsRenameAllowed')
            self.is_revoke_allowed = response_object.get('IsRevokeAllowed')
            self.is_view_allowed = response_object.get('IsViewAllowed')
            self.is_write_allowed = response_object.get('IsWriteAllowed')
