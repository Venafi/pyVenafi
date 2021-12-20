Certificate Operations
========================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Create, Renew, Download, Revoke, Delete a Certificate
-----------------------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    # Create a certificate object.
    certificate = features.certificate.create(
        name='my-team.domain.com',
        parent_folder=r'\VED\Policy\Certificates\MyTeam',
        common_name='my-team.domain.com',
        management_type=AttributeValues.Certificate.ManagementType.enrollment,
        ca_template=r'\VED\Policy\Administration\CAs\AwesomeCA',
        hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
        city='Salt Lake City',
        state='Utah',
        country='US',
        organization='My Company',
        organization_unit=['MyTeam', 'MyRegion'],
        disable_automatic_renewal=False,
        key_algorithm=AttributeValues.Certificate.KeyAlgorithm.rsa,
        key_strength=2048
    )

Renewing A Certificate
----------------------

.. code-block:: python

    from pytpp import Features, Authenticate, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    #Renew the certificate
    current_thumbprint = features.certificate.renew(certificate=certificate)
    features.certificate.wait_for_enrollment_to_complete(certificate=certificate, current_thumbprint=current_thumbprint)

Downloading A Certificate
-------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    # Download the Certificate
    downloaded_cert = features.certificate.download(certificate=certificate)

Revoking A Certificate
----------------------

.. code-block:: python

    from pytpp import Features, Authenticate, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    # Revoke a Certificate
    features.certificate.revoke(certificate=certificate, thumbprint=current_thumbprint)

Deleting A Certificate
----------------------

.. code-block:: python

    from pytpp import Features, Authenticate, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    # Delete the certificate
    features.certificate.delete(certificate=certificate)

Resetting And Retrying Certificate Requests
-------------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues
        api = Authenticate(
            host='tppserver.mycompany.com', username='username12'
            password='passw0rd!@#$', application_id='pytpp',
            scope='my_scope'
        )

    features = Features(api=api)
     #Create certificate with a dictionary
    certificate_attrs = {
        common_name='certificate_common_name.com',
        management_type=AttributeValues.Certificate.ManagementType.enrollment,
        ca_template='path',
        hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
        city='Salt Lake City',
        state='Utah',
        country='US',
        organization='Venafi',
        organization_unit=['SPI'],
        disable_automatic_renewal=False,
        key_algorithm='rsa',
        key_strength='2048'
    }
    cert = features.certificate.create(
         name='certificate.com',
         parent_folder=parent_folder,
         attributes=certificate_attrs
    )
    try:
        current_thumbprint = features.certificate.renew(certificate=cert)
        features.certificate.wait_for_enrollment_to_complete(certificate=cert, current_thumbprint=current_thumbprint)
    except:
        features.certificate.retry_from_current_stage(certificate=cert)

Validation
----------

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12'
        password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)

    cert = features.certificate.create(
        name='certificate.com',
        parent_folder=parent_folder,
        common_name='certificate_common_name.com',
        management_type=AttributeValues.Certificate.ManagementType.enrollment,
        ca_template='path',
        hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
        city='Salt Lake City',
        state='Utah',
        country='US',
        organization='Venafi',
        organization_unit=['SPI'],
        disable_automatic_renewal=False,
        key_algorithm='rsa',
        key_strength='2048'
    )
    validated_certificates, warnings = features.certificate.validate(certificate=cert)
    cert_details = features.certificate.details(certificate=cert)
    validation_results = features.certificate.get_validation_results(certificate=cert)

Getting Certifiate Data
-----------------------

ADD ME.

Associate/Dissociate A Certificate
----------------------------------

.. note:: Check out :ref:`application` and :ref:`device` for instructions on how to create and use applications and devices.

