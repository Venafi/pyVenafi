from properties.config import ConfigClass, CertificateAttributes
from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _CertificateBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth)

    def associate_application(self, certificate_dn: str, application_dn: list, push_to_new: bool = False):
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
        return self._config_create(
            name=name,
            container=container,
            config_class=ConfigClass.x509_certificate,
            attributes=attributes
        )

    def renew(self, certificate_dn: str, csr: str = None, reenable: bool = False):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        certificate_guid = self.auth.websdk.Config.DnToGuid.post(object_dn=certificate_dn).guid
        prev_thumbprint = self.auth.websdk.Certificates.Guid(certificate_guid).get().certificate_details.thumbprint

        assert self.auth.websdk.Certificates.Renew.post(certificate_dn=certificate_dn, pkcs10=csr, reenable=reenable).success

        def validate_thumbprint():
            thumbprint = self.auth.websdk.Certificates.Guid(certificate_guid).get().certificate_details.thumbprint
            return thumbprint != prev_thumbprint

        self._wait(validate_thumbprint, True, 60)
        return self.auth.websdk.Certificates.Guid(certificate_guid).get()


@feature()
class ServerCertificate(_CertificateBase):
    def __init__(self, auth):
        super().__init__(auth)

    def delete(self, certificate_guid: str):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not self.auth.websdk.Certificates.Guid(certificate_guid).delete().success:
            raise FeatureError.GeneralError('Could not delete certificate.')
