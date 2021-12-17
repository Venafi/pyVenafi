Credential
===========

Username password credential
----------------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12'
        password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)

    credential = features.credential.username_password(
        name='my_credential',
        parent_folder= 'path/to/parent/folder',
        username='my_user',
        password='password'
    )
* The attributes of the username_password object are:
    * name: Name of the credential object.
    * parent_folder: ``Config.Object`` or DN of the parent folder.
    * username: Username.
    * password: Password.
    * expiration: Number months from today at which the credential expires.
    * description: Description of the credential object.
    * encryption_key: Encryption Key used to protect the credential data.
    * shared: If True, the credential can be shared between multiple objects.
    * contacts: List of absolute paths to the users in TPP to be established as contacts.
    * get_if_already_exists: bool = True

Google password credential
---------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12'
        password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)

    json content = {
        "type"                       : "service_account",
        "project_id"                 : "********",
        "private_key_id"             : "********",
        "private_key"                : "-----BEGIN PRIVATE KEY-----\n********-----END PRIVATE KEY-----\n",
        "client_email"               : "service@********.iam.gserviceaccount.com",
        "client_id"                  : "********",
        "auth_uri"                   : "https://accounts.google.com/o/oauth2/auth",
        "token_uri"                  : "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url"       : "https://www.googleapis.com/robot/v1/metadata/x509/********.iam.gserviceaccount.com"
    }
    features.credential.google.create(
        name='my_credential',
        parent_folder= 'path/to/parent/folder',
        json_content=json_content,
        username='my_user',
        password='password'
    )

* Google credential attributes:
    * name: Name of the credential object.
    * parent_folder: ``Config.Object`` or DN of the parent folder.
    * json_content: JSON content as plain text.
    * expiration: Number months from today at which the credential expires.
    * description: Description of the credential object.
    * encryption_key: Encryption Key used to protect the credential data.
    * shared: If True, the credential can be shared between multiple objects.
    * contacts: List of absolute paths to the users in TPP to be established as contacts.
    * get_if_already_exists: bool = True