This example uses a unix based device and PKCS11 application as an example to show you how to associate, disassociate an application, and how to provision a certificate.

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues, Attributes
    from settings.legacy_config.others import Pkcs11UnixDevice, Pkcs11WindowsDevice, Pkcs11Tokens

    class PKCS11:
        DEFAULT_SETTINGS = {
            Attributes.application.pkcs11.hsm_requested_usecase:
                AttributeValues.Application.PKCS11.UseCase.tls_client_rsa,
            Attributes.application.pkcs11.hsm_cka_label_format:
                AttributeValues.Application.PKCS11.LabelFormat.date_with_cn,
            Attributes.application.pkcs11.hsm_import_certificate:
                AttributeValues.Application.PKCS11.ImportCertificatesIntoHsm.import_certificate_and_chain,
            Attributes.application.pkcs11.hsm_reverse_subject_dn: "No",
            Attributes.application.pkcs11.hsm_embed_sans_in_csr: "No"
        }
        def __init__(self, device: 'Union[Pkcs11UnixDevice, Pkcs11WindowsDevice]', device_config: 'Types.Config.Object',
                     application_attributes: dict):
            self.device = device
            self.device_config = device_config
            self.application_attributes = self.DEFAULT_SETTINGS.copy()
            self.application_attributes.update(application_attributes)

    api = Authenticate(
        host='tppserver.mycompany.com', username='username12'
        password='passw0rd!@#$', application_id='pytpp',
        scope='my_scope'
    )

    features = Features(api=api)
    unix_config = dict(
        connection_method=AttributeValues.Application.ConnectionMethod.ssh,
        port=22,
        protection_type=AttributeValues.Application.ProtectionType.softcard,
        distribution_directory='/home/spi/dist',
        cryptoki_file_with_path='/opt/nfast/toolkits/pkcs11/libcknfast.so',
        hsm_client_tool_path='/opt/venafi',
        openssl_type=AttributeValues.Application.PKCS11.OpenSslType.custom_openssl_directory,
        openssl_directory='/opt/venafi',
        openssl_config_file_with_path='/opt/venafi/openssl.cnf'
    )

    centos_device = features.device.create(
            name=f'my_centos_device',
            parent_folder='path/to/parent/folder',
            attributes={
                Attributes.device.host                       : ip_address,
                Attributes.device.credential                 : 'path/to/credential',
                Attributes.device.concurrent_connection_limit: "99",
                Attributes.device.remote_server_type         : 'os_type'
            }
        )
    centos = PKCS11(
        device=CentOS_1,
        device_config=centos_1_device,
        application_attributes=unix_config
    )
    application = features.application.pkcs11.create(
            name=f'{name}_{centos.device.name}',
            device=centos.device_config.dn,
            connection_method=centos.application_attributes['connection_method'],
            port=centos.application_attributes['port'],
            distribution_directory=centos.application_attributes['distribution_directory'],
            cryptoki_file=centos.application_attributes['cryptoki_file_with_path'],
            client_tools_directory=centos.application_attributes['hsm_client_tool_path'],
            openssl_config_file=centos.application_attributes['openssl_config_file_with_path'],
            openssl_directory=centos.application_attributes['openssl_directory'],
            import_certificate_into_hsm=centos.application_attributes[
                Attributes.application.pkcs11.hsm_import_certificate],
            label_format=centos.application_attributes[Attributes.application.pkcs11.hsm_cka_label_format],
            protection_type=centos.application_attributes['protection_type'],
            token_pin=Pkcs11Tokens.all_spec_chars_token.password,
            token_identifier=Pkcs11Tokens.all_spec_chars_token,
            use_case=centos.application_attributes[Attributes.application.pkcs11.hsm_requested_usecase]
        )
        certificate = features.certificate.create(
            name='certificate.com',
            parent_folder=parent_folder,
            common_name='certificate_common_name.com',
            management_type=AttributeValues.Certificate.ManagementType.enrollment,
            ca_template='path',
            hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
            city='Salt Lake City',
            state='Utah',
            country='US',
            organization='Venafi',
            organization_unit=['SPI'],
            disable_automatic_renewal=False,
            key_algorithm='rsa',
            key_strength='2048'
        )
        features.certificate.associate_application(
            certificate=certificate,
            applications=[application.dn]
        )

        current_thumbprint = features.certificate.renew(certificate=cert)
        features.certificate.wait_for_enrollment_to_complete(certificate=cert, current_thumbprint=current_thumbprint)
        features.application.pkcs11.wait_for_installation_to_complete(
            application=application,
            timeout=180
        )

        features.certificate.dissociate_application(certificate=certificate, applications=[application.dn])
