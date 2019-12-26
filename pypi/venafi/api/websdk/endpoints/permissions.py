from typing import List 
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.permissions import Permissions


class _Permissions:
    def __init__(self, websdk_obj):
        self.Object = self._Object(websdk_obj=websdk_obj)
        self.Refresh = self._Refresh(websdk_obj=websdk_obj)

    class _Object:
        def __init__(self, websdk_obj):
            self._websdk_obj = websdk_obj

        def Guid(self, guid):
            return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

        class _Guid(API):
            def __init__(self, guid: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/Permissions/Object/{guid}', valid_return_codes=[200])
                self._guid = guid

            @property
            @json_response_property()
            def principals(self) -> List[str]:
                return self._from_json()

            def get(self):
                self.json_response = self._get()
                return self

            def Ptype(self, ptype='Local'):
                return self._Ptype(guid=self._guid, ptype=ptype, websdk_obj=self._api_obj)

            class _Ptype:
                def __init__(self, guid:str, ptype: str, websdk_obj):
                    self._guid = guid
                    self._ptype = ptype
                    self._websdk_obj = websdk_obj

                def Pname(self, pname):
                    return self._Pname(guid=self._guid, ptype=self._ptype, pname=pname, websdk_obj=self._websdk_obj)

                def Principal(self, uuid: str):
                    return self._Principal(guid=self._guid, ptype=self._ptype, uuid=uuid, websdk_obj=self._websdk_obj)

                class _Pname:
                    def __init__(self, guid: str, ptype: str, pname: str, websdk_obj):
                        self._guid = guid
                        self._ptype = ptype
                        self._pname = pname
                        self._websdk_obj = websdk_obj

                    def Principal(self, principal: str):
                        return self._Principal(guid=self._guid, ptype=self._ptype, pname=self._pname,
                                              principal=principal, websdk_obj=self._websdk_obj)

                    class _Principal(API):
                        def __init__(self, guid: str, ptype: str, pname: str, principal: str, websdk_obj):
                            super().__init__(
                                api_obj=websdk_obj,
                                url=f'/Permissions/Object/{guid}/{ptype}/{pname}/{principal}',
                                valid_return_codes=[200]
                            )
                            self.Effective = self._Effective(guid=guid, ptype=ptype, pname=pname, principal=principal, websdk_obj=websdk_obj)

                        @property
                        @json_response_property()
                        def explicit_permissions(self):
                            return Permissions.Permissions(self._from_json(key='ExplicitPermissions'))

                        @property
                        @json_response_property()
                        def implicit_permissions(self):
                            return Permissions.Permissions(self._from_json(key='ImplicitPermissions'))

                        def delete(self):
                            self.json_response = self._delete()
                            return self

                        def get(self):
                            self.json_response = self._get()
                            return self

                        def post(self, is_associate_allowed: bool = False, is_create_allowed: bool = False, is_delete_allowed: bool = False,
                                 is_manage_permissions_allowed: bool = False, is_policy_write_allowed: bool = False,
                                 is_private_key_read_allowed: bool = False, is_private_key_write_allowed: bool = False, is_read_allowed: bool = False,
                                 is_rename_allowed: bool = False, is_revoke_allowed: bool = False, is_view_allowed: bool = False,
                                 is_write_allowed: bool = False):
                            body = {
                                'IsAssociateAllowed': is_associate_allowed,
                                'IsCreateAllowed': is_create_allowed,
                                'IsDeleteAllowed': is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed': is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                                'IsReadAllowed': is_read_allowed,
                                'IsRenameAllowed': is_rename_allowed,
                                'IsRevokeAllowed': is_revoke_allowed,
                                'IsViewAllowed': is_view_allowed,
                                'IsWriteAllowed': is_write_allowed
                            }

                            self.json_response = self._post(data=body)
                            return self

                        def put(self, is_associate_allowed: bool = False, is_create_allowed: bool = False, is_delete_allowed: bool = False,
                                is_manage_permissions_allowed: bool = False, is_policy_write_allowed: bool = False,
                                is_private_key_read_allowed: bool = False, is_private_key_write_allowed: bool = False, is_read_allowed: bool = False,
                                is_rename_allowed: bool = False, is_revoke_allowed: bool = False, is_view_allowed: bool = False,
                                is_write_allowed: bool = False):
                            body = {
                                'IsAssociateAllowed': is_associate_allowed,
                                'IsCreateAllowed': is_create_allowed,
                                'IsDeleteAllowed': is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed': is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                                'IsReadAllowed': is_read_allowed,
                                'IsRenameAllowed': is_rename_allowed,
                                'IsRevokeAllowed': is_revoke_allowed,
                                'IsViewAllowed': is_view_allowed,
                                'IsWriteAllowed': is_write_allowed
                            }

                            self.json_response = self._put(data=body)
                            return self

                        class _Effective(API):
                            def __init__(self, guid: str, ptype: str, pname: str, principal: str, websdk_obj):
                                super().__init__(
                                    api_obj=websdk_obj,
                                    url=f'/Permissions/Object/{guid}/{ptype}/{pname}/{principal}/Effective',
                                    valid_return_codes=[200]
                                )

                            @property
                            @json_response_property()
                            def effective_permissions(self):
                                return Permissions.Permissions(self._from_json('EffectivePermissions'))

                            def get(self):
                                self.json_response = self._get()
                                return self

                class _Principal(API):
                    def __init__(self, guid: str, ptype: str, uuid: str, websdk_obj):
                        super().__init__(
                            api_obj=websdk_obj,
                            url=f'/Permissions/Object/{guid}/{ptype}/{uuid}',
                            valid_return_codes=[200]
                        )
                        self.Effective = self._Effective(guid=guid, uuid=uuid, websdk_obj=websdk_obj)

                    @property
                    @json_response_property()
                    def explicit_permissions(self):
                        return Permissions.Permissions(self._from_json('ExplicitPermissions'))

                    @property
                    @json_response_property()
                    def implicit_permissions(self):
                        return Permissions.Permissions(self._from_json('ImplicitPermissions'))

                    def delete(self):
                        self.json_response = self._delete()
                        return self

                    def get(self):
                        self.json_response = self._get()
                        return self

                    def post(self, is_associate_allowed: bool = False, is_create_allowed: bool = False, is_delete_allowed: bool = False,
                             is_manage_permissions_allowed: bool = False, is_policy_write_allowed: bool = False,
                             is_private_key_read_allowed: bool = False, is_private_key_write_allowed: bool = False, is_read_allowed: bool = False,
                             is_rename_allowed: bool = False, is_revoke_allowed: bool = False, is_view_allowed: bool = False,
                             is_write_allowed: bool = False):
                        body = {
                           'IsAssociateAllowed': is_associate_allowed,
                           'IsCreateAllowed': is_create_allowed,
                           'IsDeleteAllowed': is_delete_allowed,
                           'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                           'IsPolicyWriteAllowed': is_policy_write_allowed,
                           'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                           'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                           'IsReadAllowed': is_read_allowed,
                           'IsRenameAllowed': is_rename_allowed,
                           'IsRevokeAllowed': is_revoke_allowed,
                           'IsViewAllowed': is_view_allowed,
                           'IsWriteAllowed': is_write_allowed
                        }
                        
                        self.json_response = self._post(data=body)
                        
                        return self

                    def put(self, is_associate_allowed: bool = False, is_create_allowed: bool = False, is_delete_allowed: bool = False,
                             is_manage_permissions_allowed: bool = False, is_policy_write_allowed: bool = False,
                             is_private_key_read_allowed: bool = False, is_private_key_write_allowed: bool = False, is_read_allowed: bool = False,
                             is_rename_allowed: bool = False, is_revoke_allowed: bool = False, is_view_allowed: bool = False,
                             is_write_allowed: bool = False):
                        body = {
                            'IsAssociateAllowed': is_associate_allowed,
                            'IsCreateAllowed': is_create_allowed,
                            'IsDeleteAllowed': is_delete_allowed,
                            'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                            'IsPolicyWriteAllowed': is_policy_write_allowed,
                            'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                            'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                            'IsReadAllowed': is_read_allowed,
                            'IsRenameAllowed': is_rename_allowed,
                            'IsRevokeAllowed': is_revoke_allowed,
                            'IsViewAllowed': is_view_allowed,
                            'IsWriteAllowed': is_write_allowed
                        }

                        self.json_response = self._put(data=body)
                        return self

                    class _Effective(API):
                        def __init__(self, guid: str, uuid: str, websdk_obj):
                            super().__init__(
                                api_obj=websdk_obj,
                                url=f'/Permissions/Object/{guid}/Local/{uuid}/Effective',
                                valid_return_codes=[200]
                            )

                        @property
                        @json_response_property()
                        def effective_permissions(self):
                            return Permissions.Permissions(self._from_json('EffectivePermissions'))

                        def get(self):
                            self.json_response = self._get()
                            return self

    class _Refresh(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Permissions/Refresh', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self) -> int:
            return self._from_json('Result')

        def get(self):
            self.json_response = self._get()
            return self
