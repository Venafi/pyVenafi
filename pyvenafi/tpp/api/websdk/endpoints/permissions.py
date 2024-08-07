from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import (
    identity as ident,
    permissions,
)

class _Permissions(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Permissions')
        self.Object = self._Object(api_obj=self._api_obj, url=f'{self._url}/Object')
        self.Refresh = self._Refresh(api_obj=self._api_obj, url=f'{self._url}/Refresh')

        self.GetPrincipals = self._GetPrincipals(api_obj=self._api_obj, url=f'{self._url}/GetPrincipals')
        self.GetPermissions = self._GetPermissions(api_obj=self._api_obj, url=f'{self._url}/GetPermissions')
        self.GetEffectivePermissions = self._GetEffectivePermissions(
            api_obj=self._api_obj,
            url=f'{self._url}/GetEffectivePermissions'
        )
        self.GrantPermissions = self._GrantPermissions(api_obj=self._api_obj, url=f'{self._url}/GrantPermissions')
        self.RevokePermissions = self._RevokePermissions(api_obj=self._api_obj, url=f'{self._url}/RevokePermissions')
        self.ReplacePermissions = self._ReplacePermissions(api_obj=self._api_obj, url=f'{self._url}/ReplacePermissions')

    class _Object(WebSdkEndpoint):
        def Guid(self, guid):
            return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(WebSdkEndpoint):
            def get(self):
                class Output(WebSdkOutputModel):
                    principals: list[str] = ApiField(default_factory=list)

                return generate_output(output_cls=Output, response=self._get(), root_field='principals')

            def Ptype(self, ptype='Local'):
                return self._Ptype(api_obj=self._api_obj, url=f'{self._url}/{ptype}')

            class _Ptype(WebSdkEndpoint):
                def Pname(self, pname):
                    return self._Pname(api_obj=self._api_obj, url=f'{self._url}/{pname}')

                def Principal(self, uuid: str):
                    return self._Principal(api_obj=self._api_obj, url=f'{self._url}/{uuid}')

                class _Pname(WebSdkEndpoint):
                    def Principal(self, principal: str):
                        return self._Principal(api_obj=self._api_obj, url=f'{self._url}/{principal}')

                    class _Principal(WebSdkEndpoint):
                        def __init__(self, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.Effective = self._Effective(api_obj=self._api_obj, url=f'{self._url}/Effective')

                        def delete(self):
                            return generate_output(output_cls=WebSdkOutputModel, response=self._delete())

                        def get(self):
                            class Output(WebSdkOutputModel):
                                explicit_permissions: permissions.Permissions = ApiField(alias='ExplicitPermissions')
                                implicit_permissions: permissions.Permissions = ApiField(alias='ImplicitPermissions')

                            return generate_output(output_cls=Output, response=self._get())

                        def post(
                            self,
                            is_associate_allowed: bool = None,
                            is_create_allowed: bool = None,
                            is_delete_allowed: bool = None,
                            is_manage_permissions_allowed: bool = None,
                            is_policy_write_allowed: bool = None,
                            is_private_key_read_allowed: bool = None,
                            is_private_key_write_allowed: bool = None,
                            is_read_allowed: bool = None,
                            is_rename_allowed: bool = None,
                            is_revoke_allowed: bool = None,
                            is_view_allowed: bool = None,
                            is_write_allowed: bool = None
                        ):
                            body = {
                                'IsAssociateAllowed'        : is_associate_allowed,
                                'IsCreateAllowed'           : is_create_allowed,
                                'IsDeleteAllowed'           : is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed'      : is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed'   : is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed'  : is_private_key_write_allowed,
                                'IsReadAllowed'             : is_read_allowed,
                                'IsRenameAllowed'           : is_rename_allowed,
                                'IsRevokeAllowed'           : is_revoke_allowed,
                                'IsViewAllowed'             : is_view_allowed,
                                'IsWriteAllowed'            : is_write_allowed
                            }

                            return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

                        def put(
                            self,
                            is_associate_allowed: bool = None,
                            is_create_allowed: bool = None,
                            is_delete_allowed: bool = None,
                            is_manage_permissions_allowed: bool = None,
                            is_policy_write_allowed: bool = None,
                            is_private_key_read_allowed: bool = None,
                            is_private_key_write_allowed: bool = None,
                            is_read_allowed: bool = None,
                            is_rename_allowed: bool = None,
                            is_revoke_allowed: bool = None,
                            is_view_allowed: bool = None,
                            is_write_allowed: bool = None
                        ):
                            body = {
                                'IsAssociateAllowed'        : is_associate_allowed,
                                'IsCreateAllowed'           : is_create_allowed,
                                'IsDeleteAllowed'           : is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed'      : is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed'   : is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed'  : is_private_key_write_allowed,
                                'IsReadAllowed'             : is_read_allowed,
                                'IsRenameAllowed'           : is_rename_allowed,
                                'IsRevokeAllowed'           : is_revoke_allowed,
                                'IsViewAllowed'             : is_view_allowed,
                                'IsWriteAllowed'            : is_write_allowed
                            }

                            return generate_output(output_cls=WebSdkOutputModel, response=self._put(data=body))

                        class _Effective(WebSdkEndpoint):
                            def get(self):
                                class Output(WebSdkOutputModel):
                                    effective_permissions: permissions.Permissions = ApiField(
                                        alias='EffectivePermissions'
                                    )

                                return generate_output(output_cls=Output, response=self._get())

                class _Principal(WebSdkEndpoint):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.Effective = self._Effective(api_obj=self._api_obj, url=f'{self._url}/Effective')

                    def delete(self):
                        return generate_output(output_cls=WebSdkOutputModel, response=self._delete())

                    def get(self):
                        class Output(WebSdkOutputModel):
                            explicit_permissions: permissions.Permissions = ApiField(alias='ExplicitPermissions')
                            implicit_permissions: permissions.Permissions = ApiField(alias='ImplicitPermissions')

                        return generate_output(output_cls=Output, response=self._get())

                    def post(
                        self,
                        is_associate_allowed: bool = None,
                        is_create_allowed: bool = None,
                        is_delete_allowed: bool = None,
                        is_manage_permissions_allowed: bool = None,
                        is_policy_write_allowed: bool = None,
                        is_private_key_read_allowed: bool = None,
                        is_private_key_write_allowed: bool = None,
                        is_read_allowed: bool = None,
                        is_rename_allowed: bool = None,
                        is_revoke_allowed: bool = None,
                        is_view_allowed: bool = None,
                        is_write_allowed: bool = None
                    ):
                        body = {
                            'IsAssociateAllowed'        : is_associate_allowed,
                            'IsCreateAllowed'           : is_create_allowed,
                            'IsDeleteAllowed'           : is_delete_allowed,
                            'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                            'IsPolicyWriteAllowed'      : is_policy_write_allowed,
                            'IsPrivateKeyReadAllowed'   : is_private_key_read_allowed,
                            'IsPrivateKeyWriteAllowed'  : is_private_key_write_allowed,
                            'IsReadAllowed'             : is_read_allowed,
                            'IsRenameAllowed'           : is_rename_allowed,
                            'IsRevokeAllowed'           : is_revoke_allowed,
                            'IsViewAllowed'             : is_view_allowed,
                            'IsWriteAllowed'            : is_write_allowed
                        }

                        return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

                    def put(
                        self,
                        is_associate_allowed: bool = None,
                        is_create_allowed: bool = None,
                        is_delete_allowed: bool = None,
                        is_manage_permissions_allowed: bool = None,
                        is_policy_write_allowed: bool = None,
                        is_private_key_read_allowed: bool = None,
                        is_private_key_write_allowed: bool = None,
                        is_read_allowed: bool = None,
                        is_rename_allowed: bool = None,
                        is_revoke_allowed: bool = None,
                        is_view_allowed: bool = None,
                        is_write_allowed: bool = None
                    ):
                        body = {
                            'IsAssociateAllowed'        : is_associate_allowed,
                            'IsCreateAllowed'           : is_create_allowed,
                            'IsDeleteAllowed'           : is_delete_allowed,
                            'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                            'IsPolicyWriteAllowed'      : is_policy_write_allowed,
                            'IsPrivateKeyReadAllowed'   : is_private_key_read_allowed,
                            'IsPrivateKeyWriteAllowed'  : is_private_key_write_allowed,
                            'IsReadAllowed'             : is_read_allowed,
                            'IsRenameAllowed'           : is_rename_allowed,
                            'IsRevokeAllowed'           : is_revoke_allowed,
                            'IsViewAllowed'             : is_view_allowed,
                            'IsWriteAllowed'            : is_write_allowed
                        }

                        return generate_output(output_cls=WebSdkOutputModel, response=self._put(data=body))

                    class _Effective(WebSdkEndpoint):
                        def get(self):
                            class Output(WebSdkOutputModel):
                                effective_permissions: permissions.Permissions = ApiField(alias='EffectivePermissions')

                            return generate_output(output_cls=Output, response=self._get())

    class _Refresh(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')

            return generate_output(output_cls=Output, response=self._get())

    class _GetPrincipals(WebSdkEndpoint):
        def post(self, object_dn: str = None, object_guid: str = None):
            body = {
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')
                principals: list[ident.Identity] = ApiField(alias='Principals')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetPermissions(WebSdkEndpoint):
        def post(
            self,
            principal: str = None,
            object_dn: str = None,
            object_guid: str = None,
        ):
            body = {
                "Principal" : principal,
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')
                permissions: permissions.Permissions = ApiField(alias='Permissions')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetEffectivePermissions(WebSdkEndpoint):
        def post(
            self,
            principal: str = None,
            object_dn: str = None,
            object_guid: str = None,
        ):
            body = {
                "Principal" : principal,
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')
                permissions: permissions.Permissions = ApiField(alias='Permissions')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GrantPermissions(WebSdkEndpoint):
        def post(
            self,
            principal: str = None,
            object_dn: str = None,
            object_guid: str = None,
        ):
            body = {
                "Principal" : principal,
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RevokePermissions(WebSdkEndpoint):
        def post(
            self,
            principal: str = None,
            object_dn: str = None,
            object_guid: str = None,
        ):
            body = {
                "Principal" : principal,
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ReplacePermissions(WebSdkEndpoint):
        def post(
            self,
            principal: str = None,
            object_dn: str = None,
            object_guid: str = None,
        ):
            body = {
                "Principal" : principal,
                "ObjectDN"  : object_dn,
                "ObjectGuid": object_guid,
            }

            class Output(WebSdkOutputModel):
                result: int = ApiField(alias='Result')

            return generate_output(output_cls=Output, response=self._post(data=body))
