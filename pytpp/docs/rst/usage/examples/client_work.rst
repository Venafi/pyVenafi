.. _client_work:

Client Work
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. note::
    The feature for client work is implemented by making use of the WebSDK Config API. It is a wrapper around that API to make interacting with client work easier.

Creating Client Work
--------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')


Client Work Types
-----------------

Refer to :ref:`client_work_feature_list` for the available client work feature types.

.. note::
    When assigning client work to a client group, not all client work types can be assigned to all client group types.
    See :ref:`client_groups` for more information.

Setting The Schedule For Client Work
------------------------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')

    # You can schedule with the client_work object
    features.client_work.ssh_remediation.schedule(work=client_work, start_time=2, daily=True)

    # You can also schedule with the name of the client work
    features.client_work.ssh_remediation.schedule(work='name_of_client_work', hourly=True)

.. note::
    Every client work type has different scheduling options.

Removing The Schedule From A Client Work
----------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')
    features.client_work.ssh_remediation.unschedule(work=client_work)

Enable Client Work
------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')

    features.client_work.ssh_remediation.enable(work=client_work)

Disable Client Work
-------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')

    features.client_work.ssh_remediation.disable(work=client_work)

Deleting Client Work
--------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='name_of_client_work')

    features.client_work.ssh_remediation.delete(work=client_work)

Getting Client Work
-------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # this will raise an error if it doesn't exist
    client_work = features.client_work.ssh_remediation.get(name='name_of_client_work')

    # client_work will be None if it doesn't exist:
    client_work = features.client_work.ssh_remediation.get(name='name_of_client_work', raise_error_if_not_exists=False)

.. note::
    You can create and get the client_work using: ``features.client_work.<client_work type>.create()``. This method will simply return the client_work if it already exists.

List all Client Groups
----------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    all_client_work = features.client_work.ssh_remediation.list()

    for client_work in all_client_work:
        print(client_work.name)
