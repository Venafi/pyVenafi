.. _using_features:

Using Features
==============

.. note::
    In order to use the features layer of the Venafi module the user must be able to authenticate
    to the WebSDK APIs and have sufficient privileges to the API Integration if using OAuth
    authentication. See :ref:`features` for a list of feature functions.

Initializing The Features Object
''''''''''''''''''''''''''''''''

``Features`` provides a simpler interface to TPP to accomplish tasks at a higher level of abstraction, such as
creating an Adaptable Workflow object or managing TPP Platforms.

Here is an example of how to initialize the ``Features`` object.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        application_id='PyTPP',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )
    features = Features(api)

Config and Identity Objects
'''''''''''''''''''''''''''

This documentation refers to `Config.Object` to `Identity.Identity` types. All users and groups in TPP
are Identity.Identity objects in the product. All other objects are Config.Object objects. The ``Features``
layer of this package uses object distinguished names (DNs), GUIDs, and other object identifiers to perform
a function against an object.

When creating objects and identities the Config and Identity objects are returned, respectively. An Identity
or Config Object can be acquired with a DN or GUID of that object using `features.objects.get(...)`.

:Config Object:
    + ``absolute_guid``: GUID identifier of the object and its ancestral GUIDs until the root GUID (\\VED).
    + ``dn``: Absolute path to the object.
    + ``guid``: GUID identifier of the object.
    + ``config_id``: Config identifier number of the object.
    + ``name``: Name of the object.
    + ``parent``: Absolute path to the parent object.
    + ``revision``: The revision number of the last object change.
    + ``type_name``: The object class name.

Example:

    .. code-block:: python

        features = Feature(api)
        # Get the Config object by the Policy folder DN.
        policy_folder = features.objects.get(object_dn=r'\VED\Policy')
        new_folder = features.folder.create(
            name='MyNewFolder',
            parent_folder_dn=policy_folder.dn
        )

:Identity Object:
    + ``full_name``: The AD or LDAP data that identifies the user and group. Contains CNs with the Common Name and DC Domain Components.
    + ``is_container``: ``True`` if this object is a container, otherwise ``False``.
    + ``is_group``: ``True`` if this object is a group, otherwise ``False``.
    + ``name``: The friendly name, account, or group name.
    + ``universal``: The Universal Unique ID that identifies a user or group identity.
    + ``prefix``: The identity provider prefix that manages the account or group Name.
    + ``prefixed_name``: ``prefix + name``. *Example: local:admin*
    + ``prefixed_universal``: ``prefix + universal``. *Example: local:{f32b5c37-c2d7-49aa-9ef4-2d38954a8b9b}*
    + ``type``: The category that describes the identity.

        * 0: Undefined
        * 1: User object
        * 2: Group object
        * 4: Container of users and groups.
        * 8: Distribution list.

Example:

    .. code-block:: python

        features = Features(api)
        # Get the Identity object for user AD+SomeAD:first.last.
        my_user = features.identity.user.validate(prefixed_name='AD+SomeAD:first.last')
        features.identity.group.add_members(
            group_prefixed_name='local:ImportantGroup',
            member_prefixed_names=[my_user.prefixed_name]
        )
