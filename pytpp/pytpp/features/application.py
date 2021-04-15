from pytpp.vtypes import Config
from pytpp.properties.config import ApplicationClassNames, ApplicationAttributes, ApplicationAttributeValues, CertificateAttributes
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.tools.helpers.date_converter import from_date_string


class _ApplicationBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, application: 'Config.Object'):
        """
        Deletes an Application object.

        Args:
            application: Config object of the Application object.
        """
        self._secret_store_delete(object_dn=application.dn)
        self._config_delete(object_dn=application.dn)

    def disable(self, application: 'Config.Object'):
        """
        Disables all processing and provisioning of the application.

        Args:
            application: Config object of the Application object.
        """
        result = self._api.websdk.Config.Write.post(
            object_dn=application.dn,
            attribute_data=self._name_value_list({
                ApplicationAttributes.disabled: ["1"]
            }, keep_list_values=True)
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def enable(self, application: 'Config.Object'):
        """
        Enables all processing and provisioning of the application.

        Args:
            application: Config object of the Application object.
        """
        result = self._api.websdk.Config.ClearAttribute.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.disabled
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def get_associated_certificate(self, application: 'Config.Object'):
        """
        Returns the Certificate object associated to the Application object.

        Args:
            application: Config object of the Application object.

        Returns:
            Config Object of the certificate object.
        """
        response = self._api.websdk.Config.Read.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.certificate
        )

        if not response.values:
            return None

        certificate_dn = response.values[0]
        return self._api.websdk.Config.IsValid.post(object_dn=certificate_dn).object

    def _get_stage(self, application: 'Config.Object'):
        """
        Returns the current processing stage of the application object.

        Args:
            application: Config object of the Application object.

        Returns:
            The current stage if it exists. Otherwise, returns ``None``.
        """
        response = self._api.websdk.Config.Read.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.stage
        )

        return int(response.values[0]) if response.values else None

    def get_stage(self, application: 'Config.Object'):
        """
        Returns the current processing stage of the application object.

        Args:
            application: Config object of the Application object.

        Returns:
            The current stage if it exists. Otherwise, returns ``None``.
        """
        self._get_stage(application=application)

    def get_status(self, application: 'Config.Object'):
        """
        Returns the current processing status of the application object.

        Args:
            application: Config object of the Application object.

        Returns:
            The current status if it exists. Otherwise, returns ``None``.
        """
        response = self._api.websdk.Config.Read.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.status
        )

        return response.values[0] if response.values else None

    def _is_in_error(self, application: 'Config.Object'):
        """
        Returns ``True`` if the application object is in an error state.

        Args:
            application: Config object of the Application object.

        Returns:
            Boolean
        """
        response = self._api.websdk.Config.Read.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.in_error
        )

        return bool(response.values[0]) if response.values else False

    def wait_for_installation_to_complete(self, application: 'Config.Object', timeout: int = 60):
        """
        Waits for the application object's "Last Pushed On" attribute to be a date greater than
        or equal to the "Last Renewed On" date on the associated certificate. If the certificate
        has not been recently renewed and is simply being associated to the certificate, either
        clear the "Last Pushed On" date from the application object or use
        :meth:`pytpp.pytpp.features.certificate.Certificate.associate_application` with
        ``push_to_new=True``.

        Args:
            application: Config object of the Application object.
            timeout: Timeout in seconds.
        """
        certificate_dn = self._api.websdk.Config.Read.post(
            object_dn=application.dn,
            attribute_name=ApplicationAttributes.certificate
        )
        if not certificate_dn.values:
            raise FeatureError.UnexpectedValue(
                f'There is no certificate associated to "{application.dn}" in TPP.'
            )
        response = self._api.websdk.Config.Read.post(
            object_dn=certificate_dn.values[0],
            attribute_name=CertificateAttributes.last_renewed_on
        )

        if not response.values:
            raise FeatureError.UnexpectedValue(
                f'Cannot validate that the certificate "{certificate_dn}" is installed on the application '
                f'"{application.dn}" as it seems that the certificate has never been renewed.'
            )
        certificate_last_renewed_time = from_date_string(response.values[0])

        def _certificate_is_installed():
            resp = self._api.websdk.Config.Read.post(
                object_dn=application.dn,
                attribute_name=ApplicationAttributes.last_pushed_on
            )

            if not resp.values:
                return False
            application_last_pushed_on = from_date_string(resp.values[0])
            return application_last_pushed_on >= certificate_last_renewed_time

        stage = self._get_stage(application=application)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if self._is_in_error(application=application):
                    break
                elif not stage:
                    if not _certificate_is_installed():
                        raise FeatureError.UnexpectedValue(
                            f'Expected a certificate to be installed on "{application.dn}", '
                            f'but the application is not in a processing status.'
                        )
                    return
                stage = self._get_stage(application=application)

        raise FeatureError.UnexpectedValue(
            f'Certificate installation failed on "{application.dn}".\n'
            f'Stage: {stage}\n'
            f'Status: {self.get_status(application=application)}'
        )


@feature()
class A10AXTrafficManager(_ApplicationBase):
    """
    This feature provides high-level interaction with TPP A10 AX Traffic Manager Application objects.
    """

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appa10axtm'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appadaptable'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appamazon'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appapache'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appazurekeyvault'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appbasic'
        })

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
        result = self._api.websdk.Config.MutateObject.post(
            object_dn=basic_application_dn,
            class_name=new_class_name
        )
        result.assert_valid_response()

        if attributes:
            attributes = {k: ([str(v)] if not isinstance(v, list) else v) for k, v in attributes.items()}
            result = self._api.websdk.Config.Write.post(
                object_dn=basic_application_dn,
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            result.assert_valid_response()

        new_object = self._api.websdk.Config.IsValid.post(object_dn=basic_application_dn).object
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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appBlueCoat'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appcapi'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appnetscaler'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appConnectDirect'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appf5ltmadvanced'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appdatapower'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appgsk'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appimpervamx'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appjks'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appjuniper'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appiplanet'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appPaloAlto'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appPem'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a PKCS11 application object.

        Args:
            name: Name of the Apache application object.
            parent_folder_dn: Absolute path to the parent folder of the application object.
            attributes: Additional attributes pertaining to the application object.

        Returns:
            Config Object representing the PKCS11 object.
        """
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'apppkcs11'
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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'apppkcs12'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appriverbedsteelhead'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'apptealeafpca'
        })

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

    def __init__(self, api):
        super().__init__(api=api)

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
        attributes = attributes or {}
        attributes.update({
            ApplicationAttributes.driver_name: 'appvamnshield'
        })

        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=ApplicationClassNames.vam_nshield,
            attributes=attributes
        )
