PyTPP Documentation
===================

See the full documentation `here <https://pytpp.readthedocs.io/en/latest>`_.

This is a Python package for Trust Protection Platform (TPP). It provides an interface to the TPP WebSDK API
and a feature layer abstraction that provides a higher-level interface to TPP. The feature layer
abstraction provides intuitive feature methods, such as ``folder.create()`` and ``network.discovery.run()``,
that handles all the dirty work of calling and validating the APIs under the hood.

This package is used by Venafi in testing and is actively under constant development.

Requirements
------------

* Python >= 3.8

Installation
------------

**PIP**: ``pip install pytpp``

**Git**: ``git clone https://coolsolutions.venafi.com/spi/pytpp.git``

Getting Started
---------------

.. note::
    OAuth authentication is highly recommended. Configure OAuth via Aperture. Methods other than supplying a username, password,
    and OAuth credentials are not supported in the feature layer. The WebSDK APIs are still available to authenticate otherwise.

Initializing The API and Feature Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pytpp import Authenticate, Features

    # With OAuth
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )

    # Without OAuth
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$'
    )

    features = Features(api)

Using The WebSDK API
~~~~~~~~~~~~~~~~~~~~

The path of the URL for the WebSDK API is translated to Python by following this format:

.. code-block::

    Given: POST Config/Create
    Then: ``api.websdk.Config.Create.post(...)``

The response body returned by TPP is also translated to Python. For example:

.. code-block::

    Given: POST Config/Create -> {"Object": {"DN": "...", ...}}
    Then: Access the DN -> ``response.object.dn``

.. code-block:: python

    from pytpp import Authenticate, AttributeNames, AttributeValues, Classes

    # With OAuth
    api = Authenticate(
        host='tpp.mycompany.com',
        username='username123',
        password='passw0rd!@#$',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )
    # Create a folder
    response = api.websdk.Config.Create.post(
        object_dn=r'\VED\Policy\Certificates\Team1',
        class_name=Classes.Folder.policy
    )

    #### Not the preferred method for getting content from the response. ####
    # The response is not validated until an object returned in the body of the response is accessed.
    response.assert_valid_response()  # Validate the response is valid.
    folder = response.json_response.json()['Object']  # Raw JSON response.
    print(folder['DN'])

    #### Preferred method for getting content from the response. ####
    # The response is validated automatically here since the object returned in the body of the response
    # is accessed. There is no need to call response.assert_valid_response here.
    folder = response.object # The Config Object returned by the API
    print(folder.dn)  # The DN attribute within the Config Object returned by the API

Using The Features
~~~~~~~~~~~~~~~~~~

Features are abstractions of WebSDK APIs to give a higher-level logical interface to TPP, such as creating discovery jobs and running them.

Using the above example for creating a folder:

.. code-block:: python

    from pytpp import Authenticate, Features


    api = Authenticate(...)
    features = Features(api)

    folder = features.folder.create(
        name='Team1',
        parent_folder_dn=r'\VED\Policy\Certificates'
    )
    # The Config object is returned
    print(folder.dn)  # The DN attribute within the Config Object returned by the API

This layer uses Config and Identity objects because some APIs require a DN and others a GUID. Those items are stored in the Config and Identity
objects. All create and get methods returned the Config and Identity object associated to the query.

.. code-block:: python

    from pytpp import Authenticate, Features


    api = Authenticate(...)
    features = Features(api)

    certificate = features.objects.get(
        object_dn=r'\VED\Policy\Certificates\Team1\important_cert'
    )
    current_thumbprint = features.certificate.renew(certificate=certificate)
    features.certificate.wait_for_enrollment_to_complete(certificate=certificate, current_thumbprint=current_thumbprint)
    features.certificate.download(certificate=certificate, ...)

Logging
~~~~~~~

See `dblogging <https://pypi.org/project/dblogging>`_ for details on the logging module used. Logging can be sent to
the console, stored in a SQLite database, both, or neither. By default the logger is inactive. If persistent logs to
the SQLite database, you can visualize the results in HTML. See the *dblogging* documentation for more details.

**Console Output Only**

.. code-block:: python

    from pytpp import logger

    logger.set_mode(mode='console') # Not necessary because it is set to this mode by default.
    logger.start()

**Persistent Logs**

Logs can persist in a SQLite database.

.. code-block:: python

    from pytpp import logger

    logger.set_mode(mode='persistence') # No console output, just the SQLite DB.
    logger.log_path = '/path/to/logs/folder'
    logger.start()

**Both Console And Persistent Logs**

.. code-block:: python

    from pytpp import logger

    logger.set_mode(mode='all') # Not necessary because setting the log_path implies this.
    logger.log_path = '/path/to/logs/folder'
    logger.start()

**Suppressing Verbose Logging**

Sometimes logging can be too verbose, especially when iterating through many WebSDK calls. This is especially prevalent in cases where there
is a timeout period during which many calls are issued to check for a condition to break a loop.

.. code-block:: python

    from pytpp import logger

    with logger.disabled(why='Cuz I want to.'):
        # Nothing is logged in this context block.
        ...

**Logging Custom Messages**

.. code-block:: python

    from pytpp import logger

    # Start the logger
    # Do stuff...
    logger.log(msg='Important message here!')
    try:
        # Some risky stuff...
        logger.log('I did it!')
    except:
        # Guess it didn't work...
        logger.log_exception()

.. toctree::
    :caption: Table Of Contents
    :maxdepth: 1

    rst/getting_started
    rst/pytpp

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
