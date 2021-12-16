.. _client_groups:

Client Groups
=============

.. note::
    The feature for client groups is implemented by making use of the config objects api.  It is a wrapper around that API to make interacting with client groups easier.

Creating a Client Group
-----------------------
Make sure you are authenticated, see: :ref:`authentication`

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_group = features.client_groups.create(name='name_of_client_group')

.. note::
    1. The default 'agent_type' for a client group is agentless.
    2. The features.client_groups.create() will return the group if it already exists

Agent Types
-----------
There are different types of client groups, they can be found in ClientGroupsAttributeValues:

.. code-block:: python

    from pytpp.properties.config import ClientGroupsAttributeValues

    agent_types = [
        ClientGroupsAttributeValues.AgentType.agentless,
        ClientGroupsAttributeValues.AgentType.certificate_enrollment,
        ClientGroupsAttributeValues.AgentType.deploy_user_and_device_certificates
    ]

Creating client groups with different agent_types:

.. code-block:: python

    from pytpp import Authenticate, Features
    from pytpp.properties.config import ClientGroupsAttributeValues

    api = Authenticate(...)
    features = Features(api)

    agent_installed_client_group = features.client_groups.create(name='agent_installed',  agent_type=ClientGroupsAttributeValues.AgentType.agent_installed))

Assigning Client Work to a Client Group
---------------------------------------
How to assign client work (:ref:`client_work`) to a client group

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can assign client work with the name of the client group
    features.client_groups.assign_work(group='name_of_client_group_1', work_name='name_of_client_work_1')

    # You can assign client work with the object of the client group
    client_group_2 = features.client_groups.create(name='name_of_client_group_2')
    features.client_groups.assign_work(group=client_group_2, work_name='name_of_client_work_2')

.. note::
    Only certain client work types can be assigned to specific client group agent_types.

.. code-block:: python

    from pytpp.properties.config import ClientGroupsAttributeValues
    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    agent_types = {
        ClientGroupsAttributeValues.AgentType.agentless : [
            features.client_work.ssh_discovery,
            features.client_work.ssh_remediation
        ],
        ClientGroupsAttributeValues.AgentType.certificate_enrollment : [
            features.client_work.certificate_enrollment_via_est_protocol
        ],
        ClientGroupsAttributeValues.AgentType.deploy_user_and_device_certificates : [
            features.client_work.agent_connectivity,
            features.client_work.agent_upgrade,
            features.client_work.certificate_device_placement,
            features.client_work.certificate_discovery,
            features.client_work.certificate_installation,
            features.client_work.dynamic_provisioning,
            features.client_work.ssh_device_placement,
            features.client_work.ssh_discovery,
            features.client_work.ssh_key_usage,
            features.client_work.ssh_remediation,
            features.client_work.user_certificate_creation
        ]
    }

Removing Client Work from a Client Group
----------------------------------------
How to remove client work (:ref:`client_work`) from a client group

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can remove work from a client group by name
    features.client_groups.remove_work(group='name_of_client_group_1', work_name='name_of_client_work_1')

    # You can also remove work with the client group object
    client_group_2 = features.client_groups.create(name='name_of_client_group_2')
    features.client_groups.remove_work(group=client_group_2, work_name='name_of_client_work_2')

Deleting a Client Group
-----------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can delete with the name of the group
    features.client_groups.delete(group='name_of_client_group_1')

    # You can also delete with the object of the group
    client_group_2 = features.client_groups.create(name='name_of_client_group_2')
    features.client_groups.delete(group=client_group_2)

Get a Client Groups
-------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # this will raise an error if it doesn't exist
    client_group = features.client_groups.get(name='name_of_client_group')

    # client_group will be None if it doesn't exist:
    client_group = features.client_groups.get(name='name_of_client_group', raise_error_if_not_exists=False)

.. note::
    You can create and get the client_group using: features.client_groups.create().  This method will simply return the client_group if it already exists.

List all Client Groups
----------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    all_client_groups = features.client_groups.list()

    for client_group in all_client_groups:
        print(client_group.name)
