.. _authentication:

Authentication
==============

.. note::
   The Trust Protection Platform (TPP) server must have the WebSDK component enabled in order for the PyTPP
   module to authenticate.

.. note::
   The user authenticating to TPP must have sufficient rights to make WebSDK calls. This includes ensuring the user has
   the right to use the WebSDK. If using OAuth authentication, the user must also have rights to use the desired
   Application Integration, which can be configured via the Aperture UI.


The ``Authenticate`` class creates an object that provides access to all WebSDK APIs. A ``scope`` must be provided as well
as the ``application_id`` in order to use OAuth authentication. See Venafi's WebSDK documentation for formatting the scope.

Authentication
""""""""""""""

.. warning::
   The use of *https://<tpp_host>/vedsdk/Authorize* has been deprecated as of TPP 20.1 and is required beyond 21.1. While it is
   still functional, it is advised that you use the OAuth function to authenticate.

.. note::
    The OAuth scope in this example is only an example of what scope can be used and is not the required scope for pytpp to
    function. You can create a customized API Application Integration in Aperture for PyTPP, which is documented
    `here <https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creatingNew-Aperture.php>`_.

.. note:: You can use this Application Integration JSON snippet to create an Application Integration in Aperture.

.. code-block:: json

    {
        "id"         : "pytpp",
        "name"       : "Venafi PyTPP SDK",
        "vendor"     : "Venafi, Inc.",
        "description": "Application Integration for PyTPP, a Python interface to TPP.",
        "scope"      : "certificate:approve,delete,discover,manage,read,revoke;ssh:approve,delete,discover,manage,read;codesign:delete,manage,read;configuration:delete,manage,read;restricted:delete,manage,read;security:delete,manage,read;statistics:read;agent:delete,read"
    }

.. code-block:: python

    from pytpp import Authenticate, Features

    # With OAuth
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        application_id='pytpp',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )
    # Without OAuth
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$'
    )
    # Certificate Authentication
    api = Authenticate(
        host='tppserver.mycompany.com',
        application_id='pytpp',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage",
        certificate_path='/path/to/certificate.pem',
        key_file_path='/path/to/certificate.key'
    )

    features = Features(api)

