from venafi.properties.config import CertificateClassNames, CertificateAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class Certificate(FeatureBase):
    """
    This feature provides high-level interaction with TPP Server Certificate objects.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def associate_application(self, certificate_dn: str, application_dn: list, push_to_new: bool = False):
        """
        Associate an application object to a certificate.
        .. note:: The application object must already be created in TPP.

        Args:
            certificate_dn: Absolute path to the certificate object.
            application_dn: Absolute path to the application object.
            push_to_new: If True, the certificate will be pushed to the application once associated.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not isinstance(application_dn, list):
            application_dn = [application_dn]

        assert self.auth.websdk.Certificates.Associate.post(
            application_dn=application_dn,
            certificate_dn=certificate_dn,
            push_to_new=push_to_new
        ).success

    def create(self, name: str, container: str, attributes: dict = None):
        """
        Creates the config object that represents the certificate.

        .. note:: The certificate is NOT automatically requested. Use :meth:`renew` to obtain a certificate.

        Args:
            name: Name of the Certificate object.
            container: Absolute path to the parent folder of the certificate object.
            attributes: Additional attributes that define this certificate.

        Returns:
            Config object representing the certificate object.

        """
        return self._config_create(
            name=name,
            container=container,
            config_class=CertificateClassNames.x509_certificate,
            attributes=attributes
        )

    def delete(self, certificate_guid: str):
        """
        Deletes the certificate object from TPP.

        .. note:: This method does not affect the actual certificate installed on any application.

        Args:
            certificate_guid: Guid representing the certificate object.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Certificates.Guid(certificate_guid).delete()
        if not result.success:
            certificate_dn = self.auth.websdk.Config.GuidToDn.post(object_guid=certificate_guid).object_dn
            raise FeatureError(f'Could not delete certificate {certificate_dn}.')

    def renew(self, certificate_dn: str, csr: str = None, reenable: bool = False):
        """
        Renews or requests a certificate.

        Args:
            certificate_dn: Absolute path to the certificate object.
            csr: If provided, uploads the PKCS10 CSR to TPP to send to the CA. If not provided, TPP generates the CSR.
            reenable: The action to control a previously disabled certificate:
                If False, do not renew a previously disabled certificate.
                If True, lear the Disabled attribute, reenable, and then renew the certificate (in this request).
                Reuse the same CertificateDN, that is also known as a Certificate object.

        Returns:
            Certificate details regarding the request and renewal.

        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        certificate_guid = self.auth.websdk.Config.DnToGuid.post(object_dn=certificate_dn).guid
        prev_thumbprint = self.auth.websdk.Certificates.Guid(certificate_guid).get().certificate_details.thumbprint

        assert self.auth.websdk.Certificates.Renew.post(certificate_dn=certificate_dn, pkcs10=csr, reenable=reenable).success

        def validate_thumbprint():
            thumbprint = self.auth.websdk.Certificates.Guid(certificate_guid).get().certificate_details.thumbprint
            return thumbprint != prev_thumbprint

        self._wait_for_method(validate_thumbprint, True, 60)
        return self.auth.websdk.Certificates.Guid(certificate_guid).get().certificate_details
