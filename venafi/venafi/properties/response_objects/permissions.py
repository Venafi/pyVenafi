class Permissions:
    class Permissions:
        def __init__(self, perm_dict: dict):
            if not isinstance(perm_dict, dict):
                perm_dict = {}

            self.is_associate_allowed = perm_dict.get('IsAssociateAllowed', False)
            self.is_create_allowed = perm_dict.get('IsCreateAllowed', False)
            self.is_delete_allowed = perm_dict.get('IsDeleteAllowed', False)
            self.is_manage_permissions_allowed = perm_dict.get('IsManagePermissionsAllowed', False)
            self.is_policy_write_allowed = perm_dict.get('IsPolicyWriteAllowed', False)
            self.is_private_key_read_allowed = perm_dict.get('IsPrivateKeyReadAllowed', False)
            self.is_private_key_write_allowed = perm_dict.get('IsPrivateKeyWriteAllowed', False)
            self.is_read_allowed = perm_dict.get('IsReadAllowed', False)
            self.is_rename_allowed = perm_dict.get('IsRenameAllowed', False)
            self.is_revoke_allowed = perm_dict.get('IsRevokeAllowed', False)
            self.is_view_allowed = perm_dict.get('IsViewAllowed', False)
            self.is_write_allowed = perm_dict.get('IsWriteAllowed', False)
