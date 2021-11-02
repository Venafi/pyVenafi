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

Here is an example API Application Integration that can be imported into Aperture:

.. code-block:: json

    {
        "id": "PyTPP",
        "name": "Python for TPP",
        "vendor": "Venafi",
        "description": "Python package for Trust Protection Platform (TPP). It provides an interface to the TPP WebSDK API and a feature layer abstraction that provides a higher-level interface to TPP.",
        "scope": "certificate;ssh:discover,approve;security:manage"
    }

.. code-block:: python

    from pytpp import Authenticate, Features

    # With OAuth
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        application_id='PyTPP',
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
        application_id='PyTPP',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage",
        certificate_path='/path/to/certificate.pem',
        key_file_path='/path/to/certificate.key'
    )

    features = Features(api)

