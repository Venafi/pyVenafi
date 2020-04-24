.. _authentication:

Authentication
==============

.. note::
   The Trust Protection Platform (TPP) server must have the WebSDK component enabled in order for the Venafi
   module to authenticate.

.. note::
   The user authenticating to TPP must have sufficient rights to make WebSDK calls. This includes ensuring the user has
   the right to use the WebSDK. If using OAuth authentication, the user must also have rights to use the specified
   Application Integration, which can be verified and updated throught the Aperture UI.


The ``Authenticate`` class creates an object that provides access to all WebSDK APIs and some Aperture APIs. When creating
the object the user is authenticated to **both** API sources.

A ``preference`` can be specified as either *websdk* (default) or *aperture*. The preference is used by the ``Features`` object
to specify which API will be tried first to execute the feature method.

A ``scope`` must be provided as well as the ``application_id`` in order to use OAuth authentication. The authentication must be
created through the Aperture UI prior to using OAuth authentication through the WebSDK API.

Authentication Without OAuth
""""""""""""""""""""""""""""
.. warning::
   The use of *https://<tpp_host>/vedsdk/Authorize* has been deprecated as of TPP 20.1.x. While it is still functional, it is advised
   that you use the OAuth function to authenticate.

.. code-block:: python

    from venafi import Authenticate

    # This approach is deprecated but still valid.
    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        preference='websdk'
    )

Authentication With OAuth
"""""""""""""""""""""""""

.. code-block:: python

    from venafi import Authenticate


    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        preference='websdk',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )

Authenticating To A Single API Source
"""""""""""""""""""""""""""""""""""""

.. code-block:: python

    from venafi.api.websdk.websdk import WebSDK
    from venafi.api.aperture.aperture import Aperture


    # WebSDK With OAuth
    websdk_oauth = WebSDK(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )
    # WebSDK Without OAuth
    websdk_no_oauth = WebSDK(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$'
    )

    # Aperture
    aperture = Aperture(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$'
    )

