from pytpp.attributes.user import UserAttributes
from pytpp.properties.config import IdentityAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import UnexpectedValue
from pytpp.features.definitions.classes import Classes
from typing import List, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Identity


class _IdentityBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._identity_dn = r'\VED\Identity'

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
        identity_type = 0
        if is_user:
            identity_type += IdentityAttributeValues.Types.user
        if is_security_group:
            identity_type += IdentityAttributeValues.Types.security_group
        if is_distribution_group:
            identity_type += IdentityAttributeValues.Types.distribution_group

        result = self._api.websdk.Identity.Browse.post(
            filter=name,
            limit=limit,
            identity_type=identity_type
        )
        return result.identities

    def exists(self, prefixed_name: str):
        """
        Validates that a user or group exists in TPP and returns a boolean value.

        Args:
            prefixed_name: The prefixed name of the Identity object.

        Returns:
            ``True`` if the Identity exists, otherwise ``False``.
        """
        response = self._api.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        )
        response.assert_valid_response()
        if response.api_response.content:
            return response.identity.prefixed_name == prefixed_name
        return False

    def get(self, prefixed_name: str = None, prefixed_universal: str = None, raise_error_if_not_exists: bool = True):
        """
        Get a user or group in TPP. An error is raised if the identity does not exist.

        One of ``prefixed_name`` or ``prefixed_universal`` must be provided.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            prefixed_universal: The prefixed universal GUID of the Identity object.
            raise_error_if_not_exists: Raise an exception if the identity does not exist.

        Returns:
            An Identity object of the user or group.
        """
        return self._get_identity_object(
            prefixed_name=prefixed_name,
            prefixed_universal=prefixed_universal,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def get_memberships(self, identity: 'Union[Identity.Identity, str]'):
        """
        Finds all groups to which a user or group belongs.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.

        Returns:
            List of Identity objects for each group.
        """
        if isinstance(identity, str):
            identity = self._get_identity_object(prefixed_name=identity)
        memberships = self._api.websdk.Identity.GetMemberships.post(
            identity=self._identity_dict(
                prefixed_name=identity.prefixed_name,
                prefixed_universal=identity.prefixed_universal
            )
        ).identities

        return memberships

    def read_attribute(self, identity: 'Union[Identity.Identity, str]', attribute_name: str):
        """
        Returns the value associated to the given ``attribute_name``.

        Args:
            identity: Identity.Identity or prefixed name of the user or group. The prefix is required.
            attribute_name: The name of the attribute.

        Returns:
            List of attribute values.
        """
        prefixed_name = self._get_prefixed_name(identity)
        result = self._api.websdk.Identity.ReadAttribute.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            attribute_name=attribute_name
        )
        return result.attributes


