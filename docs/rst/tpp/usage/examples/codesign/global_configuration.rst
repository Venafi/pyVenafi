.. _codesign_global_configuration_usage:

Global Configuration
====================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Getting the Global Configuration
--------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    global_configuration = features.codesign.global_configuration.get()


Setting the Global Configuration
--------------------------------

.. note::
    You can set the Global Configuration using
    ``features.codesign.global_configuration.set()``,
    or you can set individual values on the existing Global Configuration using
    ``features.codesign.global_configuration.set_values()``

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features, AttributeValues
    from pyvenafi.tpp.api.websdk.models.codesign import GlobalConfiguration

    api = Authenticate(...)
    features = Features(api)

    #### SET ENTIRE GLOBAL CONFIGURATION ####

    features.codesign.global_configuration.set(
        global_configuration=GlobalConfiguration(
            approved_key_storage_locations=[AttributeValues.CodeSign.KeyStorageLocation.software],
            available_key_storage_locations=['Software'],
            default_ca_container=r'\\VED\\Policy\\Code Signing\\Certificate Authority Templates',
            default_certificate_container=r'\\VED\\Policy\\Code Signing\\Certificates',
            default_credential_container=r'\\VED\\Policy\\Code Signing\\Credentials',
            key_use_timeout=60,
            project_description_tooltip="",
            request_in_progress_message=""
        )
    )

    #### SET PARTIAL GLOBAL CONFIGURATION ####

    features.codesign.global_configuration.set_values(
        approved_key_storage_locations=[AttributeValues.CodeSign.KeyStorageLocation.software],
    )

