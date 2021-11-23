from pytpp.attributes.microsoft_ca import MicrosoftCAAttributes
from pytpp.attributes.self_signed_ca import SelfSignedCAAttributes
from pytpp.features.bases.feature_base import FeatureBase, feature
from typing import Union, List, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config, Identity


class _CertificateAuthorityBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, certificate_authority: 'Union[Config.Object, str]'):
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
            raise_error_if_not_exists=raise_error_if_not_exists
        )


@feature()
class MSCA(_CertificateAuthorityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', hostname: str, service_name: str,
               credential: 'Union[Config.Object, str]', template: str, description: 'str' = None,
               contacts: 'List[Identity.Identity, str]' = None, manual_approvals: 'bool' = None,
               subject_alt_name_enabled: 'bool' = None, automatically_include_cn_as_dns_san: 'bool' = None,
               allow_users_to_specify_end_date: 'bool' = None, enrollment_agent: 'Union[Config.Object, str]' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Creates a Microsoft Certificate Authority object.

        Args:
            name: Name of the CA object.
            parent_folder: ``Config.Object`` or DN of the parent folder of this Certificate Authority object.
            hostname: Hostname or IP Address of the CA.
            service_name: Service, or Given, Name of the certificate authority.
            credential: ``Config.Object`` or DN of the MSCA creential.
            template: Name of the CA template.
            description: Description of the CA object.
            contacts: List of ``Identity.Identity`` or prefixed universal GUIDs of the contacts.
            manual_approvals: Require manual approvals.
            subject_alt_name_enabled: Enable Subject Alterntaive Names.
            automatically_include_cn_as_dns_san: Automatically include the common name (CN) as a DNS SAN.
            allow_users_to_specify_end_date: Allow users to specify the end date.
            enrollment_agent: ``Config.Object`` or DN of the certificate credential, or enrollment agent.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            ``Config.Object``
        """
        attributes = attributes or {}
        attributes.update({
            MicrosoftCAAttributes.driver_name: 'camicrosoft',
            MicrosoftCAAttributes.host: hostname,
            MicrosoftCAAttributes.given_name: service_name,
            MicrosoftCAAttributes.credential: self._get_dn(credential),
            MicrosoftCAAttributes.template: template,
            MicrosoftCAAttributes.description: description,
            MicrosoftCAAttributes.contact: [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            MicrosoftCAAttributes.manual_approval: {True: "1", False: "0"}.get(manual_approvals),
            MicrosoftCAAttributes.san_enabled: {True: "1", False: "1"}.get(subject_alt_name_enabled),
            MicrosoftCAAttributes.include_cn_as_san: {True: "1", False: "0"}.get(automatically_include_cn_as_dns_san),
            MicrosoftCAAttributes.specific_end_date_enabled: {True: "1", False: "0"}.get(allow_users_to_specify_end_date),
            MicrosoftCAAttributes.enrollment_agent_certificate: self._get_dn(enrollment_agent) if enrollment_agent else None
        })

        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=MicrosoftCAAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class SelfSignedCA(_CertificateAuthorityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Identity.Identity, str]' = None, key_usage: 'List[str]' = None, server_authentication: 'bool' = None,
               client_authentication: 'bool' = None, code_signing: 'bool' = None, signature_algorithm: 'str' = None,
               valid_years: 'int' = None, valid_days: 'int' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Creates a Self-Signed Certificate Authority object.

        Args:
            name: Name of the CA object.
            parent_folder: ``Config.Object`` or DN of the parent folder of this Certificate Authority object.
            description: Description of the CA object.
            contacts: List of ``Identity.Identity`` or prefixed universal GUIDs of the contacts.
            key_usage: List of key usages.
            server_authentication: Allow server authentication.
            client_authentication: Allow client authentication.
            code_signing: Allow code signing.
            signature_algorithm: Signing algorithm.
            valid_years: Validity period in years.
            valid_days: Validitiy period in days. Added to years.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            ``Config.Object``
        """
        attributes = attributes or {}
        attributes.update({
            SelfSignedCAAttributes.driver_name: 'caselfsigned',
            SelfSignedCAAttributes.description: description,
            SelfSignedCAAttributes.contact: [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            SelfSignedCAAttributes.key_usage: ','.join(key_usage),
            SelfSignedCAAttributes.algorithm: signature_algorithm,
        })
        if server_authentication or client_authentication or code_signing:
            enhanced_key_usage = {
                '1.3.6.1.5.5.7.3.1': server_authentication,
                '1.3.6.1.5.5.7.3.2': client_authentication,
                '1.3.6.1.5.5.7.3.3': code_signing
            }
            attributes.update({
                SelfSignedCAAttributes.enhanced_key_usage: [
                    eku for eku, enabled in enhanced_key_usage.items() if enabled is True
                ],
            })
        if valid_years or valid_days:
            validity_period= (365 * (valid_years or 0)) + (valid_days or 0)
            attributes.update({
                SelfSignedCAAttributes.validity_period: validity_period
            })
        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=SelfSignedCAAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )
