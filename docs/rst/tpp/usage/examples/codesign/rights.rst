.. _codesign_rights_usage:

Rights
======

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. note::
    Refer to :ref:`identity_object` to learn about identities.

Adding CodeSign Rights
----------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    user = features.identity.user.get(prefixed_name='local:AwesomeUser')

    #### ADMINISTRATOR ####

    features.codesign.rights.add_administrator(trustee=user)

    #### APPLICATION ADMINISTRATOR ####

    features.codesign.rights.add_application_administrator(trustee=user)

    #### PROJECT APPROVER ####

    features.codesign.rights.add_project_approver(trustee=user)


Getting CodeSign Rights
------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    user = features.identity.user.get(...)

    #### GET OWN RIGHTS TO OBJECT ####

    features.codesign.rights.get_right(obj=r'\VED\Code Signing\Projects\My Project')

    #### GET ALL RIGHTS OF AN IDENTITY ####

    features.codesign.rights.get_trustee_rights(trustee=user)

    #### GET IDENTITIES THAT HAVE RIGHTS TO AN OBJECT ####

    features.codesign.rights.get_object_rights(obj=r'\VED\Code Signing\Projects\My Project')

