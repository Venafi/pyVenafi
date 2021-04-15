from pytpp.vtypes import Config, Identity
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.properties.response_objects.permissions import Permissions as PermResponseObj


@feature()
class Permissions(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, obj: 'Config.Object', identity: 'Identity.Identity'):
        """
        Deletes all explicit permissions granted to a user or group on the ``obj``. All implicit permissions,
        i.e. those that are inherited from group memberships and parent folders, are unaffected.

        Args:
            obj: Config object of the object to act on.
            identity: Identity object of the user or group.
        """
        current_permissions = self.get_explicit(obj=obj, identity=identity)
        if not current_permissions:
            return

        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.delete()
        result.assert_valid_response()

    def get_effective(self, obj: 'Config.Object', identity: 'Identity.Identity'):
        """
        Returns the `effective` permissions of a user or group on the ``obj``. Effective permissions are the
        permissions that are `effectively` enforced by TPP. All Master Admin, implicit, and explicit permissions
        are taken into account to evaluate the final effective permissions of a user or group.

        Args:
            obj: Config object of the object to act on.
            identity: Identity object of the user or group.

        Returns:
            Effective Permissions object.
        """
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.Effective.get()
        return result.effective_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_explicit(self, obj: 'Config.Object', identity: 'Identity.Identity'):
        """
        Returns the `explicit` permissions of a user or group on the ``obj``. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored. To get implicit permissions, use
        :meth:`get_implicit`.

        Args:
            obj: Config object of the object to act on.
            identity: Identity object of the user or group.

        Returns:
            Explicit Permissions object.
        """
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.get()
        return result.explicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_implicit(self, obj: 'Config.Object', identity: 'Identity.Identity'):
        """
        Returns the `implicit` permissions of a user or group on the ``obj``. Implicit permissions are permissions
        inherited from other folders and group memberships. To get explicit permissions, use :meth:`get_explicit`.

        Args:
            obj: Config object of the object to act on.
            identity: Identity object of the user or group.

        Returns:
            Implicit Permissions object.
        """
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.get()
        return result.implicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def list_identities(self, obj: 'Config.Object'):
        """
        Returns a list of Identity objects that have `explicit` permissions to the object. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored.

        Args:
            obj: Config object of the object to act on.

        Returns:
            List of Identity objects.
        """
        principals = self._api.websdk.Permissions.Object.Guid(obj.guid).get().principals

        principals = [
            self._api.websdk.Identity.Validate.post(identity={'PrefixedUniversal': principal}).identity
            for principal in principals
        ]

        return principals

    def update(self, obj: 'Config.Object', identity: 'Identity.Identity', is_associate_allowed: bool = None, is_create_allowed: bool = None,
               is_delete_allowed: bool = None, is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
               is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
               is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
               is_write_allowed: bool = None):
        """
        Grants the specified permissions to a user or group identity.

        Args:
            obj: Config object of the object to act on.
            identity: Identity object of the user or group.
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
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        current_permissions = self.get_explicit(obj=obj, identity=identity)

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
