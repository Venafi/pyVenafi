.. _platforms:

Platforms
=========

Updating Platforms
------------------
Make sure you are authenticated, see: :ref:`authentication`

This example demonstrates how to update the platform attributes for the discovery manager platform on the EXAMPLE_TPP_ENGINE_1 and EXAMPLE_TPP_ENGINE_2 engines.

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.platforms.discovery_manager.update_engines(
        attributes={
            Attributes.platforms.discovery_manager.connection_timeout : ["1"],
            Attributes.platforms.engines.log_debug : ["1"]
        },
        engine_names=[
            'EXAMPLE_TPP_ENGINE_1',
            'EXAMPLE_TPP_ENGINE_2'
        ]
    )

.. note::
    There are many different platform types, discovery_manager is used in this example.

Platform Types
--------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.platforms.auto_layout_manager.update_engines(...)
    features.platforms.bulk_provisioning_manager.update_engines(...)
    features.platforms.ca_import_manager.update_engines(...)
    features.platforms.certificate_manager.update_engines(...)
    features.platforms.certificate_pre_enrollment.update_engines(...)
    features.platforms.certificate_revocation.update_engines(...)
    features.platforms.cloud_instance_monitor.update_engines(...)
    features.platforms.discovery_manager.update_engines(...)
    features.platforms.monitor.update_engines(...)
    features.platforms.onboard_discovery_manager.update_engines(...)
    features.platforms.reporting.update_engines(...)
    features.platforms.ssh_manager.update_engines(...)
    features.platforms.trustnet_manager.update_engines(...)
    features.platforms.validation_manager.update_engines(...)
