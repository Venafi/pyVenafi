.. _permissions:

Permissions
===========

Updating Permissions
--------------------
Make sure you are authenticated, see: :ref:`authentication`

This example demonstrates updating permissions to an 'example_folder' for a user named 'example_user"

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    example_folder = features.folder.get('\\VED\\Policy\\example_folder')
    user = features.identity.user.get('local:example_user')

    features.permissions.update(obj=example_folder,
                                identity=user,
                                is_associate_allowed=True,
                                is_create_allowed=True,
                                is_delete_allowed=True,
                                is_manage_permissions_allowed=True,
                                is_policy_write_allowed=True,
                                is_private_key_read_allowed=True,
                                is_private_key_write_allowed=True,
                                is_read_allowed=True,
                                is_rename_allowed=True,
                                is_revoke_allowed=True,
                                is_view_allowed=True,
                                is_write_allowed=True
                                )

.. note::
    Permissions can also be assigned using groups instead of users, please see: :ref:`identity`

Deleting Permissions
--------------------

How to remove permissions from an object

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    example_folder = features.folder.get('\\VED\\Policy\\example_folder')
    user = features.identity.user.get('local:example_user')

    features.permissions.delete(obj=example_folder, identity=user)

Get Explicit Permissions
------------------------

Explicit permissions are the permissions that are `explicitly` granted to a user or group on a particular object.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    permissions = feature.permissions.get_explicit(obj='\\VED\\Policy\\example_folder', identity='local:example_user')

    print(permissions.__dict__)

Get Implicit Permissions
------------------------

Implicit permissions are permissions inherited from other folders and group memberships.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    permissions = feature.permissions.get_implicit(obj='\\VED\\Policy\\example_folder', identity='local:example_user')

    print(permissions.__dict__)

Get Effective Permissions
-------------------------

Effective permissions are the permissions that are `effectively` enforced by TPP. All Master Admin, implicit, and explicit permissions are taken into account to evaluate the final effective permissions of a user or group.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    permissions = feature.permissions.get_effective(obj='\\VED\\Policy\\example_folder', identity='local:example_user')

    print(permissions.__dict__)

List Identities
---------------

Get a list of all identities that have permissions to an object

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    identities = feature.permissions.list_identities(obj='\\VED\\Policy\\example_folder')

    for identity in identities:
        print(identity.name)
