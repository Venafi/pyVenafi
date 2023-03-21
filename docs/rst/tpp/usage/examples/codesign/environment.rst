.. _codesign_environment_usage:

Environments
============

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Managing Environments
---------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features
    from pyvenafi.tpp.api.websdk.enums.config import CodeSign
    from pyvenafi.tpp.api.websdk.models.codesign import (
        InfoValue,
        Items,
    )

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    environment = features.codesign.environment.create(
        name='My Environment',
        template=r'\VED\Code Signing\Environment Templates\My Certificate Template',
        project=r'\VED\Code Signing\Projects\My Project',
    )

    #### UPDATE ####

    # Make changes to environment object
    environment.key_use_flow_dn = r'\\VED\\Code Signing\\Flows\\No Restrictions'
    environment.key_algorithm.value = 'RSA1024'

    features.codesign.environment.update(environment=environment)

    #### DELETE ####

    features.codesign.environment.delete(environment=environment)

Getting Environments
--------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    environment = features.codesign.environment.get(dn=r'\VED\Code Signing\Projects\My Project\My Environment')
