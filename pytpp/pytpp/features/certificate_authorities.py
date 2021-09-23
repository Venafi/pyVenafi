from pytpp.vtypes import Config
from pytpp.properties.config import CertificateAuthorityClassNames
from pytpp.attributes.adaptable_ca import AdaptableCAAttributes
from pytpp.attributes.microsoft_ca import MicrosoftCAAttributes
from pytpp.attributes.self_signed_ca import SelfSignedCAAttributes
from pytpp.features.bases.feature_base import FeatureBase, feature


class _CertificateAuthorityBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, certificate_authority: 'Config.Object'):
        """
        Deletes the Certificate Authority object from TPP, including all of the secrets associated to it.

        Args:
            certificate_authority: Config object of the CA object.
        """
        certificate_authority_dn = self._get_dn(certificate_authority)
        self._secret_store_delete(object_dn=certificate_authority_dn)
        self._config_delete(object_dn=certificate_authority_dn)

    def get(self, certificate_authority_dn: str, raise_error_if_not_exists: bool = True):
        """
        Get the Certificate Authority object in TPP.

        Args:
            certificate_authority_dn: DN of the Certificate Authority.
            raise_error_if_not_exists: Raise an exception if the object DN does not exist.

        Returns:
            Config object representing the Certificate Authority.
        """
        return self._get_config_object(
            object_dn=certificate_authority_dn,
            raise_error_if_not_exists=raise_error_if_not_exists,
            valid_class_names=list(CertificateAuthorityClassNames)
        )


@feature()
class AdaptableCA(_CertificateAuthorityBase):
    """
    This feature provides high-level interaction with TPP Adaptable Certificate Authority objects.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, powershell_script: str, username_credential_dn: str = None,
               certificate_credential_dn: str = None, secondary_credential_dn: str = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Creates a Microsoft Certificate Authority object.

        Args:
            name: Name of the CA object.
            parent_folder_dn: Absolute path to the parent folder of the CA object.
            powershell_script: Name of the PowerShell script located at `C:\\Program Files\\Venafi\\Scripts\\AdaptableCA`
            username_credential_dn: Absolute path to the Username/Password credential object. This is required by TPP if no
                ``certificate_credential_dn`` is given.
            certificate_credential_dn: Absolute path to the Certificate credential object. This is required by TPP if no
                ``username_credential_dn`` is given.
            secondary_credential_dn: Absolute path to the secondary credential object.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the certificate authority.
        """
        attributes = attributes or {}
        attributes.update({
            AdaptableCAAttributes.interoperability_script: powershell_script,
            AdaptableCAAttributes.credential: username_credential_dn,
            AdaptableCAAttributes.certificate_credential: certificate_credential_dn,
            AdaptableCAAttributes.secondary_credential: secondary_credential_dn,
            AdaptableCAAttributes.driver_name: 'caadaptable'
        })
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=CertificateAuthorityClassNames.adaptable_ca,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class MSCA(_CertificateAuthorityBase):
    """
    This feature provides high-level interaction with TPP Microsoft Certificate Authority objects.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, hostname: str, service_name: str, credential_dn: str,
               template: str, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Creates a Microsoft Certificate Authority object.

        Args:
            name: Name of the CA object.
            parent_folder_dn: Absolute path to the parent folder of the CA object.
            hostname: Hostname or IP Address of the CA.
            service_name: Service, or Given, Name of the certificate authority.
            credential_dn: Absolute path to the credential object.
            template: Name of the CA template.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the certificate authority.
        """
        attributes = attributes or {}
        attributes.update({
            MicrosoftCAAttributes.host: hostname,
            MicrosoftCAAttributes.given_name: service_name,
            MicrosoftCAAttributes.credential: credential_dn,
            MicrosoftCAAttributes.template: template,
            MicrosoftCAAttributes.driver_name: 'camicrosoft'
        })
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=CertificateAuthorityClassNames.microsoft_ca,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class SelfSignedCA(_CertificateAuthorityBase):
    """
    This feature provides high-level interaction with TPP Self-Signed Certificate Authority objects.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Creates a Self-Signed Certificate Authority object.

        Args:
            name: Name of the CA object.
            parent_folder_dn: Absolute path to the parent folder of the CA object.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the certificate authority.
        """
        attributes = attributes or {}
        attributes.update({
            SelfSignedCAAttributes.driver_name: 'caselfsigned'
        })
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=CertificateAuthorityClassNames.self_signed_ca,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )
