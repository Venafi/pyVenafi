.. _certificate_authority:

Certificate Authority
=====================

The certificate authority feature is still under development and further authority types will be implemented as needed.

Creating a certificate authority
--------------------------------

Make sure you are authenticated, see: :ref:`authentication`

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

     msca = features.certificate_authority.msca.create(
        name='name_of_msca',
        parent_folder_dn='dn_to_parent_folder',
        hostname='dns_or_ip_address',
        service_name='ca_service_name,
        template='ca_template_to_use',
        credential_dn='dn_for_credentials_to_msca'
    )

Supported certificate authority types
-------------------------------------

Currently, the features API supports these types of certificate authorities: msca, self_signed and adaptable.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.certificate_authority.msca.create(...)
    features.certificate_authority.self_signed.create(...)
    features.certificate_authority.adaptable.create(...)

Deleting a certificate authority
--------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    msca = features.certificate_authority.msca.create(
        name='name_of_msca',
        parent_folder_dn='dn_to_parent_folder',
        hostname='dns_or_ip_address',
        service_name='ca_service_name,
        template='ca_template_to_use',
        credential_dn='dn_for_credentials_to_msca'
    )

    features.certificate_authority.msca.delete(certificate_authority=msca)

Getting a certificate authority
-------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # This will raise an exception if it doesn't exist
    msca = features.certificate_authority.msca.get(
        certificate_authority_dn='\\VED\\Policy\\Administration\\Certificate Authorities\\example_msca'
    )

    # This will not raise an exception
    msca = features.certificate_authority.msca.get(
        certificate_authority_dn='\\VED\\Policy\\Administration\\Certificate Authorities\\example_msca',
        raise_error_if_not_exists=False
    )

