from typing import Union, List
from pytpp.features.identity import (
    _IdentityBase as _OriginalIdentityBase,
    User as _OriginalUser,
    Group as _OriginalGroup,
    Identity, feature
)
from pytpp.properties.rights import SubSystemTypes


class _IdentityBase(_OriginalIdentityBase):
    def allow_aperture_user_search(self, identity: Union['Identity.Identity', str]):
        """
        Grants Aperture User Search permission to a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        result = self._api.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal,
            rights_value='Impersonate'
        )
        result.assert_valid_response()

    def add_master_admin(self, identity: Union['Identity.Identity', str]):
        """
        Grants Master Admin privileges to a user or group in TPP.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
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
            result = self._api.websdk.Rights.Add.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal,
                rights_value=rights_value
            )
            result.assert_valid_response()

    def allow_websdk_access(self, identity: Union['Identity.Identity', str]):
        """
        Grants WebSDK access to a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        result = self._api.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal,
            rights_value='Allowed'
        )
        result.assert_valid_response()

    def get_rights(self, identity: Union['Identity.Identity', str]):
        """
        Returns all of the special rights granted to a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.

        Returns:
            List of Rights objects.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        return self._api.websdk.Rights.Get.post(universal_id=prefixed_universal).rights

    def remove_aperture_user_search(self, identity: Union['Identity.Identity', str]):
        """
        Removes Aperture User Search permission from a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        result = self._api.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()

    def remove_master_admin(self, identity: Union['Identity.Identity', str]):
        """
        Removes Master Admin privileges from a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
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
            result = self._api.websdk.Rights.Remove.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal
            )
            result.assert_valid_response()

    def remove_websdk_access(self, identity: Union['Identity.Identity', str]):
        """
        Removes WebSDK Access from a user or group.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
        """
        prefixed_universal = self._get_prefixed_universal(identity)
        result = self._api.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()


@feature()
class User(_OriginalUser, _IdentityBase):
    def delete(self, user: Union['Identity.Identity', str]):
        """
        Deletes the user from the Local Identity Provider. The user is removed from all local groups and
        has all rights removed.

        Args:
            user: Identity.Identity or prefixed name of the user. The prefix is required.
        """
        if isinstance(user, str):
            user = self._get_identity_object(user)
        groups = self.get_memberships(identity=user)
        for group in groups:
            result = self._api.websdk.Identity.RemoveGroupMembers.put(
                group=self._identity_dict(prefixed_name=group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            result.assert_valid_response()

        result = self._api.websdk.Rights.Remove.post(
            universal_id=user.prefixed_universal
        )
        result.assert_valid_response()

        self._config_delete(object_dn=f'{self._identity_dn}\\{user.name}')


@feature()
class Group(_OriginalGroup, _IdentityBase):
    def create(self, name: str, member_prefixed_names: List[str] = None, master_admin_group: bool = False,
               allow_websdk_access: bool = False, allow_aperture_user_search: bool = False,
               get_if_already_exists: bool = True):
        """
        Creates a local group in TPP. If ``add_master_admin`` is ``True``, then the group is automatically
        granted Master Admin privileges. The same is true for ``allow_websdk_access`` and
        ``allow_aperture_user_search``. Each member of the group inherits the rights and permissions of this
        group. To add members, provide a list of prefixed names for each member.

        Args:
            name: Name of the user. The `"local:"` prefix is not required.
            member_prefixed_names: List of prefixed universal names of each member.
            master_admin_group: If ``True``, grants Master Admin privileges to the user.
            allow_aperture_user_search: If ``True``, grants Aperture User Search permission to the user.
            allow_websdk_access: If ``True``, grants WebSDK Access to the user.
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            Identity object of the user.
        """
        if not name.startswith('local:'):
            name = f'local:{name}'
        if not isinstance(member_prefixed_names, list):
            member_prefixed_names = []
        if get_if_already_exists:
            if self.exists(prefixed_name=name):
                return self.get(prefixed_name=name)

        result = self._api.websdk.Identity.AddGroup.post(
            name=self._identity_dict(prefixed_name=name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ]
        )

        if member_prefixed_names and result.invalid_members:
            im = "\n\t".join([m.prefixed_name for m in result.invalid_members])
            self._log_warning_message(
                msg=f'Unable to add these members to the group "{name}":\n\t{im}'
            )

        group = result.identity
        if master_admin_group:
            self.add_master_admin(identity=group)

        if allow_websdk_access:
            self.allow_websdk_access(identity=group)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(identity=group)

        return group