@feature('User')
class User(_IdentityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, password: str, email_address: str, first_name: str = None, last_name: str = None,
               add_to_everyone_group: bool = True, get_if_already_exists: bool = True):
        """
        Creates a local user in TPP with the given ``password`` and ``email_address``. By default, the
        user is added to the Everyone group in the Local Identity Provider.

        Args:
            name: Name of the user. The `"local:"` prefix is not required.
            password: Password.
            email_address: E-mail address. TPP requires it.
            first_name: First name of the user.
            last_name: Last name of the user.
            add_to_everyone_group: If ``True``, the user to the Local Identity group "Everyone".
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            Identity object of the user.
        """
        attributes = {
            UserAttributes.internet_email_address: email_address,
            UserAttributes.given_name: first_name,
            UserAttributes.surname: last_name
        }
        user = self._config_create(
            name=name,
            parent_folder_dn=self._identity_dn,
            config_class=Classes.user,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )
        user = self.set_password(user=f'local:{user.name}', new_password=password)

        if add_to_everyone_group:
            response = self._api.websdk.Identity.AddGroupMembers.put(
                group=self._identity_dict(prefixed_name='local:Everyone'),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            response.assert_valid_response()
        return user

    def delete(self, user: 'Union[Identity.Identity, str]'):
        """
        Deletes the user from the Local Identity Provider. The user is removed from all local groups.

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

    def set_password(self, user: 'Union[Identity.Identity, str]', new_password: str, old_password: str = None):
        """
        Sets the ``new_password`` for a local user. If the user did not have a previous password, then
        the ``old_password`` is not required.

        Args:
            user: Identity.Identity or prefixed name of the user. The prefix is required.
            new_password: The new password for the user.
            old_password: The old password for the user. Required only if it exists.

        Returns:
            Identity object of the user.
        """
        prefixed_name = self._get_prefixed_name(user)
        response = self._api.websdk.Identity.SetPassword.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            old_password=old_password,
            password=new_password
        )
        return response.identity


@feature('Group')
class Group(_IdentityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def add_members(self, group: 'Union[Identity.Identity, str]', members: 'List[Union[Identity.Identity, str]]'):
        """
        Adds members to a local group.

        Args:
            group: Identity.Identity or prefixed name of the group. The prefix is required.
            members: List of ``Identity.Identity`` or prefixed names of each member.

        Returns:
            List of Identity objects for each member.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members]
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.AddGroupMembers.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        if member_prefixed_names and result.invalid_members:
            im = "\n\t".join([m.prefixed_name for m in result.invalid_members])
            raise UnexpectedValue(
                f'Unable to add these members to the group "{prefixed_name}":\n\t{im}'
            )

        return result.members

    def create(self, name: str, members: 'List[Union[Identity, Identity, str]]' = None, get_if_already_exists: bool = True):
        """
        Creates a local group in TPP. Each member of the group inherits the permissions of this
        group. To add members, provide a list of prefixed names for each member.

        Args:
            name: Name of the user. The `"local:"` prefix is not required.
            members: List of ``Identity.Identity`` or prefixed universal names of each member.
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            Identity object of the user.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members] if members else []
        if not name.startswith('local:'):
            name = f'local:{name}'
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
        return group

    def delete(self, group: 'Union[Identity.Identity, str]'):
        """
        Deletes a group, but not its members. All group permissions and privileges are deleted.

        Args:
            group: Identity.Identity or prefixed name of the group. The prefix is required.
        """
        if isinstance(group, str):
            group = self._get_identity_object(group)
        result = self._api.websdk.Identity.Group.Prefix(group.prefix).Principal(group.universal).delete()
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

    def get_members(self, group: 'Union[Identity.Identity, str]', resolve_nested: bool = False):
        """
        Finds all members of a group. If ``resolve_nested`` is ``True``, then members of groups within this group, etc.,
        are included in the result.

        Args:
            group: Identity.Identity or prefixed name of the group. The prefix is required.
            resolve_nested: If ``True``, returns members of nested groups within this group.

        Returns:
            List of Identity objects for each member of the group.
        """
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.GetMembers.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            resolve_nested=int(resolve_nested)
        )

        return result.identities

    def remove_members(self, group: 'Union[Identity.Identity, str]', members: 'List[Union[Identity.Identity, str]]'):
        """
        Removes members from a local group.

        Args:
            group: Identity.Identity or prefixed name of the group. The prefix is required.
            members: List of ``Identity.Identity`` or prefixed universal names of each member.

        Returns:
            List of Identity objects for each remaining member. If no members remain, then
            the list is empty.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members]
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.RemoveGroupMembers.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        return result.members

    def rename(self, group: 'Union[Identity.Identity, str]', new_group_name: str):
        """
        Renames a local group. The `"local:"` prefix is not required.

        Args:
            group: Identity.Identity or prefixed name of the group. The prefix is required.
            new_group_name: New name of the group. No prefix required.

        Returns:
            Identity object with the new group name.
        """
        prefixed_name = self._get_prefixed_name(group)
        if not new_group_name.startswith('local:'):
            new_group_name = new_group_name.lstrip('local:')

        result = self._api.websdk.Identity.RenameGroup.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            new_group_name=new_group_name
        )

        return result.identity
