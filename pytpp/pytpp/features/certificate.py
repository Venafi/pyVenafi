from typing import List
from pytpp.vtypes import Config
from pytpp.properties.config import CertificateClassNames, CertificateAttributes, CertificateAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature


@feature()
class Certificate(FeatureBase):
    """
    This feature provides high-level interaction with TPP Certificate objects.
    """

    def __init__(self, api):
        super().__init__(api)

    def _get(self, certificate: 'Config.Object'):
        result = self._api.websdk.Certificates.Guid(certificate.guid).get()
        result.assert_valid_response()

        return result

    def associate_application(self, certificate: 'Config.Object', application_dns: List[str], push_to_new: bool = False):
        """
        Associate an application object to a certificate.

        Args:
            certificate: Config object of the certificate.
            application_dns: A list of absolute paths to each application object.
            push_to_new: If True, the certificate will be pushed to the application once associated.
        """
        if not isinstance(application_dns, list):
            application_dns = [application_dns]

        assert self._api.websdk.Certificates.Associate.post(
            application_dn=application_dns,
            certificate_dn=certificate.dn,
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

    def delete(self, certificate: 'Config.Object'):
        """
        Deletes the certificate object from TPP.

        .. note:: This method does not affect the actual certificate installed on any application.

        Args:
            certificate: Config object of the certificate.
        """
        result = self._api.websdk.Certificates.Guid(certificate.guid).delete()
        if not result.is_valid_response():
            raise FeatureError(f'Could not delete certificate {certificate.dn}.')

    def details(self, certificate: 'Config.Object'):
        """
        Returns details of the actual certificate and not the renewal settings for the object.

        Args:
            certificate: Config object of the certificate.

        Returns:
            A single object with these properties:
            * C (Country)
            * CN (Common Name)
            * EnhancedKeyUsage
            * Issuer
            * KeyAlgorithm
            * KeySize
            * KeyUsage
            * L (City or Location)
            * O (Organization)
            * OU (Organizational Units)
            * PublicKeyHash
            * S (State)
            * SKIKeyIdentifier (Subject Key Identifier)
            * Serial
            * SignatureAlgorithm
            * SignatureAlgorithmOID
            * StoreAdded
            * Subject
            * SubjectAltNameDNS
            * SubjectAltNameEmail
            * SubjectAltNameIp
            * SubjectAltNameUpn
            * SubjectAltNameUri
            * Thumbprint
            * ValidFrom
            * ValidTo
        """
        return self._get(certificate=certificate).certificate_details

    def dissociate_application(self, certificate: 'Config.Object', application_dns: List[str], delete_orphans: bool = False):
        """
        Associate an application object to a certificate.

        Args:
            certificate: Config object of the certificate.
            application_dns: A list of absolute paths to each application object.
            delete_orphans: Delete the Application DN. Only delete the corresponding Device DN when it has no child objects.
                Otherwise retain only the Device DN and its children. Use this option to completely remove the application
                object and corresponding device objects.
        """
        result = self._api.websdk.Certificates.Dissociate.post(
            certificate_dn=certificate.dn,
            application_dn=application_dns,
            delete_orphans=delete_orphans
        )
        result.assert_valid_response()

    def download(self, format: str, certificate: 'Config.Object' = None, friendly_name: str = None,
                 include_chain: bool = False, include_private_key: bool = False, keystore_password: str = None,
                 password: str = None, root_first_order: bool = False, vault_id: int = None):
        """
        Downloads a certificate and returns the encoded content, filename, and format as a single object. If ``vault_id``
        is provided, then that specific version of a certificate is downloaded. This is particularly useful when
        trying to download historical certificates.

        Args:
            format: One of the following:
                * Base64
                * Base64 (PKCS #8)
                * DER
                * JKS
                * PKCS #7
                * PKCS #12
            certificate: Config object of the certificate. Not required if using vault id.
            friendly_name: Label or alias for the given format.
            include_chain: Include parent or root chain.
            include_private_key: Include the private key.
            keystore_password: JKS Keystore password.
            password: Password.
            root_first_order: If True, show root certificate first, followed by intermediate, and finally the
                end entity certificate.
            vault_id: If provided, downloads the certificate with the given Vault ID. Use this when trying
                to download historical certificates. Not required if using certificate config object.

        Returns:
            A single object with these properties:
            * Encoded Certificate Data
            * File Format
            * File name
        """
        if vault_id:
            result = self._api.websdk.Certificates.Retrieve.VaultId(vault_id).post(
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )
        else:
            result = self._api.websdk.Certificates.Retrieve.post(
                certificate_dn=certificate.dn,
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )

        return result

    def get_previous_versions(self, certificate: 'Config.Object', exclude_expired: bool = False, exclude_revoked: bool = False):
        """
        Returns all of the historical certificates and their details related to the given certificate GUID.

        Args:
            certificate: Config object of the certificate.
            exclude_expired: If True, do not include expired certificates.
            exclude_revoked: If True, do not include revoked certificates.

        Returns:
            A list of historical certificates related to the certificate GUID.
        """
        result = self._api.websdk.Certificates.Guid(certificate.guid).PreviousVersions.get(
            exclude_expired=exclude_expired,
            exclude_revoked=exclude_revoked
        )
        return result.previous_versions

    def get_validation_results(self, certificate: 'Config.Object'):
        """
        Returns the file and SSL/TLS validation results for each of the applications
        associated to the certificate.

        Args:
            certificate: Config object of the certificate.

        Returns:
            File and SSL/TLS validation results for each of the applications
            associated to the certificate.
        """
        result = self._api.websdk.Certificates.Guid(certificate.guid).ValidationResults.get()
        return [result.file, result.ssl_tls]

    def push_to_applications(self, certificate: 'Config.Object', application_dns: List[str] = None):
        """
        Push the active certificate to the given Application DNs.

        Args:
            certificate: Config object of the certificate.
            application_dns: A list of application DNs.
        """
        if not application_dns:
            application_dns = self._api.websdk.Config.ReadDn.post(
                object_dn=certificate.dn,
                attribute_name=CertificateAttributes.consumers
            ).values

        self.associate_application(
            certificate=certificate,
            application_dns=application_dns,
            push_to_new=True
        )

    def renew(self, certificate: 'Config.Object', csr: str = None, re_enable: bool = False):
        """
        Renews or requests a certificate.

        Args:
            certificate: Config object of the certificate.
            csr: If provided, uploads the PKCS10 CSR to TPP to send to the CA. If not provided, TPP generates the CSR.
            re_enable: The action to control a previously disabled certificate:
                If False, do not renew a previously disabled certificate.
                If True, clear the Disabled attribute, re-enable, and then renew the certificate (in this request).

        Returns:
            Certificate details regarding the request and renewal.

        """
        current_thumbprint = self.details(certificate=certificate).thumbprint
        result = self._api.websdk.Certificates.Renew.post(certificate_dn=certificate.dn, pkcs10=csr, reenable=re_enable)
        result.assert_valid_response()
        return current_thumbprint

    def reset(self, certificate: 'Config.Object'):
        """
        Resets the certificate to a non-processing state. No attempt to reprocess the certificate renewal is made.

        Args:
            certificate: Config object of the certificate.
        """
        result = self._api.websdk.Certificates.Reset.post(certificate_dn=certificate.dn, restart=False)
        result.assert_valid_response()
        if not result.processing_reset_completed:
            raise FeatureError.UnexpectedValue(f'Processing reset was not completed for {certificate.dn}.')

    def retry_from_current_stage(self, certificate: 'Config.Object'):
        """
        Retries renewal from the current processing stage of the certificate.

        Args:
            certificate: Config object of the certificate.
        """
        result = self._api.websdk.Certificates.Retry.post(certificate_dn=certificate.dn)
        result.assert_valid_response()

    def retry_from_stage_0(self, certificate: 'Config.Object'):
        """
        Retries renewal from stage 0. This clears all current processing data and restarts
        processing.

        Args:
            certificate: Config object of the certificate.
        """
        result = self._api.websdk.Certificates.Reset.post(certificate_dn=certificate.dn, restart=True)
        result.assert_valid_response()
        if not result.restart_completed:
            raise FeatureError.UnexpectedValue(f'Restart renewal from stage 0 was not triggered on {certificate.dn}.')

    def revoke(self, certificate: 'Config.Object', comments: str = None, disable: bool = None,
               reason: int = None, thumbprint: str = None):
        """
        Revokes the certificate. If a thumbprint is provided, then the particular historical certificate
        associated to the certificate having that thumbprint will be revoked.

        Args:
            certificate: Config object of the certificate.
            comments: Any comments to include in the revoke request.
            disable: If True, disables the certificate object.
            reason: Reason for revoking.
            thumbprint: If given, the thumbprint of the historical certificate to be revoked.

        Returns:

        """
        result = self._api.websdk.Certificates.Revoke.post(
            certificate_dn=certificate.dn,
            comments=comments,
            disable=disable,
            reason=reason,
            thumbprint=thumbprint
        )
        result.assert_valid_response()
        if result.success is not True:
            raise FeatureError.UnexpectedValue(
                f'Cannot revoke {certificate.dn} due to this error:\n{result.error}.'
            )

    def upload(self, certificate_data: str, parent_folder_dn: str, certificate_authority_attributes: dict = None, name: str = None,
               password: str = None, private_key_data: str = None, reconcile: bool = False):
        """
        Uploads the certificate data to TPP to create a certificate object under the given parent folder DN. If the BEGIN/END
        header or footer is missing, the data is assumed to be Base 64 encoded in the PKCS#12 format. For Base 64 encoded
        certificates, characters, such as spaces and new line escape characters (/n), are optional. White space characters are
        removed before any attempt is made to decode the certificate.

        Args:
            certificate_data: Encoded certificate data.
            parent_folder_dn: Absolute path to the parent folder DN.
            certificate_authority_attributes: Attributes pertaining to the Certificate Authority to store with the certificate
                object. This is not a DN to a Certificate Authority in TPP.
            name: If given, the name of the new certificate object. If not given, then the Common Name is used.
            password: Password to decrypt the private key.
            private_key_data: Encoded private key data.
            reconcile: If False, replaces the current certificate, if it exists, and stores the current certificate as a
                historical certificate. If True, then TPP activates the certificate with the newest "ValidFrom" date and
                archives the other certificate as a historical certificate.

        Returns:
            Config object representing the (new) certificate object.
        """
        if certificate_authority_attributes:
            certificate_authority_attributes = self._name_value_list(attributes=certificate_authority_attributes)

        result = self._api.websdk.Certificates.Import.post(
            certificate_data=certificate_data,
            policy_dn=parent_folder_dn,
            ca_specific_attributes=certificate_authority_attributes,
            object_name=name,
            password=password,
            private_key_data=private_key_data,
            reconcile=reconcile
        )
        result.assert_valid_response()
        return self._api.websdk.Config.IsValid.post(object_dn=result.certificate_dn).object

    def validate(self, certificates: 'List[Config.Object]'):
        """
        Validates the certificate on all applications associated to certificate that are not disabled.

        Args:
            certificates: List of certificate config objects to validate.

        Returns:
            Validation results.
        """
        result = self._api.websdk.Certificates.Validate.post(certificate_dns=[c.dn for c in certificates])
        return result

    def wait_for_enrollment_to_complete(self, certificate: 'Config.Object', current_thumbprint: str, timeout: int = 60):
        """
        Waits for the certificate renewal to complete over a period of ``timeout`` seconds. The ``current_thumbprint``
        is returned by :meth:`renew`. Renewal is complete when the ``current_thumbprint`` does not match the new
        thumbprint and either the processing stage is "none" or greater than or equal to 800, which is the start of the
        provisioning stage. If the certificate management type is set to *Provisioning*, use the application feature
        :meth:`pytpp.pytpp.features.application._ApplicationBase`.

        See TPP WebSDK documentation "GET Certificate/<GUID>" for details on what is returned. Only the "CertificateDetails"
        is returned.

        Args:
            certificate: Config object of the certificate.
            current_thumbprint: Thumbprint of the `current` certificate object.
            timeout: Timeout in seconds before raising an error.

        Returns:
            Certificate details object.
        """
        cert = self._get(certificate=certificate)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                cert.assert_valid_response()
                thumbprint = cert.certificate_details.thumbprint
                if thumbprint and thumbprint != current_thumbprint and cert.processing_details.stage in {None, 800}:
                    return cert.certificate_details
                elif cert.processing_details.in_error:
                    break
                cert = self._get(certificate=certificate)

        raise FeatureError.UnexpectedValue(
            f'Certificate renewal for "{cert.dn}" encountered an error at stage {cert.processing_details.stage} with '
            f'status "{cert.processing_details.status}".'
        )

    def wait_for_stage(self, certificate: 'Config.Object', stage: int, expect_workflow: bool = True, timeout: int = 60):
        """
        Waits for the current processing of the certificate to reach the given ``stage`` over a period of
        ``timeout`` seconds. If the timeout is reached, an error is raised.

        Args:
            certificate: Config object of the certificate.
            stage: Stage at which to return
            expect_workflow: If ``True``, validates that a Ticket DN has been issued to the certificate.
            timeout: Timeout in seconds before throwing an error.

        Returns:
            Certificate and processing details.
        """
        cert = self._get(certificate=certificate)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if cert.processing_details.in_error is True:
                    break
                if cert.processing_details.stage is not None:
                    if expect_workflow and cert.processing_details.stage == stage:
                        if 'pending workflow resolution' in cert.processing_details.status.lower():
                            return cert
                    elif not expect_workflow and cert.processing_details.stage >= stage:
                        return cert
                cert = self._get(certificate=certificate)

        if expect_workflow and stage == cert.processing_details.stage:
            msg = f'After {timeout} seconds certificate renewal reached stage {stage}, but no workflow was issued. ' \
                  f'The current stage is {cert.processing_details.stage} with status {cert.processing_details.status}.'
        else:
            msg = f'Certificate renewal did not reach stage {stage} after {timeout} seconds. The current ' \
                  f'stage is {cert.processing_details.stage} with status {cert.processing_details.status}.'
        raise FeatureError.UnexpectedValue(msg)
