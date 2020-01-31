from venafi.features.bases.feature_base import FeatureBase, ApiPreferences, feature
from venafi.properties.response_objects.permissions import Permissions as PermResponseObj


@feature()
class Permissions(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str, identity_prefixed_universal: str):
        """
        Deletes all explicit permissions granted to a user or group on the ``object_dn``. All implicit permissions,
        i.e. those that are inherited from group memberships and parent folders, are unaffected.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.
            identity_prefixed_universal: The prefixed name of the Identity object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        current_permissions = self.get_explicit(object_dn=object_dn, identity_prefixed_universal=identity_prefixed_universal)
        if not current_permissions:
            return

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        prefix, universal = identity_prefixed_universal.split(':', 1)  # type: str, str
        if '+' in prefix:
            ptype, pname = prefix.split('+', 1)
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype(ptype).Pname(pname).Principal(universal)
        else:
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype().Principal(universal)

        result = api.delete()
        result.assert_valid_response()

    def get_effective(self, object_dn: str, identity_prefixed_universal: str):
        """
        Returns the `effective` permissions of a user or group on the ``object_dn``. Effective permissions are the
        permissions that are `effectively` enforced by TPP. All Master Admin, implicit, and explicit permissions
        are taken into account to evaluate the final effective permissions of a user or group.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.
            identity_prefixed_universal: The prefixed name of the Identity object.

        Returns:
            Effective Permissions object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        prefix, universal = identity_prefixed_universal.split(':', 1)  # type: str, str
        if '+' in prefix:
            ptype, pname = prefix.split('+', 1)
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype(ptype).Pname(pname).Principal(universal)
        else:
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype().Principal(universal)

        result = api.Effective.get()
        return result.effective_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_explicit(self, object_dn: str, identity_prefixed_universal: str):
        """
        Returns the `explicit` permissions of a user or group on the ``object_dn``. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored. To get implicit permissions, use
        :meth:`get_implicit`.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.
            identity_prefixed_universal: The prefixed name of the Identity object.

        Returns:
            Explicit Permissions object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        prefix, universal = identity_prefixed_universal.split(':', 1)  # type: str, str
        if '+' in prefix:
            ptype, pname = prefix.split('+', 1)
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype(ptype).Pname(pname).Principal(universal)
        else:
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype().Principal(universal)

        result = api.get()
        return result.explicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_implicit(self, object_dn: str, identity_prefixed_universal: str):
        """
        Returns the `implicit` permissions of a user or group on the ``object_dn``. Implicit permissions are permissions
        inherited from other folders and group memberships. To get explicit permissions, use :meth:`get_explicit`.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.
            identity_prefixed_universal: The prefixed name of the Identity object.

        Returns:
            Implicit Permissions object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        prefix, universal = identity_prefixed_universal.split(':', 1)  # type: str, str
        if '+' in prefix:
            ptype, pname = prefix.split('+', 1)
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype(ptype).Pname(pname).Principal(universal)
        else:
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype().Principal(universal)

        result = api.get()
        return result.implicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def list_identities(self, object_dn: str):
        """
        Returns a list of Identity objects that have `explicit` permissions to the object. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.

        Returns:
            List of Identity objects.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        principals = self._auth.websdk.Permissions.Object.Guid(object_guid).get().principals

        principals = [
            self._auth.websdk.Identity.Validate.post(identity={'PrefixedUniversal': principal}).identity
            for principal in principals
        ]

        return principals

    def update(self, object_dn: str, identity_prefixed_universal: str, is_associate_allowed: bool = None, is_create_allowed: bool = None,
               is_delete_allowed: bool = None, is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
               is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
               is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
               is_write_allowed: bool = None):
        """
        Grants the specified permissions to a user or group identity.

        Args:
            object_dn: Absolute path to the object to which permissions will be granted.
            identity_prefixed_universal: The prefixed name of the Identity object.
            is_associate_allowed: Allows associating/dissociating applications to certificates and pushing certificates
                to the associated applications.
            is_create_allowed: Allows creating subordinate objects to the ``object_dn``. Also grants View permission.
            is_delete_allowed: Allows deleting subordinate objects to the ``object_dn``.
            is_manage_permissions_allowed: Allows modification to others' permissions to ``object_dn`` and its
                subordinate objects.
            is_policy_write_allowed: Allows modification to policy values on folder. Requires View permission. Also grants
                Read and Write permissions.
            is_private_key_read_allowed: Allows download of private keys.
            is_private_key_write_allowed: Allows upload of private keys.
            is_read_allowed: Allows ability to read values on subordinate objects to ``object_dn``.
            is_rename_allowed: Allows ability to rename and move subordinate objects to ``object_dn``. Requires Rename
                permission to the destination location.
            is_revoke_allowed: Allows ability to invalidate a certificate. Requires Write permission to the certificate
                object.
            is_view_allowed: Allows ability to view the name of all subordinate objects to ``object_dn``.
            is_write_allowed: Allows editing of subordinate objects to ``object_dn``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        object_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=object_dn).guid
        prefix, universal = identity_prefixed_universal.split(':', 1)  # type: str, str
        if '+' in prefix:
            ptype, pname = prefix.split('+', 1)
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype(ptype).Pname(pname).Principal(universal)
        else:
            api = self._auth.websdk.Permissions.Object.Guid(object_guid).Ptype().Principal(universal)

        current_permissions = self.get_explicit(object_dn=object_dn, identity_prefixed_universal=identity_prefixed_universal)

        if bool([y for x, y in current_permissions.__dict__.items() if not x.startswith('_') and y is not None]):
            method = api.put
        else:
            method = api.post

        result = method(
            is_associate_allowed=is_associate_allowed,
            is_create_allowed=is_create_allowed,
            is_delete_allowed=is_delete_allowed,
            is_manage_permissions_allowed=is_manage_permissions_allowed,
            is_policy_write_allowed=is_policy_write_allowed,
            is_private_key_read_allowed=is_private_key_read_allowed,
            is_private_key_write_allowed=is_private_key_write_allowed,
            is_read_allowed=is_read_allowed,
            is_rename_allowed=is_rename_allowed,
            is_revoke_allowed=is_revoke_allowed,
            is_view_allowed=is_view_allowed,
            is_write_allowed=is_write_allowed
        )
        result.assert_valid_response()
