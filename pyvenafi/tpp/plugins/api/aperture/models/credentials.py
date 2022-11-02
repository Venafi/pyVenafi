from __future__ import annotations
from pyvenafi.tpp.api.api_base import ObjectModel, ApiField
from typing import List
from datetime import datetime


class Permissions(ObjectModel):
    is_associate_allowed: bool = ApiField(alias='isAssociateAllowed')
    is_auditor: bool = ApiField(alias='isAuditor')
    is_create_allowed: bool = ApiField(alias='isCreateAllowed')
    is_delete_allowed: bool = ApiField(alias='isDeleteAllowed')
    is_manage_permissions_allowed: bool = ApiField(alias='isManagePermissionsAllowed')
    is_policy_write_allowed: bool = ApiField(alias='isPolicyWriteAllowed')
    is_private_key_read_allowed: bool = ApiField(alias='isPrivateKeyReadAllowed')
    is_private_key_write_allowed: bool = ApiField(alias='isPrivateKeyWriteAllowed')
    is_read_allowed: bool = ApiField(alias='isReadAllowed')
    is_rename_allowed: bool = ApiField(alias='isRenameAllowed')
    is_revoke_allowed: bool = ApiField(alias='isRevokeAllowed')
    is_view_allowed: bool = ApiField(alias='isViewAllowed')
    is_write_allowed: bool = ApiField(alias='isWriteAllowed')
    principal: str = ApiField(alias='principal')


class CredentialDetails(ObjectModel):
    contacts: List[str] = ApiField(alias='contacts', default_factory=list)
    created_on: datetime = ApiField(alias='createdOn')
    description: str = ApiField(alias='description')
    id: str = ApiField(alias='id')
    name: str = ApiField(alias='name')
    parentDn: str = ApiField(alias='parentDn')
    schema_class: str = ApiField(alias='schemaClass')
    single_click_actions: List[str] = ApiField(alias='singleClickActions', default_factory=list)
