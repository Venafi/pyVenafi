from venafi.tpp.features.identity import (
    _IdentityBase as _OriginalIdentityBase,
    User as _OriginalUser,
    Group as _OriginalGroup,
)
from venafi.tpp.features.bases.feature_base import feature
from venafi.tpp.api.websdk.enums.rights import SubSystemTypes
from typing import Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from venafi.tpp.api.websdk.models import identity as ident
    from venafi.tpp.plugins import Authenticate as PluginsAuthenticate


class _IdentityBase(_OriginalIdentityBase):
    _api: 'PluginsAuthenticate'

    def allow_aperture_user_search(self, identity: Union['ident.Identity', str]):
        """
        Grants Aperture User Search permission to a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        self._api.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal,
            rights_value='Impersonate'
        )

    def add_master_admin(self, identity: Union['ident.Identity', str]):
        """
        Grants Master Admin privileges to a user or group in TPP.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        ved_guid = self._api.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid, 'AllPrivileges'],
            [SubSystemTypes.secret_store_config, ved_guid, '*127'],
            [SubSystemTypes.client, '', 'AllPrivileges'],
            [SubSystemTypes.rights, '', 'Supervisor'],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            self._api.websdk.Rights.Add.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal,
                rights_value=rights_value
            )

    def allow_websdk_access(self, identity: Union['ident.Identity', str]):
        """
        Grants WebSDK access to a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        self._api.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal,
            rights_value='Allowed'
        )

    def get_rights(self, identity: Union['ident.Identity', str]):
        """
        Returns all of the special rights granted to a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.

        Returns:
            List of Rights objects.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        return self._api.websdk.Rights.Get.post(universal_id=prefixed_universal).rights

    def remove_aperture_user_search(self, identity: Union['ident.Identity', str]):
        """
        Removes Aperture User Search permission from a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        self._api.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal
        )

    def remove_master_admin(self, identity: Union['ident.Identity', str]):
        """
        Removes Master Admin privileges from a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        ved_guid = self._api.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid],
            [SubSystemTypes.secret_store_config, ved_guid],
            [SubSystemTypes.client, ''],
            [SubSystemTypes.rights, ''],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            self._api.websdk.Rights.Remove.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal
            )

    def remove_websdk_access(self, identity: Union['ident.Identity', str]):
        """
        Removes WebSDK Access from a user or group.

        Args:
            identity: ident.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        self._api.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal
        )


@feature(_OriginalUser.__feature__)
class User(_OriginalUser, _IdentityBase):
    def create(self, name: str, password: str, email_address: str, add_master_admin: bool = False,
               allow_aperture_user_search: bool = False, allow_websdk_access: bool = False,
               add_to_everyone_group: bool = True, get_if_already_exists: bool = True):
        """
        Creates a local user in TPP with the given ``password`` and ``email_address``. By default, the
        user is added to the Everyone group in the Local Identity Provider. If ``add_master_admin`` is
        ``True``, then the user is automatically enrolled as a Master Admin. The same is true for
        ``allow_websdk_access`` and ``allow_aperture_user_search``.

        Args:
            name: Name of the user. The `"local:"` prefix is not required.
            password: Password.
            email_address: E-mail address. TPP requires it.
            add_master_admin: If ``True``, grants Master Admin privileges to the user.
            allow_aperture_user_search: If ``True``, grants Aperture User Search permission to the user.
            allow_websdk_access: If ``True``, grants WebSDK Access to the user.
            add_to_everyone_group: If ``True``, the user to the Local Identity group "Everyone".
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            Identity object of the user.
        """
        user = super().create(
            name=name, password=password, email_address=email_address,
            get_if_already_exists=get_if_already_exists
        )

        if add_master_admin:
            self.add_master_admin(identity=user)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(identity=user)

        if allow_websdk_access:
            self.allow_websdk_access(identity=user)

        return user

    def delete(self, user: Union['ident.Identity', str]):
        """
        Deletes the user from the Local Identity Provider. The user is removed from all local groups and
        has all rights removed.

        Args:
            user: ident.Identity or prefixed name of the user. The prefix is required.
        """
        if isinstance(user, str):
            user = self._get_identity_object(user)
        groups = self.get_memberships(identity=user)
        for group in groups:
            self._api.websdk.Identity.RemoveGroupMembers.put(
                group=self._identity_dict(prefixed_name=group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
        self._api.websdk.Rights.Remove.post(
            universal_id=user.prefixed_universal
        )
        self._config_delete(object_dn=f'{self._identity_dn}\\{user.name}')


@feature(_OriginalGroup.__name__)
class Group(_OriginalGroup, _IdentityBase):
    def create(self, name: str, members: 'List[Union[ident.Identity, str]]' = None, master_admin_group: bool = False,
               allow_websdk_access: bool = False, allow_aperture_user_search: bool = False,
               get_if_already_exists: bool = True):
        """
        Creates a local group in TPP. If ``add_master_admin`` is ``True``, then the group is automatically
        granted Master Admin privileges. The same is true for ``allow_websdk_access`` and
        ``allow_aperture_user_search``. Each member of the group inherits the rights and permissions of this
        group. To add members, provide a list of prefixed names for each member.

        Args:
            name: Name of the user. The `"local:"` prefix is not required.
            members: List of ``ident.Identity`` or prefixed universal names of each member.
            master_admin_group: If ``True``, grants Master Admin privileges to the user.
            allow_aperture_user_search: If ``True``, grants Aperture User Search permission to the user.
            allow_websdk_access: If ``True``, grants WebSDK Access to the user.
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            Identity object of the user.
        """
        group = super().create(name=name, members=members, get_if_already_exists=get_if_already_exists)
        if master_admin_group:
            self.add_master_admin(identity=group)

        if allow_websdk_access:
            self.allow_websdk_access(identity=group)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(identity=group)

        return group
