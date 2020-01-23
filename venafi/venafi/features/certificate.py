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

        Args:
            certificate_dn: Absolute path to the certificate object.
            application_dns: A list of absolute paths to each application object.
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
            certificate_guid: GUID of the certificate object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).delete()
        if not result.success:
            certificate_dn = self._auth.websdk.Config.GuidToDn.post(object_guid=certificate_guid).object_dn
            raise FeatureError(f'Could not delete certificate {certificate_dn}.')

    def details(self, certificate_guid: str):
        """
        Returns details of the actual certificate and not the renewal settings for the object.
        
        Args:
            certificate_guid: GUID of the certificate object. 

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
        return self._get(certificate_guid=certificate_guid).certificate_details

    def dissociate_application(self, certificate_dn: str, application_dns: list, delete_orphans: bool = False):
        """
        Associate an application object to a certificate.

        Args:
            certificate_dn: Absolute path to the certificate object.
            application_dns: A list of absolute paths to each application object.
            delete_orphans: Delete the Application DN. Only delete the corresponding Device DN when it has no child objects.
                Otherwise retain only the Device DN and its children. Use this option to completely remove the application
                object and corresponding device objects.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Dissociate.post(
            certificate_dn=certificate_dn,
            application_dn=application_dns,
            delete_orphans=delete_orphans
        )
        result.assert_valid_response()

    def download(self, certificate_dn: str, format: str, friendly_name: str = None, include_chain: bool = False,
                 include_private_key: bool = False, keystore_password: str = None, password: str = None,
                 root_first_order: bool = False, vault_id: int = None):
        """
        Downloads a certificate and returns the encoded content, filename, and format as a single object. If ``vault_id``
        is provided, then that specific version of a certificate is downloaded. This is particularly useful when
        trying to download historical certificates.

        Args:
            certificate_dn: Absolute path to the certificate object.
            format: One of the following:
                * Base64
                * Base64 (PKCS #8)
                * DER
                * JKS
                * PKCS #7
                * PKCS #12
            friendly_name: Label or alias for the given format.
            include_chain: Include parent or root chain.
            include_private_key: Include the private key.
            keystore_password: JKS Keystore password.
            password: Password.
            root_first_order: If True, show root certificate first, followed by intermediate, and finally the
                end entity certificate.
            vault_id: If provided, downloads the certificate with the given Vault ID. Use this when trying
                to download historical certificates.

        Returns:
            A single object with these properties:
            * Encoded Certificate Data
            * File Format
            * File name
        """
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

        return result

    def get_previous_versions(self, certificate_guid: str, exclude_expired: bool = False, exclude_revoked: bool = False):
        """
        Returns all of the historical certificates and their details related to the given certificate GUID.

        Args:
            certificate_guid: GUID of the certificate object.
            exclude_expired: If True, do not include expired certificates.
            exclude_revoked: If True, do not include revoked certificates.

        Returns:
            A list of historical certificates related to the certificate GUID.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).PreviousVersions.get(
            exclude_expired=exclude_expired,
            exclude_revoked=exclude_revoked
        )
        return result.previous_versions

    def get_tickets(self, certificate_dn: str):
        """
        Reads the Ticket DN attribute of the certificate and returns a list of all tickets.

        Args:
            certificate_dn: Absolute path to the certificate object.

        Returns:
            List of Config Objects
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ticket_names = self._auth.websdk.Workflow.Ticket.Enumerate.post(
            object_dn=certificate_dn
        ).guids

        ticket_dns = [
            self._auth.websdk.Config.IsValid.post(object_dn=f'\\VED\\Workflow\\{ticket_name}').object
            for ticket_name in ticket_names
        ]

        return ticket_dns

    def get_validation_results(self, certificate_guid: str):
        """
        Returns the file and SSL/TLS validation results for each of the applications
        associated to the certificate GUID.

        Args:
            certificate_guid: GUID of the certificate.

        Returns:
            File and SSL/TLS validation results for each of the applications
            associated to the certificate GUID.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Guid(certificate_guid).ValidationResults.get()
        return [result.file, result.ssltls]

    def push_to_applications(self, certificate_dn: str, application_dns: List[str] = None):
        """
        Push the active certificate of the Certificate DN to the given Application DNs.
        Args:
            certificate_dn: Absolute path to the certificate object.
            application_dns: A list of application DNs to push certificates.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if not application_dns:
            application_dns = self._auth.websdk.Config.ReadDn.post(
                object_dn=certificate_dn,
                attribute_name=CertificateAttributes.consumers
            ).values

        self.associate_application(
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

    def reset(self, certificate_dn: str):
        """
        Resets the certificate to a non-processing state. Technically, the stage in "none". No attempt
        to reprocess the certificate renewal is made.

        Args:
            certificate_dn: Absolute path to the certificate object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=False)

        result.assert_valid_response()

        if not result.processing_reset_completed:
            raise FeatureError.UnexpectedValue(f'Processing reset was not completed for {certificate_dn}.')

    def retry_from_current_stage(self, certificate_dn: str):
        """
        Retries renewal from the current processing stage of the certificate.

        Args:
            certificate_dn: Absolute path to the certificate object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Retry.post(certificate_dn=certificate_dn)
        result.assert_valid_response()

    def retry_from_stage_0(self, certificate_dn: str):
        """
        Retries renewal from stage 0. This clears all current processing data and restarts
        processing.

        Args:
            certificate_dn: Absolute path to the certificate object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=True)

        result.assert_valid_response()

        if not result.restart_completed:
            raise FeatureError.UnexpectedValue('Restart renewal from stage 0 was not triggered.')

    def revoke(self, certificate_dn: str, comments: str = None, disable: bool = None,
               reason: int = None, thumbprint: str = None):
        """
        Revokes the certificate. If a thumbprint is provided, then the particular historical certificate
        associated to the certificate DN whose thumbprint matches will be revoked.

        Args:
            certificate_dn: Absolute path to the certificate object.
            comments: Any comments to include in the revoke request.
            disable: If True, disables the certificate object.
            reason: Reason for revoking.
            thumbprint: If given, the thumbprint of the historical certificate to be revoked.

        Returns:

        """
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
        """
        Validates the certificate on all applications associated to certificate that are not disabled.

        Args:
            certificate_dns: List of certificate DNs to validate.

        Returns:
            Validation results.
        """
        if not isinstance(certificate_dns, list):
            certificate_dns = [certificate_dns]

        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Certificates.Validate.post(certificate_dns=certificate_dns)
        return result

    def wait_for_renewal_complete(self, certificate_guid: str, current_thumbprint: str, timeout: int = 60):
        """
        Waits for the certificate renewal to complete over a period of ``timeout`` seconds. The `current_thumbprint``
        is returned by :meth:`renew`. Renewal is complete when the ``current_thumbprint`` does not match the new
        thumbprint AND there is no processing stage.

        Args:
            certificate_guid: GUID of the certificate object.
            current_thumbprint: Thumbprint of the `current` certificate object.
            timeout: Timeout in seconds before raising an error.

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
        """
        Waits for the current processing of the certificate to reach the given ``stage`` over a period of
        ``timeout`` seconds. If the timeout is reached, an error is thrown.

        Args:
            certificate_guid: GUID of the certificate object.
            stage: Stage at which to return
            timeout: Timeout in seconds before throwing an error.

        Returns:
            Certificate and processing details.
        """
        cert = self._get(certificate_guid=certificate_guid)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if cert.processing_details.stage == stage:
                    return cert
                cert = self._get(certificate_guid=certificate_guid)

        raise FeatureError.UnexpectedValue(
            f'Certificate renewal did not reach stage {stage} after {timeout} seconds. The current stage is '
            f'{cert.processing_details.stage} with status {cert.processing_details.status}.'
        )
