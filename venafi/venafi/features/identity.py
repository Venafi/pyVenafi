from typing import List
from venafi.properties.config import IdentityClassNames, IdentityAttributes, IdentityAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.rights import SubSystemTypes


class _IdentityBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._identity_dn = r'\VED\Identity'

    def allow_aperture_user_search(self, prefixed_universal: str):
        """
        Grants Aperture User Search permission to a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal,
            rights_value='Impersonate'
        )
        result.assert_valid_response()

    def add_master_admin(self, prefixed_universal: str):
        """
        Grants Master Admin privileges to a user or group in TPP.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.
        """

        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ved_guid = self._auth.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid, 'AllPrivileges'],
            [SubSystemTypes.secret_store_config, ved_guid, '*127'],
            [SubSystemTypes.client, '', 'AllPrivileges'],
            [SubSystemTypes.rights, '', 'Supervisor'],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            result = self._auth.websdk.Rights.Add.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal,
                rights_value=rights_value
            )
            result.assert_valid_response()

    def allow_websdk_access(self, prefixed_universal: str):
        """
        Grants WebSDK access to a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:

        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal,
            rights_value='Allowed'
        )
        result.assert_valid_response()

    def _find(self, name: str, limit: int = 100, is_distribution_group: bool = False, is_security_group: bool = False,
              is_user: bool = False):
        """
        Finds users and/or groups within the Identity Provider permissions of the caller having containing ``name`` within
        its name. If the caller is an AD user and has permissions to view the Local Identity Provider in TPP, then that
        user will be able to search for both users and groups within its own AD Identity Provider and the Local Identity
        Provider.

        Result can be filtered by group types (Security and/or Distribution groups) and be limited to a certain number of
        results.

        Examples:

            .. code-block::python

            cool_groups = self.features.identity.group.find(name='CoolGroup', limit=2)
            cool_users = self.features.identity.user.find(name='CoolUser', limit=20)

        Args:
            name: String of characters contained within the names to be found.
            limit: Maximum number of results to return.
            is_distribution_group: If ``True``, results include AD Distribution Groups.
            is_security_group: If ``True``, results include Local and AD/LDAP groups.
            is_user: If ``True``, results include Local and AD/LDAP users.

        Returns:
            List of Identity objects for each identity found.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        identity_type = 0
        if is_user:
            identity_type += IdentityAttributes.Types.user
        if is_security_group:
            identity_type += IdentityAttributes.Types.security_group
        if is_distribution_group:
            identity_type += IdentityAttributes.Types.distribution_group

        result = self._auth.websdk.Identity.Browse.post(
            filter=name,
            limit=limit,
            identity_type=identity_type
        )
        return result.identities

    def exists(self, prefixed_name: str = None):
        """
        Validates that a user or group exists in TPP and returns a boolean value. To enforce that
        a user or group exists by throwing an error if it does not, use :meth:`validate`.

        Args:
            prefixed_name: The prefixed name of the Identity object.

        Returns:
            ``True`` if the Identity exists, otherwise ``False``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        )
        response.assert_valid_response()
        if response.json_response.content:
            return response.identity.prefixed_name == prefixed_name
        return False

    def get_memberships(self, prefixed_name: str = None):
        """
        Finds all groups to which a user or group belongs.

        Args:
            prefixed_name: The prefixed name of the Identity object.

        Returns:
            List of Identity objects for each group.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        memberships = self._auth.websdk.Identity.GetMemberships.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        ).identities

        return memberships

    def get_rights(self, prefixed_universal: str):
        """
        Returns all of the special rights granted to a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:
            List of Rights objects.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._auth.websdk.Rights.Get.post(universal_id=prefixed_universal).rights

    def read_attribute(self, prefixed_name: str, attribute_name: str):
        """
        Returns the value associated to the given ``attribute_name``.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            attribute_name: The name of the attribute.

        Returns:
            List of attribute values.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Identity.ReadAttribute.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            attribute_name=attribute_name
        )
        return result.attributes

    def remove_aperture_user_search(self, prefixed_universal: str):
        """
        Removes Aperture User Search permission from a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()

    def remove_master_admin(self, prefixed_universal: str):
        """
        Removes Master Admin privileges from a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ved_guid = self._auth.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid],
            [SubSystemTypes.secret_store_config, ved_guid],
            [SubSystemTypes.client, ''],
            [SubSystemTypes.rights, ''],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            result = self._auth.websdk.Rights.Remove.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal
            )
            result.assert_valid_response()

    def remove_websdk_access(self, prefixed_universal: str):
        """
        Removes WebSDK Access from a user or group.

        Args:
            prefixed_universal: The prefixed universal GUID of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()

    def validate(self, prefixed_name: str = None, prefixed_universal: str = None):
        """
        Validates that a user or group exists in TPP. If it does, then the Identity object is
        returned. Otherwise an error is thrown. If throwing an error is not desired, use
        :meth:`exists` to obtain a boolean value.

        One of ``prefixed_name`` or ``prefixed_universal`` must be provided.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:
            If validated, the Identity object. Otherwise an error is thrown.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        identity = self._auth.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name, prefixed_universal=prefixed_universal)
        ).identity

        return identity

    @staticmethod
    def _identity_dict(prefixed_name: str = None, prefixed_universal: str = None):
        """
        Creates an ID object to write to the Identity APIs.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:
            {
                'PrefixedUniversal': ``prefixed_universal``,
                'PrefixedName': ``prefixed_name``
            }
        """

        d = {}
        if prefixed_name:
            d.update({'PrefixedName': prefixed_name})
        if prefixed_universal:
            d.update({'PrefixedUniversal': prefixed_universal})
        return d


@feature()
class User(_IdentityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, password: str, email_address: str, add_master_admin: bool = False,
               allow_aperture_user_search: bool = False, allow_websdk_access: bool = False,
               add_to_everyone_group: bool = True):
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

        Returns:
            Identity object of the user.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        attributes = {
            'Internet Email Address': email_address
        }
        user = self._config_create(
            name=name,
            parent_folder_dn=self._identity_dn,
            config_class=IdentityClassNames.user,
            attributes=attributes,
        )
        user = self.validate(prefixed_name=f'local:{user.name}')
        self.set_password(prefixed_name=user.prefixed_name, new_password=password)

        if add_to_everyone_group:
            everyone_group = self.validate(prefixed_name='local:Everyone')
            response = self._auth.websdk.Identity.AddGroupMembers.put(
                group=self._identity_dict(prefixed_name=everyone_group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            response.assert_valid_response()

        if add_master_admin:
            self.add_master_admin(prefixed_universal=user.prefixed_universal)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(prefixed_universal=user.prefixed_universal)

        if allow_websdk_access:
            self.allow_websdk_access(prefixed_universal=user.prefixed_universal)

        return user

    def delete(self, prefixed_name: str):
        """
        Deletes the user from the Local Identity Provider. The user is removed from all local groups and
        has all rights removed.

        Args:
            prefixed_name: The prefixed name of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        user = self.validate(prefixed_name=prefixed_name)

        groups = self.get_memberships(prefixed_name=user.prefixed_name)
        for group in groups:
            result = self._auth.websdk.Identity.RemoveGroupMembers.put(
                group=self._identity_dict(prefixed_name=group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            result.assert_valid_response()

        result = self._auth.websdk.Rights.Remove.post(
            universal_id=user.prefixed_universal
        )
        result.assert_valid_response()

        self._config_delete(object_dn=f'{self._identity_dn}\\{user.name}')

    def find(self, name: str, limit: int = 100):
        """
        Finds users within the Identity Provider permissions of the caller having containing ``name`` within its name.
        If the caller is an AD user and has permissions to view the Local Identity Provider in TPP, then that user
        will be able to search for users within its own AD Identity Provider and the Local Identity Provider.

        Result can be limited to a certain number of results.

        Examples:

            .. code-block::python

            cool_users = self.features.identity.user.find(name='CoolUser', limit=20)

        Args:
            name: String of characters contained within the names to be found.
            limit: Maximum number of results to return.

        Returns:
            List of Identity objects for each identity found.
        """
        return self._find(
            name=name,
            limit=limit,
            is_distribution_group=False,
            is_security_group=False,
            is_user=True
        )

    def set_password(self, prefixed_name: str, new_password: str, old_password: str = None):
        """
        Sets the password for a local user. If the user did not have a previous password, then
        the ``old_password`` is not required.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            new_password: The new password for the user.
            old_password: The old password for the user. Required only if it exists.

        Returns:
            Identity object of the user.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Identity.SetPassword.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            old_password=old_password,
            password=new_password
        )
        return response.identity


@feature()
class Group(_IdentityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def add_members(self, group_prefixed_name: str, member_prefixed_names: List[str]):
        """
        Adds members to a local group.

        Args:
            group_prefixed_name: The prefixed name of the group.
            member_prefixed_names: List of prefixed universal names of each member.

        Returns:
            List of Identity objects for each member.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Identity.AddGroupMembers.put(
            group=self._identity_dict(prefixed_name=group_prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        if member_prefixed_names and result.invalid_members:
            im = "\n\t".join([m.prefixed_name for m in result.invalid_members])
            raise FeatureError.UnexpectedValue(
                f'Unable to add these members to the group "{group_prefixed_name}":\n\t{im}'
            )

        return result.members

    def create(self, name: str, member_prefixed_names: List[str] = None, master_admin_group: bool = False,
               allow_websdk_access: bool = False, allow_aperture_user_search: bool = False):
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

        Returns:
            Identity object of the user.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not name.startswith('local:'):
            name = f'local:{name}'
        if not isinstance(member_prefixed_names, list):
            member_prefixed_names = []

        result = self._auth.websdk.Identity.AddGroup.post(
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
            self.add_master_admin(prefixed_universal=group.prefixed_universal)

        if allow_websdk_access:
            self.allow_websdk_access(prefixed_universal=group.prefixed_universal)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(prefixed_universal=group.prefixed_universal)

        return group

    def delete(self, prefixed_universal: str):
        """
        Deletes a group, but not its members. All group permissions and privileges are deleted.

        Args:
            prefixed_universal: The prefixed universal GUID of the group.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        prefix, universal = prefixed_universal.split(':', 1)
        result = self._auth.websdk.Identity.Group.Prefix(prefix).Principal(universal).delete()
        result.assert_valid_response()

    def find(self, name: str, limit: int = 100, is_distribution_group: bool = False, is_security_group: bool = True):
        """
        Finds groups within the Identity Provider permissions of the caller having containing ``name`` within its name.
        If the caller is an AD user and has permissions to view the Local Identity Provider in TPP, then that user will
        be able to search for groups within its own AD Identity Provider and the Local Identity Provider.

        Result can be filtered by group types (Security and/or Distribution groups) and be limited to a certain number of
        results.

        Examples:

            .. code-block::python

            cool_groups = self.features.identity.group.find(name='CoolGroup', limit=2)

        Args:
            name: String of characters contained within the names to be found.
            limit: Maximum number of results to return.
            is_distribution_group: If ``True``, results include AD Distribution Groups.
            is_security_group: If ``True``, results include Local and AD/LDAP groups.

        Returns:
            List of Identity objects for each identity found.
        """
        return self._find(
            name=name,
            limit=limit,
            is_distribution_group=is_distribution_group,
            is_security_group=is_security_group,
            is_user=False
        )

    def get_members(self, group_prefixed_name: str, resolve_nested: bool = False):
        """
        Finds all members of a group. If ``resolve_nested`` is ``True``, then members of groups within this group, etc.,
        are included in the result.

        Args:
            group_prefixed_name: The prefixed universal GUID of the group.
            resolve_nested: If ``True``, returns members of nested groups within this group.

        Returns:
            List of Identity objects for each member of the group.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Identity.GetMembers.post(
            identity=self._identity_dict(prefixed_name=group_prefixed_name),
            resolve_nested=int(resolve_nested)
        )

        return result.identities

    def remove_members(self, group_prefixed_name: str, member_prefixed_names: List[str]):
        """
        Removes members from a local group.

        Args:
            group_prefixed_name: The prefixed name of the group.
            member_prefixed_names: List of prefixed universal names of each member.

        Returns:
            List of Identity objects for each remaining member. If no members remain, then
            the list is empty.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Identity.RemoveGroupMembers.put(
            group=self._identity_dict(prefixed_name=group_prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        return result.members

    def rename(self, group_prefixed_name: str, new_group_name: str):
        """
        Renames a local group. The `"local:"` prefix is not required.

        Args:
            group_prefixed_name: Name of the local group.
            new_group_name: New name of the group. No prefix required.

        Returns:
            Identity object with the new group name.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not new_group_name.startswith('local:'):
            new_group_name = new_group_name.lstrip('local:')

        result = self._auth.websdk.Identity.RenameGroup.put(
            group=self._identity_dict(prefixed_name=group_prefixed_name),
            new_group_name=new_group_name
        )

        return result.identity
