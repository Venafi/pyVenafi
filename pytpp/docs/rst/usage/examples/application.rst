.. _application:

Application
===========

Creating an Application
-----------------------

Make sure you are authenticated, see: :ref:`authentication`

.. code-block:: python

    from pytpp import AttributeValues, Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    application = features.application.pkcs11.create(name='example_application',
                                       parent_folder_dn='\\VED\\Policy\\Installations\\Applications',
                                       attributes={
                                           Attributes.application.pkcs11.connection_method        : AttributeValues.Application.ConnectionMethod.ssh,
                                           Attributes.application.pkcs11.port                     : 22,
                                           Attributes.application.pkcs11.hsm_protection_type      : AttributeValues.Application.ProtectionType.softcard,
                                           Attributes.application.pkcs11.hsm_certificate_directory: '/home/example/dist',
                                           Attributes.application.pkcs11.hsm_cryptoki_file        : '/opt/nfast/toolkits/pkcs11/libcknfast.so',
                                           Attributes.application.pkcs11.hsm_client_tool_path     : '/opt/example',
                                           Attributes.application.pkcs11.hsm_token_label          : 'hsm_example_label',
                                           Attributes.application.pkcs11.hsm_token_password       : 'hsm_example_password',
                                       })

Application Types
-----------------

There are different types of applications:

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.application.a10_ax_traffic_manager.create(...)
    features.application.amazon_aws.create(...)
    features.application.apache.create(...)
    features.application.azure_key_vault.create(...)
    features.application.basic.create(...)
    features.application.blue_coat_sslva.create(...)
    features.application.capi.create(...)
    features.application.citrix_net_scaler.create(...)
    features.application.connect_direct.create(...)
    features.application.f5_authentication_bundle.create(...)
    features.application.f5_ltm_advanced.create(...)
    features.application.ibm_datapower.create(...)
    features.application.ibm_gsk.create(...)
    features.application.imperva_mx.create(...)
    features.application.jks.create(...)
    features.application.juniper_sas.create(...)
    features.application.oracle_iplanet.create(...)
    features.application.palo_alto_network_fw.create(...)
    features.application.pem.create(...)
    features.application.pkcs11.create(...)
    features.application.pkcs12.create(...)
    features.application.riverbed_steel_head.create(...)
    features.application.tealeaf_pca.create(...)
    features.application.vamnshield.create(...)

Get an Application
------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # This will raise an error if it doesn't exist
    application = features.application.pkcs11.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')

    # This will not raise an error if it doesn't exist
    application = features.application.pkcs11.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application', raise_error_if_not_exists=False)

Delete an Application
---------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can delete with the application object
    application = features.application.pkcs11.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')

    features.application.pkcs11.delete(application=application)

    # You can also delete with the DN
    features.application.pkcs11.delete(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Enable an Application
---------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can enable with the application object
    application = features.application.pkcs11.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')

    features.application.pkcs11.enable(application=application)

    # You can also enable with the DN
    features.application.pkcs11.enable(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Disable an Application
----------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can disable with the application object
    application = features.application.pkcs11.get(application_dn='\\VED\\Policy\\Installations\\Applications\\example_application')

    features.application.pkcs11.disable(application=application)

    # You can also disable with the DN
    features.application.pkcs11.disable(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Application Certificate
---------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate = features.application.pkcs11.get_associated_certificate(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Processing Stage of the Application
---------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    stage = features.application.pkcs11.get_stage(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Get Processing Status of the Application
----------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    status = features.application.pkcs11.get_status(application='\\VED\\Policy\\Installations\\Applications\\example_application')

Wait for Certificate Installation to Complete
---------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # First we need to get the certificate to renew
    certificate = features.application.pkcs11.get_associated_certificate(application='\\VED\\Policy\\Installations\\Applications\\example_application')

    # Next we renew the certificate, you can also simply provide a DN if you have it already
    features.certificate.renew(certificate=certificate)

    # Now we can wait for the application to complete
    features.application.pkcs11.wait_for_installation_to_complete(application='\\VED\\Policy\\Installations\\Applications\\example_application')
