Folders
=======

Creating And Deleting Folders
-----------------------------

.. warning::
    Deleting a folder will also remove all objects from its associated secrets, such as private key information
    stored in the database. While the opbject is removed from the secret, the secret is not removed from the
    vault until the secret has no other associations to it, in which case the secret will be removed. If you
    wish to preserve the object's association to it secrets use the WebSDK API ``POST Config/Delete`` instead.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the folder.
    some_folder = features.folder.create(
        name='SomeFolder',
        parent_folder=r'\VED\Policy\Certificates\MyTeam',
        description='Some folder for my team.',
        contacts=['local:user123', 'local:user456'],
        engines=['WestRegionTpp-1', 'MidWestRegionTpp-1'],
        log_server='WestRegionTpp-1 Log Server',
    )

    print(some_folder.dn)  # prints "\VED\Policy\Certificates\MyTeam\SomeFolder"

    # Delete the folder.
    features.folder.delete(folder=some_folder, recursive=True)

Getting, Adding And Removing Engines
------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Add these two engines as the processing engines for this folder. All other
    # engines will be removed.
    features.folder.set_engines(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        engines=['WestRegionTpp-1', 'MidWestRegionTpp-1'],
        append_engines=False  # Set to "True" to preserve existing engines.
    )

    # Get the engines
    engines = features.folder.get_engines(folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder')
    print([e.engine_name for e in engines])  # prints "['WestRegionTpp-1', 'MidWestRegionTpp-1']"

    # Remove all engines from the folder. Now all engines will be able to process work from
    # this folder.
    features.folder.delete_engines(folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder')

.. _applying_workflows:

Applying And Removing Workflows
-------------------------------

.. rubric:: Managing Applied Workflows
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Add a workflow.
    features.folder.apply_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        workflow=r'\VED\Policy\Administration\Workflows\Stage 100 Check'
    )

    # Remove a workflow.
    features.folder.remove_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        workflow=r'\VED\Policy\Administration\Workflows\Stage 100 Check'
    )

.. rubric:: Managing Blocked Workflows
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Add a workflow.
    features.folder.block_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        workflow=r'\VED\Policy\Administration\Workflows\Stage 100 Check'
    )

    # Remove a workflow.
    features.folder.remove_blocked_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        workflow=r'\VED\Policy\Administration\Workflows\Stage 100 Check'
    )

Searching Objects
-----------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    items = features.folder.search(
        object_name_pattern='*my-site?.com',
        object_types=[Attributes.certificate.__config_class__, Attributes.device.__config_class__],
        starting_dn=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        recursive=True
    )

    # prints the DN of all "X509 Certificate" and "Device" items found recursively under
    # the "starting_dn".
    print([i.dn for i in items])

Managing Policies
-----------------

.. _read_policy_attributes:

.. rubric:: Reading Policy Attributes

.. note::
    Reading policy values on a folder only returns the policy values *set* on that folder and not the
    effective value (that may be inherited by a parent policy). To read the *effective* policy value
    use :ref:`read_attributes`.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    items = features.folder.read_policy(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        class_name=Attributes.certificate.__config_class__,
        attribute_name=Attributes.certificate.certificate_authority
    )

.. _write_policy_attributes:

.. rubric:: Writing Policy Attributes

.. note::
    When writing policy values (as opposed to updating them) the current value(s) will be
    overwritten. To simply update the value(s) refer to :ref:`update_policy_attributes`.


.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Use these approveres and remove the existing ones, if any.
    features.folder.write_policy(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['local:approver-1', 'local:approver-1']
        },
        locked=True
    )

.. _update_policy_attributes:

.. rubric:: Updating Policy Attributes

.. note::
    When updating policy values (as opposed to writing them) the current value(s) will *not*
    be overwritten, but will be appended by the requested value(s). To overwrite the existing
    value(s) refer to :ref:`write_policy_attributes`.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Append these approveres to the existing ones, if any.
    features.folder.update_policy(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['local:approver-1', 'local:approver-1']
        },
        locked=True
    )

.. rubric:: Clearing Policy Attributes

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Clear only one approver on the policy, but preserve the rest that may exist.
    features.folder.clear_policy(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['local:approver-1']
        }
    )

    # Clear all approvers on the policy.
    features.folder.clear_policy(
        folder=r'\VED\Policy\Certificates\MyTeam\SomeFolder',
        class_name=Attributes.certificate.__config_class__,
        attributes=[
            Attributes.certificate.approver
        ]
    )
