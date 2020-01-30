class Permissions:
    class Permissions:
        def __init__(self, perm_dict: dict):
            if not isinstance(perm_dict, dict):
                perm_dict = {}

            self.is_associate_allowed = perm_dict.get('IsAssociateAllowed')
            self.is_create_allowed = perm_dict.get('IsCreateAllowed')
            self.is_delete_allowed = perm_dict.get('IsDeleteAllowed')
            self.is_manage_permissions_allowed = perm_dict.get('IsManagePermissionsAllowed')
            self.is_policy_write_allowed = perm_dict.get('IsPolicyWriteAllowed')
            self.is_private_key_read_allowed = perm_dict.get('IsPrivateKeyReadAllowed')
            self.is_private_key_write_allowed = perm_dict.get('IsPrivateKeyWriteAllowed')
            self.is_read_allowed = perm_dict.get('IsReadAllowed')
            self.is_rename_allowed = perm_dict.get('IsRenameAllowed')
            self.is_revoke_allowed = perm_dict.get('IsRevokeAllowed')
            self.is_view_allowed = perm_dict.get('IsViewAllowed')
            self.is_write_allowed = perm_dict.get('IsWriteAllowed')
