.. _codesign_application_collection_usage:

Application Collections
=======================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Managing Application Collections
--------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    collection = features.codesign.application_collection.create(
        name='My Application Collection',
        applications=[r'\VED\Code Signing\Signing Applications\My Application']
    )

    #### UPDATE ####

    # Make changes to application collection object

    features.codesign.application_collection.update(collection=collection)

    #### DELETE ####

    features.codesign.application_collection.delete(collection=collection)

Getting & Enumerating Application Collections
---------------------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET ####

    collection = features.codesign.application_collection.get(dn=r'\VED\Code Signing\Signing Applications\My Application Collection')

    #### ENUMERATE ####

    collections = features.codesign.application_collection.enumerate(_filter='\VED\Code Signing\Signing Applications\My App*')

Find Application Collection References
--------------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    collection = features.codesign.application_collection.get(dn=r'\VED\Code Signing\Signing Applications\My Application Collection')

    #### COUNT REFERENCES ####

    num_references = features.codesign.application_collection.count_references(collection=collection)

    #### ENUMERATE REFERENCES ####

    references = features.codesign.application_collection.enumerate_references(collection=collection)
