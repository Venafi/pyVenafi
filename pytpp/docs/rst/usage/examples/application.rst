.. _application:

Application
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Application Types
-----------------

Refer to :ref:`application_feature_list` for the available application feature types.

Creating an Application
-----------------------

.. code-block:: python

    from pytpp import AttributeValues, Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.application.apache.create(
        name='example_apache_application',
        device='\\VED\\Policy\\Installations\\Devices\\example_device',
        private_key_file='/etc/example/private_key.p12',
        certificate_file='/etc/example/cert.crt',
    )

Get an Application
------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # This will raise an error if it doesn't exist
    application = features.application.apache.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')

    # This will not raise an error if it doesn't exist
    application = features.application.apache.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application', raise_error_if_not_exists=False)

Delete an Application
---------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can delete with the application object
    application = features.application.apache.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')
    features.application.apache.delete(application=application)

    # You can also delete with the DN
    features.application.apache.delete(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Enable an Application
---------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can enable with the application object
    application = features.application.apache.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')
    features.application.apache.enable(application=application)

    # You can also enable with the DN
    features.application.apache.enable(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Disable an Application
----------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can disable with the application object
    application = features.application.apache.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')
    features.application.apache.disable(application=application)

    # You can also disable with the DN
    features.application.apache.disable(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Application Certificate
---------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate = features.application.apache.get_associated_certificate(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Processing Stage of the Application
---------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    stage = features.application.apache.get_stage(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Processing Status of the Application
----------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    status = features.application.apache.get_status(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Wait for Certificate Installation to Complete
---------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # First we need to get the certificate to renew
    certificate = features.application.apache.get_associated_certificate(application='\\VED\\Policy\\Installations\\Applications\\example_application')

    # Next we renew the certificate, you can also simply provide a DN if you have it already
    features.certificate.renew(certificate=certificate)

    # Now we can wait for the application to complete
    features.application.apache.wait_for_installation_to_complete(application='\\VED\\Policy\\Installations\\Applications\\example_application')
