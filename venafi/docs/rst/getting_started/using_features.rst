.. _using_features:

Using Features
==============

.. note::
    In order to use the features layer of the Venafi module the user must be able to authenticate
    to the WebSDK APIs and have sufficient privileges to the API Integration if using OAuth
    authentication. See :ref:`features` for a list of feature functions.

Initializing The Features Object
''''''''''''''''''''''''''''''''

The ``Features`` object consumes the ``Authenticate`` object, which holds the user's authenticated
sessions to all API sources. This object grants higher-level access to the underlying APIs that
accomplish a function within Trust Protection Platform (TPP). The advantage of this layer of code
over using direct APIs are these:

* No matter how the APIs changes or how the API sources change, the ``Features`` will not change
  unless an entire feature within the product is deprecated.
* Feature functions are composed of one and sometimes multiple API calls. Each function validates
  the success of each API response within the function and responds appropriately.

Here is an example of how to initialize the ``Features`` object.

.. code-block:: python

    from venafi import Authenticate, Features

    # Authenticate to all API sources.
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        preference='websdk',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )
    # Access the features by providing the authenticated sessions to the Features class.
    features = Features(api)

Config and Identity Objects
'''''''''''''''''''''''''''

All users and groups in TPP are Identity objects in the product. All other objects are Config objects.
The ``Features`` layer of the product uses object distinguished names (DNs), GUIDs, and other object
identifiers to perform a function against an object.

When creating objects and identities the Config and Identity objects are returned, respectively.

Getter methods are available to get a Config or Identity object.

:Config Object:
    + ``absolute_guid``: GUID identifier of the object and its ancestral GUIDs until the root GUID (\\VED).
    + ``dn``: Absolute path to the object.
    + ``guid``: GUID identifier of the object.
    + ``config_id``: Config identifier number of the object. ``None`` when using Aperture API.
    + ``name``: Name of the object.
    + ``parent``: Absolute path to the parent object.
    + ``revision``: The revision number of the last object change. ``None`` when using Aperture API.
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
    + ``universal``: The Universal Unique ID that identifies a user or group identity. ``None`` when using Aperture API.
    + ``prefix``: The identity provider prefix that manages the account or group Name. ``None`` when using Aperture API.
    + ``prefixed_name``: ``prefix + name``. *Example: local:admin*
    + ``prefixed_universal``: ``prefix + universal``. *Example: local:{f32b5c37-c2d7-49aa-9ef4-2d38954a8b9b}*
    + ``type``: The category that describes the identity. ``None`` when using Aperture API.

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
