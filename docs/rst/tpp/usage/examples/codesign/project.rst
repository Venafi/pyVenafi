.. _codesign_project_usage:

Projects
========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Managing Projects
-----------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    user = features.identity.user.get(prefixed_name='local:AwesomeUser')

    project = features.codesign.project.create(
        name='My Project',
        description='My Project'
        owners=[user]
    )

    #### UPDATE ####

    # Make changes to project object
    project.description = 'New description'

    features.codesign.project.update(project=project)

    #### DELETE ####

    features.codesign.project.delete(project=project)

Getting & Enumerating Projects
------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET ####

    project = features.codesign.project.get(dn=r'\VED\Code Signing\Projects\My Project')

    #### ENUMERATE ####

    projects = features.codesign.project.enumerate()

