.. _certificate_authority:

Certificate Authority
=====================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Supported Certificate Authority Types
-------------------------------------

The certificate authority feature is still under development and further Certificate Authority types will be implemented
as needed. See :ref:`certificate_authorities_feature_list` for a list of supported Certificate Authority types.

Creating And Deleting A Certificate Authority
---------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the CA.
     msca = features.certificate_authority.msca.create(
        name='Awesome MSCA',
        parent_folder=r'\VED\Policy\Administration\CAs',
        hostname='awesomeca.my-company.com',
        service_name='AwesomeCA',
        template='AwesomeTemplate',
        credential=r'\VED\Policy\Administration\Credentials\Awesome MSCA'
    )

    # Delete the CA.
    features.certificate_authority.msca.delete(certificate_authority=msca)

Getting A Certificate Authority
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
