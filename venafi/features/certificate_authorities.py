from venafi.properties.config import CertificateAuthorityClassNames, CertificateAuthorityAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _CertificateAuthorityBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str):
        """
        Deletes the Certificate Authority object from TPP, including all of the secrets associated to it.

        Args:
            object_dn: Absolute path to the CA object.

        Returns:

        """
        self._secret_store_delete_by_dn(object_dn=object_dn)
        self._config_delete(object_dn=object_dn)


@feature()
class MSCA(_CertificateAuthorityBase):
    """
    This feature provides high-level interaction with TPP Microsoft Certificate Authority objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, hostname: str, service_name: str, credential_dn: str,
               template: str, attributes: dict = None):
        """
        Creates a Microsoft Certificate Authority object.

        Args:
            name: Name of the CA object.
            container: Absolute path to the parent folder of the CA object.
            hostname: Hostname or IP Address of the CA.
            service_name: Service, or Given, Name of the certificate authority.
            credential_dn: Absolute path to the credential object.
            template: Name of the CA template.
            attributes: Additional attributes associated to the CA object.

        Returns:
            Config object representing the certificate authority.

        """
        attributes = attributes or {}
        attributes.update({
            CertificateAuthorityAttributes.MSCA.host: hostname,
            CertificateAuthorityAttributes.MSCA.given_name: service_name,
            CertificateAuthorityAttributes.MSCA.credential: credential_dn,
            CertificateAuthorityAttributes.MSCA.template: template,
            CertificateAuthorityAttributes.MSCA.driver_name: 'camicrosoft'
        })
        return self._config_create(
            name=name,
            container=container,
            config_class=CertificateAuthorityClassNames.microsoft_ca,
            attributes=attributes
        )


@feature()
class SelfSigned(_CertificateAuthorityBase):
    """
    This feature provides high-level interaction with TPP Self-Signed Certificate Authority objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, attributes: dict = None):
        """
        Creates a Self-Signed Certificate Authority object.

        Args:
            name: Name of the CA object.
            container: Absolute path to the parent folder of the CA object.
            attributes: Additional attributes associated to the CA object.

        Returns:
            Config object representing the certificate authority.

        """
        attributes = attributes or {}
        attributes.update({
            CertificateAuthorityAttributes.SelfSigned.driver_name: 'caselfsigned'
        })
        return self._config_create(
            name=name,
            container=container,
            config_class=CertificateAuthorityClassNames.self_signed_ca,
            attributes=attributes
        )
