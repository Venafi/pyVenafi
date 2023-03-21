.. _codesign_application_usage:

Applications
============

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Managing Applications
---------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    application = features.codesign.application.create(
        name='My Application',
        description='My Application',
        signatory_issuer='Microsoft Corporation',
        signatory_subject='Microsoft Corporation',
        size=40,
        version='7.1A',
    )

    #### UPDATE ####

    # Make changes to application object
    application.description = 'New description'

    features.codesign.application.update(application=application)

    #### DELETE ####

    features.codesign.application.delete(application=application)

Getting & Enumerating Applications
----------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET ####

    application = features.codesign.application.get(dn=r'\VED\Code Signing\Signing Applications\My Application')

    #### ENUMERATE ####

    applications = features.codesign.application.enumerate(_filter='\VED\Code Signing\Signing Applications\My App*')

Find Application References
---------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    application = features.codesign.application.get(dn=r'\VED\Code Signing\Signing Applications\My Application')

    #### COUNT REFERENCES ####

    num_references = features.codesign.application.count_references(application=application)

    #### ENUMERATE REFERENCES ####

    references = features.codesign.application.enumerate_references(application=application)
