from venafi.properties.config import ConfigClass, ApplicationAttributes, ApplicationAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _ApplicationBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str):
        self._secret_store_delete_by_dn(object_dn=object_dn)
        self._config_delete(object_dn=object_dn)


@feature()
class Apache(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Apache Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, private_key_file: str, certificate_file: str, attributes: dict = None):
        """
        Creates an Apache application object.

        Args:
            name: Name of the Apache application object.
            container: Absolute path to the parent folder of the application object.
            private_key_file: Location on the application device to place the private key file.
            certificate_file: Location on the application device to place the certificate file.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.

        """
        attributes = attributes or {}
        apache_attrs = ApplicationAttributes.Apache
        attributes.update({
            ApplicationAttributes.Apache.private_key_file: private_key_file,
            ApplicationAttributes.Apache.certificate_file: certificate_file
        })
        return self._config_create(config_class=ConfigClass.apache, name=name, container=container, attributes=attributes)


@feature()
class PKCS11(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP PKCS11 Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, cryptoki_file_with_path: str, distribution_directory: str, openssl_config_file_with_path:str,
               openssl_directory: str, token_slot_identifier: str, token_slot_pin_dn: str, use_case: str, attributes: dict = None,
               connection_method: str = 'SSH', embed_sans_in_csr: bool = False, import_certificates_into_hsm: str = '0',
               label_format: str = 'Date with CN', port: int = 22, protection_type: str = 'Module', openssl_type:str = 'System',
               reverse_subject_dn: bool = False):
        """
        Creates a PKCS11 application object.

        Args:
            name: Name of the Apache application object.
            container: Absolute path to the parent folder of the application object.
            cryptoki_file_with_path:
            distribution_directory:
            openssl_config_file_with_path:
            openssl_directory:
            token_slot_identifier:
            token_slot_pin_dn:
            use_case:
            attributes: Additional attributes pertaining to the application object.
            connection_method:
            embed_sans_in_csr:
            import_certificates_into_hsm:
            label_format:
            port:
            protection_type:
            openssl_type:
            reverse_subject_dn:

        Returns:

        """
        attributes = attributes or {}
        pkcs11_attrs = ApplicationAttributes.PKCS11
        pkcs11_attr_vals = ApplicationAttributeValues.PKCS11
        attributes.update({
            pkcs11_attrs.hsm_cryptoki_file: cryptoki_file_with_path,
            pkcs11_attrs.hsm_certificate_directory: distribution_directory,
            pkcs11_attrs.hsm_openssl_config_file: openssl_config_file_with_path,
            pkcs11_attrs.hsm_openssl_path: openssl_directory,
            pkcs11_attrs.hsm_token_label: token_slot_identifier,
            pkcs11_attrs.hsm_token_password: token_slot_pin_dn,
            pkcs11_attrs.hsm_requested_usecase: use_case,
            pkcs11_attrs.connection_method: connection_method,
            pkcs11_attrs.hsm_embed_sans_in_csr: embed_sans_in_csr,
            pkcs11_attrs.hsm_import_certificate: import_certificates_into_hsm,
            pkcs11_attrs.hsm_cka_label_format: label_format,
            pkcs11_attrs.port: port,
            pkcs11_attrs.hsm_protection_type: protection_type,
            pkcs11_attrs.hsm_openssl_type: openssl_type,
            pkcs11_attrs.hsm_reverse_subject_dn: reverse_subject_dn
        })
        return self._config_create(config_class=ConfigClass.pkcs11, name=name, container=container, attributes=attributes)
