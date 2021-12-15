.. _authentication:

Authentication
==============

.. note::
    Be sure to check out the :ref:`pytpp-requirements` to configure your API Application Integration in Aperture.
    Only OAuth authentication is supported. Be sure to use the appropriate OAuth scope.

Define The OAuth API Application Integration
--------------------------------------------

Create your Application ID and OAuth scope definition in a separate file.

.. code-block:: python
    :caption: tpp_authentication.py

    from pytpp import Scope


    # Only set the scope needed for this application. This example sets all to True just as an
    # example of the possible options.
    my_oauth_application = dict(
        application_id='pytpp',
        scope=Scope()\
            .agent(delete=True, read=True)\
            .certificate(approve=True, delete=True, discover=True, manage=True, read=True, revoke=True)\
            .configuration(delete=True, manage=True, read=True)\
            .codesign(delete=True, manage=True, read=True)\
            .restricted(delete=True, manage=True, read=True)\
            .security(delete=True, manage=True, read=True)\
            .ssh(approve=True, delete=True, discover=True, manage=True, read=True)\
            .statistics(read=True)
    )

    proxies = {
        'http':
    }

Here are a few different ways to authenticate to TPP:

Username/Password Authentication
--------------------------------
.. code-block:: python

    from tpp_authentication import my_oauth_application
    from pytpp import Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$',
        **my_oauth_application
    )

Certiifcate Authentication
--------------------------

.. code-block:: python

    from tpp_authentication import my_oauth_application
    from pytpp import Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', certificate_path='/local/path/to/cert.crt',
        key_file_path='/local/path/to/cert.key', **my_oauth_application
    )

Reusing An OAuth Token
----------------------

.. code-block:: python

    from tpp_authentication import my_oauth_application
    from pytpp import Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', token='IpGB3icCfMn6YeyIvWu9tB==', **my_oauth_application
    )

Using A Proxy Server
--------------------

|Product| uses the |Python Requests Library| to make REST API requests.
The proxies are submitted to `Authenticate` as a dictionary of protocols to URL endpoints and are used for all API
requests made with this object.

.. code-block:: python

    from tpp_authentication import my_oauth_application
    from pytpp import Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12', password='passw0rd!@#$',
        proxies={'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'},
        **my_oauth_application
    )

