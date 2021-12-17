Identity
=============
.. note::
    Check out :ref:`authentication` for instructions on how to authenticate and have access to the required features.

Here are some examples of what kinds of operations can be done at the group and user level.

Group Operations
------------------

.. rubric:: Create a Group
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)

    group = features.identity.group.create(
        name='my_group', member_prefixed_names=my_list_of_prefixed_usernames, get_if_already_exists=True
    )
.. rubric:: Delete a Group
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    features.identity.group.delete(group=my_group)
.. rubric:: Add a Member
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)

    features.identity.group.add_members(
        group=my_group, members_prefixed_names=list_of_my_users
    )

.. rubric:: Find a Group
This will allow you to search for a specific group name, but it will return a list of all groups that contain the name searched.

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    groups = features.identity.group.find(
        name='group_name', limit=100, is_distribution_group=False, is_security_group=True
    )
.. rubric:: Get the Members of a Group
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    group_members = features.identity.group.get_members(group=my_group)
.. rubric:: Remove Members from a Group
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    features.identity.group.remove_members(
        group=my_group,
        member_prefixed_names=my_list_of_prefixed_usernames
    )
.. rubric:: Rename a Group
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    features.identity.group.rename(
        group=my_group,
        new_group_name='my_new_group_name'
    )

User Operations
---------------

.. rubric:: Create a User
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
            host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
            scope='my_scope'
        )

    features = Features(api=api)

    my_user = features.identity.user.create(
        name='my_username',
        password='password',
        email_address='myemail@venafi.com',
    )
.. rubric:: Delete a User
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
            host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
            scope='my_scope'
        )

    features = Features(api=api)
    features.identity.user.delete(user=my_user)
.. rubric:: Find a User
.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
            host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
            scope='my_scope'
        )

    features = Features(api=api)
    user = features.identity.user.find(name='my_username', limit = 100)
.. rubric:: Change a Password
This will set the password of the user. If the user did not have a previous password then you are not required to provide an old_password

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(
            host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$', application_id='pytpp',
            scope='my_scope'
        )

    features = Features(api=api)
    user = features.identity.user.set_password(user=my_user, new_password='new_password', old_passsword='old_password')
