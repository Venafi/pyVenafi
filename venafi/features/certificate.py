from typing import List
from venafi.properties.config import CertificateClassNames, CertificateAttributes, CertificateAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class Certificate(FeatureBase):
    """
    This feature provides high-level interaction with TPP Server Certificate objects.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def _get(self, certificate_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).get()
        result.assert_valid_response()

        return result

    def associate_application(self, certificate_dn: str, application_dns: list, push_to_new: bool = False):
        """
        Associate an application object to a certificate.
        .. note:: The application object must already be created in TPP.

        Args:
            certificate_dn: Absolute path to the certificate object.
            application_dn: Absolute path to the application object.
            push_to_new: If True, the certificate will be pushed to the application once associated.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not isinstance(application_dns, list):
            application_dns = [application_dns]

        assert self._auth.websdk.Certificates.Associate.post(
            application_dn=application_dns,
            certificate_dn=certificate_dn,
            push_to_new=push_to_new
        ).success

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates the config object that represents the certificate.

        .. note:: The certificate is NOT automatically requested. Use :meth:`renew` to obtain a certificate.

        Args:
            name: Name of the Certificate object.
            parent_folder_dn: Absolute path to the parent folder of the certificate object.
            attributes: Additional attributes that define this certificate.

        Returns:
            Config object representing the certificate object.

        """
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
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
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).delete()
        if not result.success:
            certificate_dn = self._auth.websdk.Config.GuidToDn.post(object_guid=certificate_guid).object_dn
            raise FeatureError(f'Could not delete certificate {certificate_dn}.')

    def details(self, certificate_guid: str):
        return self._get(certificate_guid=certificate_guid).certificate_details

    def dissociate_application(self, certificate_dn: str, application_dn: list, delete_orphans: bool = False):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Dissociate.post(
            certificate_dn=certificate_dn,
            application_dn=application_dn,
            delete_orphans=delete_orphans
        )
        result.assert_valid_response()

    def download(self, certificate_dn: str, format: str, friendly_name: str = None, include_chain: bool = False,
                 include_private_key: bool = False, keystore_password: str = None, password: str = None,
                 root_first_order: bool = False, vault_id: int = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if vault_id:
            result = self._auth.websdk.Certificates.Retrieve.VaultId(vault_id).post(
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )
        else:
            result = self._auth.websdk.Certificates.Retrieve.post(
                certificate_dn=certificate_dn,
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )

        return [result.filename, result.certificate_data]

    def get_previous_versions(self, certificate_guid: str, exclude_expired: bool = False, exclude_revoked: bool = False):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).PreviousVersions.get(
            exclude_expired=exclude_expired,
            exclude_revoked=exclude_revoked
        )
        return result.previous_versions

    def push_to_applications(self, certificate_dn: str, application_dns: List[str] = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not application_dns:
            application_dns = self._auth.websdk.Config.ReadDn.post(
                object_dn=certificate_dn,
                attribute_name=CertificateAttributes.consumers
            ).values

        return self.associate_application(
            certificate_dn=certificate_dn,
            application_dns=application_dns,
            push_to_new=True
        )

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
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        certificate_guid = self._auth.websdk.Config.DnToGuid.post(object_dn=certificate_dn).guid
        current_thumbprint = self.details(certificate_guid=certificate_guid).thumbprint

        result = self._auth.websdk.Certificates.Renew.post(certificate_dn=certificate_dn, pkcs10=csr, reenable=reenable)
        result.assert_valid_response()

        return current_thumbprint

    def retry_from_current_stage(self, certificate_dn: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Retry.post(certificate_dn=certificate_dn)
        result.assert_valid_response()

    def retry_from_stage_0(self, certificate_dn: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=True)

        result.assert_valid_response()

        if not result.restart_completed:
            raise FeatureError.UnexpectedValue('Restart renewal from stage 0 was not triggered.')

    def reset_to_stage_0(self, certificate_dn: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=False)

        result.assert_valid_response()

        if not result.processing_reset_completed:
            raise FeatureError.UnexpectedValue(f'Processing reset was not completed for {certificate_dn}.')

    def revoke(self, certificate_dn: str, comments: str = None, disable: bool = None,
               reason: int = None, thumbprint: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Revoke.post(
            certificate_dn=certificate_dn,
            comments=comments,
            disable=disable,
            reason=reason,
            thumbprint=thumbprint
        )
        result.assert_valid_response()
        try:
            assert result.success is True  # TPP may not return "Success", which will throw an error.
        except:
            raise FeatureError.UnexpectedValue(
                f'Cannot revoke {certificate_dn} due to this error:\n{result.error}.'
            )

    def upload(self, certificate_data: str, parent_folder_dn: str, certificate_authority_attributes: dict = None, name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if certificate_authority_attributes:
            certificate_authority_attributes = self._name_value_list(attributes=certificate_authority_attributes)

        result = self._auth.websdk.Certificates.Import.post(
            certificate_data=certificate_data,
            policy_dn=parent_folder_dn,
            ca_specific_attributes=certificate_authority_attributes,
            object_name=name,
            password=password,
            private_key_data=private_key_data,
            reconcile=reconcile
        )

        result.assert_valid_response()

        return self._auth.websdk.Config.IsValid.post(object_dn=result.certificate_dn).object

    def validate(self, certificate_dns: List[str]):
        if not isinstance(certificate_dns, list):
            certificate_dns = [certificate_dns]

        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Validate.post(certificate_dns=certificate_dns)
        return [result.validated_certificate_dns, result.warnings]

    def wait_for_renewal_complete(self, certificate_guid: str, current_thumbprint: str, timeout: int = 60):
        cert = self._get(certificate_guid=certificate_guid)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                cert.assert_valid_response()
                thumbprint = cert.certificate_details.thumbprint
                if thumbprint and thumbprint != current_thumbprint and cert.processing_details.stage is None:
                    return cert.certificate_details
                cert = self._get(certificate_guid=certificate_guid)

        raise FeatureError.UnexpectedValue(
            f'Certificate renewal for "{cert.dn}" encountered an error at stage {cert.processing_details.stage} with '
            f'status "{cert.processing_details.status}".'
        )

    def wait_for_stage(self, certificate_guid: str, stage: int, timeout: int = 60):
        cert = self._get(certificate_guid=certificate_guid)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if cert.processing_details.in_error:
                    raise FeatureError.UnexpectedValue(
                        f'Certificate renewal encountered an error at stage {cert.processing_details.stage} with '
                        f'status "{cert.processing_details.status}".'
                    )
                elif cert.processing_details.stage == stage:
                    return cert
                cert = self._get(certificate_guid=certificate_guid)

        raise FeatureError.UnexpectedValue(
            f'Certificate renewal did not reach stage {stage} after {timeout} seconds. The current stage is '
            f'{cert.processing_details.stage} with status {cert.processing_details.status}.'
        )
