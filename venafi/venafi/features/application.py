from venafi.properties.config import ApplicationClassNames, ApplicationAttributes, ApplicationAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _ApplicationBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, application_dn: str):
        """
        Deletes an Application object.

        Args:
            application_dn: Absolute path to the Application object.
        """
        self._secret_store_delete(object_dn=application_dn)
        self._config_delete(object_dn=application_dn)

    def disable(self, application_dn: str):
        """
        Disables all processing and provisioning of the application.

        Args:
            application_dn:  Absolute path to the Application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.ClearAttribute.post(
            object_dn=application_dn,
            attribute_name=ApplicationAttributes.disabled
        )

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def enable(self, application_dn: str):
        """
        Enables all processing and provisioning of the application.

        Args:
            application_dn:  Absolute path to the Application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.Write.post(
            object_dn=application_dn,
            attribute_data=self._name_value_list({
                ApplicationAttributes.disabled: "1"
            })
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def get_associated_certificate(self, application_dn: str):
        """
        Returns the Certificate object details associated to the Application object.

        Args:
            application_dn:  Absolute path to the Application object.

        Returns:
            Config Object of the certificate object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.ReadDn.post(
            object_dn=application_dn,
            attribute_name=ApplicationAttributes.certificate
        ).values

        if not result:
            return None

        certificate_dn = result[0]
        return self._auth.websdk.Config.IsValid.post(object_dn=certificate_dn).object

    def get_stage(self, application_dn: str):
        """
        Returns the current processing stage of the application object.

        Args:
            application_dn: Absolute path to the Application object.

        Returns:
            The current stage if it exists. Otherwise, returns ``None``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.ReadDn.post(
            object_dn=application_dn,
            attribute_name=ApplicationAttributes.stage
        ).values

        return int(result[0]) if result else None

    def get_status(self, application_dn: str):
        """
        Returns the current processing status of the application object.

        Args:
            application_dn: Absolute path to the Application object.

        Returns:
            The current status if it exists. Otherwise, returns ``None``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.ReadDn.post(
            object_dn=application_dn,
            attribute_name=ApplicationAttributes.status
        ).values

        return result[0] if result else None


@feature()
class A10AXTrafficManager(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP A10 AX Traffic Manager Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an A10 AX Traffic Manager application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.a10_ax_traffic_manager,
            attributes=attributes
        )


@feature()
class Adaptable(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Adaptable Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Adaptable application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.adaptable_app,
            attributes=attributes
        )


@feature()
class AmazonAWS(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Amazon AWS Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an Amazon AWS application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.amazon_app,
            attributes=attributes
        )


@feature()
class Apache(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Apache Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an Apache application object.

        Args:
            name: Name of the Apache application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.

        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.apache,
            attributes=attributes
        )


@feature()
class AzureKeyVault(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Azure Key Vault Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an Azure Key Vault application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.azure_key_vault,
            attributes=attributes
        )


@feature()
class Basic(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Basic Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Basic application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.basic,
            attributes=attributes
        )

    def convert(self, basic_application_dn: str, new_class_name: str, attributes: dict = None):
        """
        Converts the Basic Application to another application class type. If attributes are given,
        then those attributes will apply to the new application once conversion is complete.

        Args:
            basic_application_dn: Absolute path to the Basic Application.
            new_class_name: Application Class Name of the new application object.
            attributes: Attributes pertaining to the new application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.MutateObject.post(
            object_dn=basic_application_dn,
            class_name=new_class_name
        )
        result.assert_valid_response()

        if attributes:
            attributes = {k:([str(v)] if not isinstance(v, list) else v) for k, v in attributes.items()}
            result = self._auth.websdk.Config.Write.post(
                object_dn=basic_application_dn,
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            result.assert_valid_response()

        new_object = self._auth.websdk.Config.IsValid.post(object_dn=basic_application_dn).object
        if new_object.type_name != new_class_name:
            raise FeatureError.UnexpectedValue(
                f'Unable to convert Basic App "{basic_application_dn}" to {new_class_name}. '
                f'Its current class name is {new_object.type_name}.'
            )
        return new_object


@feature()
class BlueCoatSSLVA(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP BlueCoat SSLVA Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a BlueCoat SSLVA application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.blue_coat_sslva,
            attributes=attributes
        )


@feature()
class CAPI(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP CAPI Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a CAPI application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.capi,
            attributes=attributes
        )


@feature()
class CitrixNetScaler(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP CAPI Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a CAPI application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.net_scaler,
            attributes=attributes
        )


@feature()
class ConnectDirect(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Connect:Direct Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Connect:Direct application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.connect_direct,
            attributes=attributes
        )


@feature()
class F5AuthenticationBundle(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP F5 Authentication Bundle Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, bundle_file_name: str, attributes: dict = None):
        """
        Creates a F5 Authentication Bundle application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            bundle_file_name: Name of the bundle file.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.F5AuthenticationBundle.advanced_settings_bundle_name: bundle_file_name
        })
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.f5_authentication_bundle,
            attributes=attributes
        )


@feature()
class F5LTMAdvanced(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP F5 LTM Advanced Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a F5 LTM Advanced application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.f5_ltm_advanced,
            attributes=attributes
        )


@feature()
class IBMDataPower(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP IBM DataPower Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an IBM DataPower application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.data_power,
            attributes=attributes
        )


@feature()
class IBMGSK(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP IBM GSK Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an IBM GSK application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.gsk,
            attributes=attributes
        )


@feature()
class ImpervaMX(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Imperva MX Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates an Imperva MX application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.imperva_mx,
            attributes=attributes
        )


@feature()
class JKS(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP JKS Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a JKS application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.jks,
            attributes=attributes
        )


@feature()
class JuniperSAS(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Juniper SAS Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Juniper SAS application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.juniper_sas,
            attributes=attributes
        )


@feature()
class OracleIPlanet(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Oracle iPlanet Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Oracle iPlanet application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.iplanet,
            attributes=attributes
        )


@feature()
class PaloAltoNetworkFW(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Palo Alto Network FW Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Palo Alto Network FW application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.palo_alto_network_fw,
            attributes=attributes
        )


@feature()
class PEM(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP PEM Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a PEM application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.pem,
            attributes=attributes
        )


@feature()
class PKCS11(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP PKCS11 Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, cryptoki_file_with_path: str, distribution_directory: str,
               openssl_config_file_with_path:str, token_slot_identifier: str, token_slot_pin_dn: str, use_case: str,
               attributes: dict = None, connection_method: str = ApplicationAttributeValues.ConnectionMethod.ssh,
               embed_sans_in_csr: str = "No", import_certificates_into_hsm: str = '0',
               label_format: str = ApplicationAttributeValues.PKCS11.LabelFormat.date_with_cn, port: int = 22,
               protection_type: str = ApplicationAttributeValues.ProtectionType.module, openssl_directory: str = None,
               openssl_type: str = ApplicationAttributeValues.PKCS11.OpenSslType.system,
               reverse_subject_dn: str = "No"):
        """
        Creates a PKCS11 application object.

        Args:
            name: Name of the Apache application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            cryptoki_file_with_path: Absolute path to the Cryptoki file on the client machine.
            distribution_directory: Absolute path to the folder on the client machine where the
                certificate and chain are installed.
            openssl_config_file_with_path: Absolute path to the OpenSSL configuration file on the
                client machine.
            token_slot_identifier: HSM token slot identifier.
            token_slot_pin_dn: Absolute path to the password credential object storing the slot PIN.
            use_case: Purpose for which the certificate is to be used.
            attributes: Additional attributes pertaining to the application object.
            connection_method: Connection protocol for TPP to communicate with the client.
            embed_sans_in_csr: If "Yes", the SANs are included in the CSR.
            import_certificates_into_hsm: If ``True``, the certificates are imported into the HSM.
            label_format: The format of the label. May be custom.
            port: Connection port.
            protection_type: Protection type of the HSM.
            openssl_directory: Directory holding the OpenSSL executable. Only set when ``openssl_type`` is set to
                be custom.
            openssl_type: If set to 'System', then the ``openssl_directory`` is set to the default system location.
            reverse_subject_dn: If "Yes", the subject's domain components are reversed in the CSR.

        Returns:
            Config Object representing the PKCS11 object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)
        attributes = attributes or {}
        pkcs11_attrs = ApplicationAttributes.PKCS11
        attributes.update({
            pkcs11_attrs.hsm_cryptoki_file: cryptoki_file_with_path,
            pkcs11_attrs.hsm_certificate_directory: distribution_directory,
            pkcs11_attrs.hsm_openssl_config_file: openssl_config_file_with_path,
            pkcs11_attrs.hsm_openssl_path: openssl_directory,
            pkcs11_attrs.hsm_token_label: token_slot_identifier,
            pkcs11_attrs.hsm_token_password: token_slot_pin_dn,
            pkcs11_attrs.hsm_requested_usecase: use_case,
            ApplicationAttributes.connection_method: connection_method,
            pkcs11_attrs.hsm_embed_sans_in_csr: embed_sans_in_csr,
            pkcs11_attrs.hsm_import_certificate: import_certificates_into_hsm,
            pkcs11_attrs.hsm_cka_label_format: label_format,
            ApplicationAttributes.port: port,
            pkcs11_attrs.hsm_protection_type: protection_type,
            pkcs11_attrs.hsm_openssl_type: openssl_type,
            pkcs11_attrs.hsm_reverse_subject_dn: reverse_subject_dn
        })
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.pkcs11,
            attributes=attributes
        )


@feature()
class PKCS12(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP PKCS #12 Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a PKCS #12 application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.pkcs12,
            attributes=attributes
        )


@feature()
class RiverbedSteelHead(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Riverbed SteelHead Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Riverbed SteelHead application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.riverbed_steel_head,
            attributes=attributes
        )


@feature()
class TealeafPCA(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP Tealeaf PCA Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Tealeaf PCA application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.tealeaf_pca,
            attributes=attributes
        )


@feature()
class VAMnShield(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP VAM nShield Application objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a VAM nShield application object.

        Args:
            name: Name of the application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config object representation of the application object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.vam_nshield,
            attributes=attributes
        )
