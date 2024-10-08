from __future__ import annotations

import base64
import hashlib
from typing import (
    TYPE_CHECKING,
    Union,
)

from pyvenafi.tpp.api.websdk.enums.secret_store import (
    KeyNames,
    Namespaces,
    VaultTypes,
)
from pyvenafi.tpp.attributes.adaptable_ca import AdaptableCAAttributes
from pyvenafi.tpp.attributes.microsoft_ca import MicrosoftCAAttributes
from pyvenafi.tpp.attributes.self_signed_ca import SelfSignedCAAttributes
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

if TYPE_CHECKING:
    from pyvenafi.tpp.api.websdk.models import (
        config,
        identity as ident,
    )

class _CertificateAuthorityBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, certificate_authority: 'Union[config.Object, str]'):
        """
        Deletes the certificate authority object from TPP, including all of the secrets associated to it.

        Args:
            certificate_authority: :ref:`config_object` or :ref:`dn` for the certificate authority object.
        """
        certificate_authority_dn = self._get_dn(certificate_authority)
        self._secret_store_delete(object_dn=certificate_authority_dn)
        self._config_delete(object_dn=certificate_authority_dn)

    def get(self, certificate_authority_dn: str, raise_error_if_not_exists: bool = True):
        """
        Get the certificate authority object in TPP.

        Args:
            certificate_authority_dn: :ref:`dn` of the certificate authority.
            raise_error_if_not_exists: Raise an exception if the object :ref:`dn` does not exist.

        Returns:
            :ref:`config_object` of the certificate authority.
        """
        return self._get_config_object(
            object_dn=certificate_authority_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

@feature('Microsoft CA')
class MSCA(_CertificateAuthorityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(
        self, name: str, parent_folder: 'Union[config.Object, str]', hostname: str, service_name: str,
        credential: 'Union[config.Object, str]', template: str, description: 'str' = None,
        contacts: 'list[ident.Identity, str]' = None, manual_approvals: 'bool' = None,
        subject_alt_name_enabled: 'bool' = None, automatically_include_cn_as_dns_san: 'bool' = None,
        allow_users_to_specify_end_date: 'bool' = None, enrollment_agent: 'Union[config.Object, str]' = None,
        attributes: dict = None, get_if_already_exists: bool = True
    ):
        """
        Args:
            name: Name of the CA object.
            parent_folder: `:ref:`config_object` or :ref:`dn` of the parent folder of this certificate authority object.
            hostname: Hostname or IP Address of the CA.
            service_name: Service, or Given, Name of the certificate authority.
            credential: `:ref:`config_object` or :ref:`dn` of the CA credential.
            template: Name of the CA template.
            description: Description of the CA object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            manual_approvals: Require manual approvals.
            subject_alt_name_enabled: Enable Subject Alternative Names.
            automatically_include_cn_as_dns_san: Automatically include the common name (CN) as a DNS SAN.
            allow_users_to_specify_end_date: Allow users to specify the end date.
            enrollment_agent: `:ref:`config_object` or :ref:`dn` of the certificate credential, or enrollment agent.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the certificate authority.
        """
        bool_to_string = lambda x: {
            True : "1",
            False: "0"
        }.get(x)
        ca_attrs = {
            MicrosoftCAAttributes.driver_name                 : 'camicrosoft',
            MicrosoftCAAttributes.host                        : hostname,
            MicrosoftCAAttributes.given_name                  : service_name,
            MicrosoftCAAttributes.credential                  : self._get_dn(credential),
            MicrosoftCAAttributes.template                    : template,
            MicrosoftCAAttributes.description                 : description,
            MicrosoftCAAttributes.contact                     : [self._get_prefixed_universal(c) for c in
                                                                 contacts] if contacts else None,
            MicrosoftCAAttributes.manual_approval             : bool_to_string(manual_approvals),
            MicrosoftCAAttributes.san_enabled                 : bool_to_string(subject_alt_name_enabled),
            MicrosoftCAAttributes.include_cn_as_san           : bool_to_string(automatically_include_cn_as_dns_san),
            MicrosoftCAAttributes.specific_end_date_enabled   : bool_to_string(allow_users_to_specify_end_date),
            MicrosoftCAAttributes.enrollment_agent_certificate: self._get_dn(
                enrollment_agent
            ) if enrollment_agent else None
        }
        if attributes:
            ca_attrs.update(attributes)

        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=MicrosoftCAAttributes.__config_class__,
            attributes=ca_attrs,
            get_if_already_exists=get_if_already_exists
        )

@feature('Self-Signed CA')
class SelfSignedCA(_CertificateAuthorityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(
        self, name: str, parent_folder: 'Union[config.Object, str]', description: 'str' = None,
        contacts: 'list[ident.Identity, str]' = None, key_usage: 'list[str]' = None,
        server_authentication: 'bool' = None, client_authentication: 'bool' = None, code_signing: 'bool' = None,
        time_stamping: 'bool' = None, signature_algorithm: 'str' = None, valid_years: 'int' = None,
        valid_days: 'int' = None, attributes: dict = None, get_if_already_exists: bool = True
    ):
        """
        Args:
            name: Name of the CA object.
            parent_folder: `:ref:`config_object` or :ref:`dn` of the parent folder of this certificate authority object.
            description: Description of the CA object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            key_usage: List of key usages.
            server_authentication: Allow server authentication.
            client_authentication: Allow client authentication.
            code_signing: Allow code signing.
            time_stamping: Allow time stamping.
            signature_algorithm: Signing algorithm.
            valid_years: Validity period in years.
            valid_days: Validity period in days. Added to years.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the certificate authority.
        """
        ca_attrs = {
            SelfSignedCAAttributes.driver_name: 'caselfsigned',
            SelfSignedCAAttributes.description: description,
            SelfSignedCAAttributes.contact    : [self._get_prefixed_universal(c) for c in
                                                 contacts] if contacts else None,
            SelfSignedCAAttributes.key_usage  : ','.join(key_usage),
            SelfSignedCAAttributes.algorithm  : signature_algorithm,
        }
        if server_authentication or client_authentication or code_signing or time_stamping:
            enhanced_key_usage = {
                '1.3.6.1.5.5.7.3.1': server_authentication,
                '1.3.6.1.5.5.7.3.2': client_authentication,
                '1.3.6.1.5.5.7.3.3': code_signing,
                '1.3.6.1.5.5.7.3.8': time_stamping
            }
            ca_attrs.update(
                {
                    SelfSignedCAAttributes.enhanced_key_usage: [
                        eku for eku, enabled in enhanced_key_usage.items() if enabled is True
                    ],
                }
            )
        if valid_years or valid_days:
            validity_period = (365 * (valid_years or 0)) + (valid_days or 0)
            ca_attrs.update(
                {
                    SelfSignedCAAttributes.validity_period: validity_period
                }
            )
        if attributes:
            ca_attrs.update(attributes)
        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=SelfSignedCAAttributes.__config_class__,
            attributes=ca_attrs,
            get_if_already_exists=get_if_already_exists
        )

@feature('Self-Signed CA')
class AdaptableCA(_CertificateAuthorityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(
        self, name: str, parent_folder: 'Union[config.Object, str]', powershell_script_name: str,
        powershell_script_content: bytes, oauth_application_id: str,
        oauth_token_credential: 'Union[config.Object, str]', description: 'str' = None,
        contacts: 'list[ident.Identity, str]' = None, username_credential: 'Union[config.Object, str]' = None,
        certificate_credential: 'Union[config.Object, str]' = None,
        secondary_credential: 'Union[config.Object, str]' = None, service_address: 'str' = None,
        profile_string: 'str' = None, renewal_window: int = None,
        allow_reissuance: bool = False, subject_alt_name_enabled: bool = False,
        fix_certificate_errors: bool = False, enabled_debug_logging: bool = False,
        oauth_scope: str = None, attributes: dict = None, get_if_already_exists: bool = True
    ):
        """
        Args:
            name: Name of the CA object.
            parent_folder: `:ref:`config_object` or :ref:`dn` of the parent folder of this certificate authority object.
            powershell_script_name: Powershell script name on the TPP server.
            powershell_script_content: Powershell script content on the TPP server.
            oauth_application_id: Application ID of the OAuth application.
            oauth_token_credential: `:ref:`config_object` or :ref:`dn` of the parent folder of this certificate authority object.
            description: Description of the CA object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            username_credential: `:ref:`config_object` or :ref:`dn` of a username credential.
            certificate_credential: `:ref:`config_object` or :ref:`dn` of a certificate credential.
            secondary_credential: `:ref:`config_object` or :ref:`dn` of a secondary credential.
            service_address: Any service address.
            profile_string: Profile string.
            renewal_window: Renewal window of the CA object.
            allow_reissuance: Allow certificate reissuance.
            subject_alt_name_enabled: Enable subject alternate names.
            fix_certificate_errors: Fix certificate errors when the script is updated.
            enabled_debug_logging: Enable debug logging.
            oauth_scope: Scope of the OAuth application.
            attributes: Additional attributes associated to the CA object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the certificate authority.
        """
        bool_to_str = lambda x: "1" if x else None
        ca_attrs = {
            AdaptableCAAttributes.driver_name                     : 'caadaptable',
            AdaptableCAAttributes.description                     : description,
            AdaptableCAAttributes.contact                         : [
                self._get_prefixed_universal(c) for c in
                contacts
            ] if contacts else None,
            AdaptableCAAttributes.credential                      : self._get_dn(username_credential),
            AdaptableCAAttributes.certificate_credential          : self._get_dn(certificate_credential),
            AdaptableCAAttributes.secondary_credential            : self._get_dn(secondary_credential),
            AdaptableCAAttributes.service_address                 : service_address,
            AdaptableCAAttributes.profile_string                  : profile_string,
            AdaptableCAAttributes.renewal_window                  : renewal_window,
            AdaptableCAAttributes.allow_reissue                   : bool_to_str(allow_reissuance),
            AdaptableCAAttributes.san_enabled                     : bool_to_str(subject_alt_name_enabled),
            AdaptableCAAttributes.retry_after_script_hash_mismatch: bool_to_str(fix_certificate_errors),
            AdaptableCAAttributes.log_debug                       : bool_to_str(enabled_debug_logging),
            AdaptableCAAttributes.oauth_token_application_id      : oauth_application_id,
            AdaptableCAAttributes.oauth_token_credential          : self._get_dn(oauth_token_credential),
            AdaptableCAAttributes.oauth_token_scope               : oauth_scope,
        }
        if attributes:
            ca_attrs.update(attributes)
        ca = self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=AdaptableCAAttributes.__config_class__,
            attributes=ca_attrs,
            get_if_already_exists=get_if_already_exists
        )

        self._api.websdk.Config.AddValue.post(
            object_dn=ca.dn,
            attribute_name=AdaptableCAAttributes.interoperability_script,
            value=powershell_script_name
        )

        script_hash = base64.b64encode(
            hashlib.sha256(
                powershell_script_content.decode().encode('utf-32-le')
            ).hexdigest().encode()
        ).decode()

        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=script_hash,
            keyname=KeyNames.software_default,
            vault_type=VaultTypes.blob,
            namespace=Namespaces.config,
            owner=ca.dn,
        ).vault_id

        self._api.websdk.Config.WriteDn.post(
            object_dn=ca.dn,
            attribute_name=AdaptableCAAttributes.powershell_script_hash_vault_id,
            values=[vault_id]
        )

        return ca
