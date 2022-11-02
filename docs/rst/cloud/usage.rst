Venafi Cloud
============

Authentication
--------------

.. note::
   Be sure to create your own API Key before authenticating. Refer to
   `Obtaining an API Key <https://docs.venafi.cloud/api/obtaining-api-key/>`_ for directions.


.. code-block:: python

   import os
   from pyvenafi.cloud import Authenticate

   session = Authenticate(server='api.venafi.cloud', api_key=os.getenv('VENAFI_CLOUD_API_KEY'))


Making API Calls
----------------

.. note::
   All schema models are defined with `pydantic <https://pydantic-docs.helpmanual.io>`_ , which automatically serializes inputs and outputs
   to and from the API servers.

Making API calls is super easy! Just pay attention to these details.
 * Import the basics: ``from pyvenafi import Authenticate, models``
 * Specify the same path pattern in code as you would see in the url, minus ``v1``. The REST method follows. For example,
   ``GET /v1/users/username/{username}`` becomes ``session.cloud_api.users.username.USERNAME('my_awesome_email@awesomeness.com').get(...)``.
 * The parameters for the method often require a model. Find the model you need under ``models.[service].[model_name]`` where ``[service]``
   is the service name for the API (found in the Swagger documentation) and the ``[model_name]`` is the name of the Component Schema, which
   is usually the same name as the parameter. For example, ``POST /v1/pairingcodes`` (part of the ``edgemanagement_service``) requires an input of
   the ``PairingCodeRequest`` model, which becomes:
   ``session.cloud_api.pairingcodes.post(PairingCodeRequest=models.edgemanagement_service.PairingCodeRequest(...))``
 * The output contains the response from Python's ``requests`` library as well as a model of the Component Schema. While most APIs only return one
   possible schema on an OK response, some may return one of many, dependent on the return code. Be sure you know which schema to expect in return
   and reference that schema in the code.

**Example 1**

.. code-block:: text

    Given: GET /v1/users/username/{username}
    USERNAME: my_awesome_email@awesomeness.com
    RESULT:
        {
          "users": [
            {
              "username": "my_awesome_email@awesomeness.com",
              "id": "271318d0-2e48-11ed-ac1c-4fcd86477abc",
              "companyId": "a15e8751-ae42-11e9-ad55-1b87ad668abc",
              "firstname": "ME",
              "lastname": "AWESOME",
              "emailAddress": "my_awesome_email@awesomeness.com",
              "userType": "EXTERNAL",
              "userAccountType": "WEB_UI",
              "ssoStatus": "INACTIVE",
              "userStatus": "ACTIVE",
              "systemRoles": [
                "SYSTEM_ADMIN"
              ],
              "productRoles": {},
              "localLoginDisabled": false,
              "hasPassword": true,
              "firstLoginDate": "2022-09-07T18:10:07.218+00:00",
              "creationDate": "2022-09-07T18:09:02.173+00:00",
              "ownedTeams": [],
              "memberedTeams": []
            }
          ]
        }

.. code-block:: python

    from pyvenafi.cloud import Authenticate

    session = Authenticate(...)
    response = session.cloud_api.users.username.USERNAME('my_awesome_email@awesomeness.com').get()
    # This will print everything returned by the method above as JSON.
    print(response.json(indent=2))
    # This will print the usernames returned.
    for user in response.UserResponse.users:
      print(user.username)

**Example 2**

.. code-block:: python

   from pyvenafi.cloud import Authenticate, models
   from datetime import datetime
   from uuid import UUID

   ENVIRONMENT_ID = UUID(...)

   session = Authenticate(...)
   response = session.cloud_api.pairingcodes.post(PairingCodeRequest=models.edgemanagement_service.PairingCodeRequest(
       environmentId=ENVIRONMENT_ID,
       reuseCount=1,
       expirationDate=datetime.today() + timedelta(days=1)
   ))
   print(response.PairingCodeInformation.pairingCode)


Logging
-------

.. warning::

    Only enable logging for debugging purposes. It is not recommended to enable logging in Production. Logging can
    potentially log sensitive information, such as private keys or credentials.

This package uses a custom logger class derived from built-in logging to log the inputs and outputs to each API. Use Python's built-in logging
module to enable logging.
