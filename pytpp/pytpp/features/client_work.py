import datetime
import time
from typing import List, Union
from pytpp.vtypes import Config
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.properties.config import ClientWorkAttributeValues, ClientWorkClassNames
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes
from pytpp.attributes.server_agent_base_device_placement_work import \
    ServerAgentBaseDevicePlacementWorkAttributes
from pytpp.attributes.client_agent_automatic_upgrade_work import ClientAgentAutomaticUpgradeWorkAttributes
from pytpp.attributes.client_agent_configuration_work import ClientAgentConfigurationWorkAttributes
from pytpp.attributes.client_agent_device_placement_work import ClientAgentDevicePlacementWorkAttributes
from pytpp.attributes.client_agent_ssh_discovery_work import ClientAgentSSHDiscoveryWorkAttributes
from pytpp.attributes.client_agent_ssh_key_usage_work import ClientAgentSSHKeyUsageWorkAttributes
from pytpp.attributes.client_certificate_discovery_work import ClientCertificateDiscoveryWorkAttributes
from pytpp.attributes.client_user_certificate_work import ClientUserCertificateWorkAttributes
from pytpp.attributes.network_device_certificate_work import NetworkDeviceCertificateWorkAttributes
from pytpp.attributes.server_certificate_work import ServerCertificateWorkAttributes


class _ClientWorkBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api)
        self._work_base_dn = r'\VED\Clients\Work'

    def delete(self, work: Union['Config.Object', str]):
        """
        Deletes a client work

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        response = self._api.websdk.Config.Delete.post(work_dn)

        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(
                code=response.result.code,
                code_description=response.result.credential_result
            )

    def disable(self, work: Union['Config.Object', str]):
        """
        Disables a client work

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        result = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list({
                ClientWorkBaseAttributes.disabled: ["1"]
            }, keep_list_values=True)
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def enable(self, work: Union['Config.Object', str]):
        """
        Enables a client work

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        result = self._api.websdk.Config.ClearAttribute.post(
            object_dn=work_dn,
            attribute_name=ClientWorkBaseAttributes.disabled
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Gets a client work and returns a config object

        Args:
            name: The name of the client work.
            raise_error_if_not_exists: Raise an exception if the client work does not exist.

        Returns:
            Config object representing a client work
        """
        return self._get_config_object(
            object_dn=rf'{self._work_base_dn}\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists,
            valid_class_names=list(ClientWorkClassNames)
        )

    def list(self):
        """
        Gets a list of all client work

        Returns:
            A list of config objects representing all of the client work
        """
        response = self._api.websdk.Config.Enumerate.post(object_dn=self._work_base_dn)

        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(code=response.result.code,
                                                 code_description=response.result.credential_result)
        return response.objects


@feature()
class AgentConnectivity(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 days_of_week: List[str] = None,
                 days_of_month: List[str] = None, randomize_minutes: int = 0):
        """
        Schedules the Agent Connectivity work to run

        .. note::
            Only one of daily, hourly, days_of_week or days_of_month can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            days_of_week: Runs the client work on specific days of the week. It is a Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Runs the client work on specific days of the month.
            randomize_minutes: Randomize the given minutes for agent check-in to the server
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)

        attributes = {
            ClientAgentConfigurationWorkAttributes.start_time: datetime.time(start_time % 24).strftime("%I:00 %p"),
            ClientAgentConfigurationWorkAttributes.interval  : randomize_minutes
        }

        if len([x for x in [daily, hourly, days_of_week, days_of_month] if x not in[None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,days_of_week,days_of_month")

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientAgentConfigurationWorkAttributes.schedule_type] = ClientWorkAttributeValues.AgentConnectivity.ScheduleType.daily
        elif hourly:
            attributes[ClientAgentConfigurationWorkAttributes.schedule_type] = ClientWorkAttributeValues.AgentConnectivity.ScheduleType.hourly
        elif days_of_week:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_week interval")

            attributes[ClientAgentConfigurationWorkAttributes.schedule_type] = ClientWorkAttributeValues.AgentConnectivity.ScheduleType.days_of_week
            attributes[ClientAgentConfigurationWorkAttributes.days_of_week] = days_of_week
        elif days_of_month:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_month interval")

            attributes[ClientAgentConfigurationWorkAttributes.schedule_type] = ClientWorkAttributeValues.AgentConnectivity.ScheduleType.days_of_month
            attributes[ClientAgentConfigurationWorkAttributes.days_of_month] = days_of_month
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply at one of (daily, hourly, days_of_week, days_of_month)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes, True)
        )
        response.assert_valid_response()

    def create(self, name: str, server_url: str = "", proxy_url: str = "", proxy_credentials: str = "",
               log_threshold: str = ClientWorkAttributeValues.AgentConnectivity.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates an Agent Connectivity client work

        Args:
            name: The name of the client work.
            server_url: (optional) specify the server url
            proxy_url: (optional) specify the proxy url
            proxy_credentials: (optional) specify the proxy credentials
            log_threshold: (optional) set the log threshold, defaults to INFO
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """
        attributes = {
            ClientAgentConfigurationWorkAttributes.created_by   : ClientWorkAttributeValues.AgentConnectivity.CreatedBy.websdk,
            ClientAgentConfigurationWorkAttributes.interval     : 0,
            ClientAgentConfigurationWorkAttributes.log_threshold: log_threshold
        }

        if len(server_url) > 0:
            attributes[ClientAgentConfigurationWorkAttributes.web_service_url] = server_url
        if len(proxy_url) > 0:
            attributes[ClientAgentConfigurationWorkAttributes.proxy_host] = proxy_url
        if len(proxy_credentials) > 0:
            attributes[ClientAgentConfigurationWorkAttributes.proxy_credential] = proxy_credentials

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.agent_connectivity,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientAgentConfigurationWorkAttributes.start_time,
            ClientAgentConfigurationWorkAttributes.schedule_type,
            ClientAgentConfigurationWorkAttributes.interval,
            ClientAgentConfigurationWorkAttributes.days_of_week,
            ClientAgentConfigurationWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class AgentUpgrade(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, get_if_already_exists: bool = True, **kwargs):
        """
        Creates an Agent Upgrade client work

        Args:
            name: The name of the client work.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """
        attributes = {
            ClientAgentAutomaticUpgradeWorkAttributes.created_by: ClientWorkAttributeValues.AgentUpgrade.CreatedBy.websdk,
        }

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.agent_connectivity,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class CertificateDevicePlacement(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, placement_folder_dn: str, share_mode: int = 2,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a Certificate Device Placement client work

        Args:
            name: The name of the client work.
            placement_folder_dn: The folder's dn to place devices
            share_mode: (optional) specify how newly discovered devices are de-duplicated
                0: search the entire policy tree
                1: search the devices folder
                2: search the devices folder and any sub-folders
                3: create a duplicate device
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """
        attributes = {
            ClientAgentDevicePlacementWorkAttributes.created_by            : ClientWorkAttributeValues.CertificateDevicePlacement.CreatedBy.websdk,
            ClientAgentDevicePlacementWorkAttributes.device_object_location: placement_folder_dn
        }

        if share_mode == 0:
            attributes[ServerAgentBaseDevicePlacementWorkAttributes.device_share_mode] = \
                ClientWorkAttributeValues.CertificateDevicePlacement.DeviceSharedMode.whole_tree
        elif share_mode == 1:
            attributes[
                ServerAgentBaseDevicePlacementWorkAttributes.device_share_mode] = \
                ClientWorkAttributeValues.CertificateDevicePlacement.DeviceSharedMode.devices_folder
        elif share_mode == 2:
            attributes[ServerAgentBaseDevicePlacementWorkAttributes.device_share_mode] = \
                ClientWorkAttributeValues.CertificateDevicePlacement.DeviceSharedMode.devices_folder_and_sub_folders
        elif share_mode == 3:
            attributes[ServerAgentBaseDevicePlacementWorkAttributes.device_share_mode] = \
                ClientWorkAttributeValues.CertificateDevicePlacement.DeviceSharedMode.duplicate_device
        else:
            raise FeatureError.UnexpectedValue(f"Unexpected value for 'share_mode': {share_mode}")

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.agent_connectivity,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class CertificateDiscovery(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 on_receipt: bool = False,
                 days_of_week: List[str] = None, days_of_month: List[str] = None, randomize_minutes: int = 0,
                 full_scan: bool = False):
        """
        Schedules the Certificate Discovery work to run

        .. note::
			Only one of daily, hourly, on_receipt, days_of_week or days_of_month can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            on_receipt: Runs the client work on_receipt
            days_of_week: Runs the client work on specific days of the week. It is a Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Runs the client work on specific days of the month.
            randomize_minutes: Randomize the given minutes for agent to send data back to the server
            full_scan: Reset the cache and perform a full scan (resend all the data to the server)
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        attributes = {
            ClientCertificateDiscoveryWorkAttributes.start_time: datetime.time(start_time % 24).strftime("%I:00 %p"),
            ClientCertificateDiscoveryWorkAttributes.interval  : randomize_minutes
        }

        if len([x for x in [daily, hourly, on_receipt, days_of_week, days_of_month] if x not in [None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,on_receipt,days_of_week,days_of_month")

        if full_scan:
            attributes[ClientCertificateDiscoveryWorkAttributes.clear_cache_timestamp] = str(time.time())

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateDiscovery.ScheduleType.daily
        elif hourly:
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateDiscovery.ScheduleType.hourly
        elif on_receipt:
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateDiscovery.ScheduleType.on_receipt
        elif days_of_week:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_week interval")

            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateDiscovery.ScheduleType.days_of_week
            attributes[ClientCertificateDiscoveryWorkAttributes.days_of_week] = days_of_week
        elif days_of_month:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_month interval")

            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateDiscovery.ScheduleType.days_of_month
            attributes[ClientCertificateDiscoveryWorkAttributes.days_of_month] = days_of_month
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply at one of (daily, hourly, days_of_week, days_of_month)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes, True)
        )
        response.assert_valid_response()

    def create(self,
               name: str, certificate_location_dn: str, recursive_paths: List[str] = None, non_recursive_paths: List[str] = None,
               max_filesize: str = ClientWorkAttributeValues.CertificateDiscovery.MaxFilesize.less_than_10k,
               pkcs12_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_pkcs12_extensions,
               pkcs7_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_pkcs7_extensions,
               pem_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_pem_extensions,
               ibmcms_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_ibmcms_extensions,
               jks_jceks_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_jks_jceks_extensions,
               iplanet_extensions: List[str] = ClientWorkAttributeValues.CertificateDiscovery.Extensions.default_iplanet_extensions,
               exclude_recursive_paths: List[str] = None, exclude_non_recursive_paths: List[str] = None,
               exclude_file_patterns: List[str] = None, scan_mounted_file_systems: bool = False,
               log_threshold: str = ClientWorkAttributeValues.CertificateDiscovery.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a Certificate Discovery client work

        Args:
            name: The name of the client work.
            certificate_location_dn: The folder's dn to place the certificates
            recursive_paths: (optional) A list of file paths to recursively search for new certificates
            non_recursive_paths: (optional) A lit of file paths to search for new certificates
            max_filesize: (optional) A maximum file size (Ignores files larger than this size)
            pkcs12_extensions: (optional) A list of pkcs#12 extensions to match (defaults to .p12, .pfx)
            pkcs7_extensions: (optional) A list of pkcs#7 extensions to match (defaults to .p7b, .p7c, .p7)
            pem_extensions: (optional) A list of PEM extensions to match (defaults to .cer, .der, .crt, .pem)
            ibmcms_extensions: (optional) A list of IBM CMS extensions to match (defaults to .kdb)
            jks_jceks_extensions: (optional) A list of JKS/JCKES(java) extensions to match (defaults to .jck, .jceks, .jks, cacerts)
            iplanet_extensions: (optional) A list of iPlanet(Berkeley/NSS) extensions to match (defaults to .db)
            exclude_recursive_paths: (optional) A list of file paths to exclude (recursively) from discovery
            exclude_non_recursive_paths: (optional) A list of file paths to exclude from discovery
            exclude_file_patterns: (optional) A list of file patterns to exclude from discovery
            scan_mounted_file_systems: (optional) Scan file systems mounted via NFS/CIFS/NTFS junction points (defaults to False)
            log_threshold: (optional) set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """
        attributes = {
            ClientCertificateDiscoveryWorkAttributes.created_by                 : ClientWorkAttributeValues.CertificateDiscovery.CreatedBy.websdk,
            ClientCertificateDiscoveryWorkAttributes.certificate_location_dn    : certificate_location_dn,
            ClientCertificateDiscoveryWorkAttributes.interval                   : 0,
            ClientCertificateDiscoveryWorkAttributes.log_threshold              : log_threshold,
            ClientCertificateDiscoveryWorkAttributes.exclude_remote_mount_points: int(scan_mounted_file_systems),
            ClientCertificateDiscoveryWorkAttributes.max_filesize               : max_filesize
        }

        paths = []

        for path in (non_recursive_paths or []):
            paths.append(f'1,{path}')
        for path in (recursive_paths or []):
            paths.append(f'2,{path}')
        for path in (exclude_non_recursive_paths or []):
            paths.append(f'3,{path}')
        for path in (exclude_recursive_paths or []):
            paths.append(f'4,{path}')
        for path in (exclude_file_patterns or []):
            paths.append(f'6,{path}')

        if len(paths) > 0:
            attributes[ClientCertificateDiscoveryWorkAttributes.certificate_scanner_path] = paths

        extensions = []

        for ext in (pkcs12_extensions or []):
            extensions.append(f'5,{ext}')
        for ext in (pkcs7_extensions or []):
            extensions.append(f'7,{ext}')
        for ext in (pem_extensions or []):
            extensions.append(f'8,{ext}')
        for ext in (ibmcms_extensions or []):
            extensions.append(f'3,{ext}')
        for ext in (jks_jceks_extensions or []):
            extensions.append(f'4,{ext}')
        for ext in (iplanet_extensions or []):
            extensions.append(f'2,{ext}')

        if len(extensions) > 0:
            attributes[ClientCertificateDiscoveryWorkAttributes.certificate_scanner_map] = extensions

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.certificate_discovery,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )


    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientCertificateDiscoveryWorkAttributes.start_time,
            ClientCertificateDiscoveryWorkAttributes.schedule_type,
            ClientCertificateDiscoveryWorkAttributes.interval,
            ClientCertificateDiscoveryWorkAttributes.days_of_week,
            ClientCertificateDiscoveryWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class CertificateEnrollmentViaESTProtocol(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, certificate_container_dn: str, naming_pattern: str, ca_template_dn: str,
               contacts: List[str], certificate_origin: str = None, certificate_description: str = None,
               validation_type: int = ClientWorkAttributeValues.CertificateEnrollmentViaESTProtocol.ValidationType.basic,
               revocation_status_check: int = ClientWorkAttributeValues.CertificateEnrollmentViaESTProtocol.RevocationStatusCheck.accept_when_unknown,
               authentication_credentials_dn: str = None, authenticate_only_by_password: bool = False,
               revoke_previous_version: bool = False,
               identity_verification: int = ClientWorkAttributeValues.CertificateEnrollmentViaESTProtocol.IdentityVerification.valid,
               trusted_certs_and_cas: List[str] = None, get_if_already_exists: bool = False, **kwargs):
        """
        Creates a Certificate Enrollment Via EST Protocol client work

        Args:
            name: The name of the client work.
            certificate_container_dn: The folder's dn to create certificates
            naming_pattern: The object naming pattern (IE. $CSR.CN$)
            ca_template_dn: The Certificate Authority Template to use
            contacts: List of identity prefixed universal GUIDs. (IE: contacts = [user1.guid, user2.guid]
            certificate_origin: (optional) Specify the certificate origin value
            certificate_description: (optional) Specify the certificate description value
            validation_type: (optional) defaults to basic
                                basic: Checks Expiration, Revocation, and Chain of Trust
                                strict: Performs Basic Validation and checks Client Authentication Enhanced Key Usage
            revocation_status_check: (optional) defaults to accept when unknown
            authentication_credentials_dn: (optional) credential_dn to provide client password authentication
            authenticate_only_by_password: (optional) only accept requests that are authenticated by password
            revoke_previous_version: (optional) Revoke previous versions of the certificate (defaults to False)
            identity_verification: (optional) Proof of Possession
            trusted_certs_and_cas: (optional) A List of Certificate Authorities and Certificates to trust
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """
        attributes = {
            NetworkDeviceCertificateWorkAttributes.created_by                                 : ClientWorkAttributeValues.CertificateEnrollmentViaESTProtocol.CreatedBy.websdk,
            NetworkDeviceCertificateWorkAttributes.certificate_container                      : certificate_container_dn,
            NetworkDeviceCertificateWorkAttributes.naming_pattern                             : naming_pattern,
            NetworkDeviceCertificateWorkAttributes.certificate_authority                      : ca_template_dn,
            NetworkDeviceCertificateWorkAttributes.contact                                    : contacts,
            NetworkDeviceCertificateWorkAttributes.client_certificate_eku_checks_enabled      : validation_type,
            NetworkDeviceCertificateWorkAttributes.revocation_mode                            : revocation_status_check,
            NetworkDeviceCertificateWorkAttributes.fallback_to_http_auth                      : int(authenticate_only_by_password == False),
            NetworkDeviceCertificateWorkAttributes.revoke_existing_certificate_on_reenrollment: int(revoke_previous_version),
            NetworkDeviceCertificateWorkAttributes.pop_mode                                   : identity_verification
        }

        if certificate_origin: attributes[NetworkDeviceCertificateWorkAttributes.origin] = certificate_origin
        if certificate_description: attributes[NetworkDeviceCertificateWorkAttributes.description] = certificate_description
        if authentication_credentials_dn: attributes[NetworkDeviceCertificateWorkAttributes.authentication_credentials] = authentication_credentials_dn

        if trusted_certs_and_cas:
            attributes[NetworkDeviceCertificateWorkAttributes.explicit_trust_anchors] = trusted_certs_and_cas
            attributes[NetworkDeviceCertificateWorkAttributes.use_implicit_trust_anchors] = 0
        else:
            attributes[NetworkDeviceCertificateWorkAttributes.use_implicit_trust_anchors] = 1

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.certificate_enrollment_via_est_protocol,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class CertificateInstallation(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 on_receipt: bool = False,
                 days_of_week: List[str] = None,
                 days_of_month: List[str] = None, every_x_minutes: int = None, randomize_minutes: int = 0):
        """
        Schedules the Certificate Installation work to run

        .. note::
			Only one of daily, hourly, on_receipt, days_of_week, days_of_month or every_x_minutes can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            on_receipt: Runs the client work on receipt
            days_of_week: Runs the client work on specific days of the week. It is a Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Runs the client work on specific days of the month.
            every_x_minutes: Runs the client work every 1,5,15 or 30 minutes. (Must be one of 1, 5, 15 or 30)
            randomize_minutes: Randomize the given minutes for agent to send data back to the server
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        attributes = {
            ClientCertificateDiscoveryWorkAttributes.interval: randomize_minutes
        }

        if len([x for x in [daily, hourly, on_receipt, days_of_week, days_of_month, every_x_minutes] if
                x not in [None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,on_receipt,days_of_week,days_of_month,every_x_minutes")

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientCertificateDiscoveryWorkAttributes.start_time] = datetime.time(
                start_time % 24).strftime(
                "%I:00 %p")
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateInstallation.ScheduleType.daily
        elif hourly:
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateInstallation.ScheduleType.hourly
        elif days_of_week:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_week interval")
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.CertificateInstallation.ScheduleType.days_of_week
            attributes[ClientCertificateDiscoveryWorkAttributes.days_of_week] = days_of_week
        elif days_of_month:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_month interval")
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.days_of_month
            attributes[ClientCertificateDiscoveryWorkAttributes.days_of_month] = days_of_month
        elif on_receipt:
            attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.on_receipt
        elif every_x_minutes:
            if every_x_minutes == 30:
                attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.every_x_minutes
                attributes[ClientCertificateDiscoveryWorkAttributes.start_time] = "12:30:00 AM"
            elif every_x_minutes == 15:
                attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.every_x_minutes
                attributes[ClientCertificateDiscoveryWorkAttributes.start_time] = "12:15:00 AM"
            elif every_x_minutes == 5:
                attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.every_x_minutes
                attributes[ClientCertificateDiscoveryWorkAttributes.start_time] = "12:05:00 AM"
            elif every_x_minutes == 1:
                attributes[ClientCertificateDiscoveryWorkAttributes.schedule_type] = ClientWorkAttributeValues.CertificateInstallation.ScheduleType.every_x_minutes
                attributes[ClientCertificateDiscoveryWorkAttributes.start_time] = "12:01:00 AM"
            else:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply at one of (30, 15, 5, 1) for every_x_minutes")
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply at one of (daily,hourly,on_receipt,days_of_week,days_of_month,every_x_minutes)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes)
        )
        response.assert_valid_response()

    def create(self, name: str, log_threshold: str = ClientWorkAttributeValues.CertificateInstallation.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a Certificate Installation client work

        Args:
            name: The name of the client work.
            log_threshold: (optional) set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientCertificateDiscoveryWorkAttributes.created_by   : ClientWorkAttributeValues.CertificateInstallation.CreatedBy.websdk,
            ClientCertificateDiscoveryWorkAttributes.interval     : 0,
            ClientCertificateDiscoveryWorkAttributes.log_threshold: log_threshold
        }

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.certificate_installation,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientCertificateDiscoveryWorkAttributes.start_time,
            ClientCertificateDiscoveryWorkAttributes.schedule_type,
            ClientCertificateDiscoveryWorkAttributes.interval,
            ClientCertificateDiscoveryWorkAttributes.days_of_week,
            ClientCertificateDiscoveryWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class DeviceCertificateCreation(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, certificate_container_dn: str, ca_template_dn: str, contacts: List[str],
               description: str = None, naming_pattern: str = "$Client.DNSName$",
               common_name: str = "$Client.DNSName$", organization: str = None,
               organizational_unit: List[str] = None, city_locality: str = None, state_province: str = None,
               country: str = None, subject_alternative_names: bool = False, automatic_renewal: bool = True,
               renewal_days_before: int = 30, key_bit_strength: int = 2048, allow_certificate_sharing: bool = False,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a Device Certificate Creation client work

        Args:
            name: The name of the client work
            certificate_container_dn: Folder dn to create certificates in
            ca_template_dn: Certificate Authority dn to use
            contacts: List of identity prefixed universal GUIDs. (IE: contacts = [user1.guid, user2.guid]
            description: (optional) A description for the certificates
            naming_pattern: (optional) object naming pattern (defaults to: $Client.DNSName$)
            common_name: (optional) common name for the certificate
            organization: (optional) organization for the certificate
            organizational_unit: (optional) A list of organizational units for the certificate
            city_locality: (optional) a city or locality for the certificate
            state_province: (optional) a state or province for the certificate
            country: (optional) a country code for the certificate
            subject_alternative_names: (optional) a subject alternative name for the certificate
            automatic_renewal: enable automatic renewal (defaults to True)
            renewal_days_before: days before expiration for automatic renewal (defaults to 30)
            key_bit_strength: key size of the certificates (defaults to 2048)
            allow_certificate_sharing: allow sharing with mobile devices (default sto False)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientUserCertificateWorkAttributes.created_by               : ClientWorkAttributeValues.DeviceCertificateCreation.CreatedBy.websdk,
            ClientUserCertificateWorkAttributes.certificate_container    : certificate_container_dn,
            ClientUserCertificateWorkAttributes.certificate_authority    : ca_template_dn,
            ClientUserCertificateWorkAttributes.naming_pattern           : naming_pattern,
            ClientUserCertificateWorkAttributes.contact                  : contacts,
            ClientUserCertificateWorkAttributes.key_bit_strength         : key_bit_strength,
            ClientUserCertificateWorkAttributes.x509_subject             : common_name,
            ClientUserCertificateWorkAttributes.disable_automatic_renewal: not automatic_renewal,
            ClientUserCertificateWorkAttributes.transfer_allowed         : allow_certificate_sharing
        }

        attributes.update(kwargs)

        if description: attributes[ClientUserCertificateWorkAttributes.description] = description
        if organization: attributes[ClientUserCertificateWorkAttributes.organization] = organization
        if city_locality: attributes[ClientUserCertificateWorkAttributes.city] = city_locality
        if state_province: attributes[ClientUserCertificateWorkAttributes.state] = state_province
        if organizational_unit: attributes[ClientUserCertificateWorkAttributes.organizational_unit] = organizational_unit
        if country: attributes[ClientUserCertificateWorkAttributes.country] = country
        if subject_alternative_names: attributes[ClientUserCertificateWorkAttributes.x509_subjectaltname_dns] = common_name
        if automatic_renewal: attributes[ClientUserCertificateWorkAttributes.renewal_window] = renewal_days_before

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.device_certificate_creation,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class DynamicProvisioning(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, certificate_container_dn: str, ca_template_dn: str, contacts: List[str],
               description: str = None, naming_pattern: str = "$Client.DNSName$", common_name: str = "$Client.DNSName$",
               organization: str = None, organizational_unit: List[str] = None, city_locality: str = None,
               state_province: str = None, country: str = None, subject_alternative_names: str = "$Client.DNSname$",
               capi_keystore: bool = False, capi_friendly_name: str = "", capi_trustee: str = "",
               key_bit_strength: int = 2048, retry_interval: int = 15,
               log_threshold: str = ClientWorkAttributeValues.DynamicProvisioning.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a Dynamic Provisioning client work

        Args:
            name: The name of the client work
            certificate_container_dn: Folder dn to create certificates in
            ca_template_dn: Certificate Authority dn to use
            contacts: List of identity prefixed universal GUIDs. (IE: contacts = [user1.guid, user2.guid]
            description: (optional) A description for the certificates
            naming_pattern: (optional) object naming pattern (defaults to: $Client.DNSName$)
            common_name: (optional) common name for the certificate
            organization: (optional) organization for the certificate
            organizational_unit: (optional) A list of organizational units for the certificate
            city_locality: (optional) a city or locality for the certificate
            state_province: (optional) a state or province for the certificate
            country: (optional) a country code for the certificate
            subject_alternative_names: (optional) a subject alternative name for the certificate
            capi_keystore: (optional) use a capi keystore (defaults to False)
            capi_friendly_name: (optional) friendly name in the keystore
            capi_trustee: (optional) Set the capi trustee
            key_bit_strength: (optional) key size for the certificate (defaults to 2048)
            retry_interval: (optional) An interval in minutes (15, 30, 45, 60) for the agent to retry
            log_threshold: (optional) Set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ServerCertificateWorkAttributes.created_by             : ClientWorkAttributeValues.DynamicProvisioning.CreatedBy.websdk,
            ServerCertificateWorkAttributes.certificate_container  : certificate_container_dn,
            ServerCertificateWorkAttributes.certificate_authority  : ca_template_dn,
            ServerCertificateWorkAttributes.naming_pattern         : naming_pattern,
            ServerCertificateWorkAttributes.contact                : contacts,
            ServerCertificateWorkAttributes.key_bit_strength       : key_bit_strength,
            ServerCertificateWorkAttributes.x509_subject           : common_name,
            ServerCertificateWorkAttributes.x509_subjectaltname_dns: subject_alternative_names,
            ServerCertificateWorkAttributes.interval               : retry_interval,
            ServerCertificateWorkAttributes.log_threshold          : log_threshold
        }

        if description: attributes[ServerCertificateWorkAttributes.description] = description
        if organization: attributes[ServerCertificateWorkAttributes.organization] = organization
        if city_locality: attributes[ServerCertificateWorkAttributes.city] = city_locality
        if state_province: attributes[ServerCertificateWorkAttributes.state] = state_province
        if organizational_unit: attributes[ServerCertificateWorkAttributes.organizational_unit] = organizational_unit
        if country: attributes[ServerCertificateWorkAttributes.country] = country
        if capi_keystore:
            attributes[ServerCertificateWorkAttributes.application_type] = ClientWorkAttributeValues.DynamicProvisioning.ApplicationType.capi
            attributes[ServerCertificateWorkAttributes.friendly_name] = capi_friendly_name
            attributes[ServerCertificateWorkAttributes.private_key_trustee] = capi_trustee

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.dynamic_provisioning,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class SSHDevicePlacement(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, devices_folder_dn: str,
               share_mode: str = ClientWorkAttributeValues.SSHDevicePlacement.DeviceSharedMode.devices_folder_and_sub_folders,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a SSH Device Placement client work

        Args:
            name: The name of the client work
            devices_folder_dn: the folder's dn to place newly discovered ssh devices
            share_mode: how to de-duplicate newly discovered devices:
                    "WholeTree" : search the entire policy tree
                    "SpecifiedFolderOnly" : search the devices folder
                    "SpecifiedFolderAndSubFolders" : search the devices folder and all sub-folders
                    "None" : create a duplicate device
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ServerAgentBaseDevicePlacementWorkAttributes.created_by            : ClientWorkAttributeValues.AgentConnectivity.CreatedBy.websdk,
            ServerAgentBaseDevicePlacementWorkAttributes.device_object_location: devices_folder_dn,
            ServerAgentBaseDevicePlacementWorkAttributes.device_share_mode     : share_mode
        }

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.ssh_device_placement,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class SSHDiscovery(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 on_receipt: bool = False, every_30_minutes: bool = False,
                 days_of_week: List[str] = None,
                 days_of_month: List[str] = None, randomize_minutes: int = 0, full_scan: bool = False):
        """
        Schedules the SSH Discovery work to run

        .. note::
			Only one of daily, hourly, on_receipt, every_30_minutes, days_of_week or days_of_month can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            on_receipt: Runs the client work on_receipt
            every_30_minutes: Runs the client work every 30 minutes
            days_of_week: Runs the client work on specific days of the week. It is a Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Runs the client work on specific days of the month.
            randomize_minutes: Randomize the given minutes for agent to send data back to the server
            full_scan: Reset the cache and perform a full scan (resend all the data to the server)
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        attributes = {
            ClientAgentSSHDiscoveryWorkAttributes.interval: randomize_minutes
        }

        if len([x for x in [daily, hourly, on_receipt, every_30_minutes, days_of_week, days_of_month] if x not in [None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,on_receipt,every_30_minutes,days_of_week,days_of_month")

        if full_scan:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.clear_cache_timestamp] = str(time.time())

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = \
                datetime.time(start_time % 24).strftime("%I:00 %p")
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.daily
        elif hourly:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.hourly
        elif on_receipt:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.on_receipt
        elif every_30_minutes:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.every_30_minutes
            attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = "12:30:00 AM"
        elif days_of_week:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_week interval")

            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.days_of_week
            attributes[ClientAgentSSHDiscoveryWorkAttributes.days_of_week] = days_of_week
        elif days_of_month:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_month interval")

            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHDiscovery.ScheduleType.days_of_month
            attributes[ClientAgentSSHDiscoveryWorkAttributes.days_of_month] = days_of_month
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply one of (daily,hourly,on_receipt,every_30_minutes,days_of_week,days_of_month)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes, True)
        )
        response.assert_valid_response()

    def create(self, name: str, scan_default_paths: bool = True, host_key_paths: List[str] = None,
               user_key_paths: List[str] = None,
               user_or_host_paths: List[str] = None, exclude_paths: List[str] = None, scan_mounted_fs: bool = False,
               minimize_resources: bool = False,
               max_filesize: int = ClientWorkAttributeValues.SSHDiscovery.MaxFilesize.less_than_1MB,
               log_threshold: str = ClientWorkAttributeValues.SSHDiscovery.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a SSH Discovery client work

        Args:
            name: The name of the client work
            scan_default_paths: (optional) scan all of the default paths for ssh keys
            host_key_paths: (optional) A list of paths to scan for host keys
            user_key_paths: (optional) A list of paths to scan for user keys
            user_or_host_paths: (optional) A list of paths to scan for both host and user keys
            exclude_paths: (optional) A list of paths to exclude from scan
            scan_mounted_fs: (optional) Scan file systems mounted via NFS/CIFS/NTFS junction points (defaults to False)
            minimize_resources: (optional) Minimizes resource usage during scan (defaults to False)
            max_filesize: (optional) Ignore files larger than this size (defaults to 1MB)
            log_threshold: (optional) Set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientAgentSSHDiscoveryWorkAttributes.created_by                   : ClientWorkAttributeValues.SSHDiscovery.CreatedBy.websdk,
            ClientAgentSSHDiscoveryWorkAttributes.interval                     : 0,
            ClientAgentSSHDiscoveryWorkAttributes.server_path_defaults_disabled: int(not scan_default_paths),
            ClientAgentSSHDiscoveryWorkAttributes.user_path_defaults_disabled  : int(not scan_default_paths),
            ClientAgentSSHDiscoveryWorkAttributes.exclude_remote_mount_points  : int(not scan_mounted_fs),
            ClientAgentSSHDiscoveryWorkAttributes.minimize_resource_use        : int(minimize_resources),
            ClientAgentSSHDiscoveryWorkAttributes.max_filesize                 : max_filesize,
            ClientAgentSSHDiscoveryWorkAttributes.log_threshold                : log_threshold
        }

        scanner_paths = []
        user_paths = []

        for path in (host_key_paths or []):
            scanner_paths.append(f'2,{path}')
        for path in (user_key_paths or []):
            user_paths.append(f'2,{path}')
        for path in (user_or_host_paths or []):
            scanner_paths.append(f'2,{path}')
            user_paths.append(f'2,{path}')
        for path in (exclude_paths or []):
            scanner_paths.append(f'4,{path}')
            user_paths.append(f'4,{path}')

        if len(scanner_paths) > 0: attributes[ClientAgentSSHDiscoveryWorkAttributes.ssh_scanner_service_path]: scanner_paths
        if len(user_paths) > 0: attributes[ClientAgentSSHDiscoveryWorkAttributes.ssh_scanner_user_path]: user_paths

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.ssh_discovery,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )

    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientAgentSSHDiscoveryWorkAttributes.start_time,
            ClientAgentSSHDiscoveryWorkAttributes.schedule_type,
            ClientAgentSSHDiscoveryWorkAttributes.interval,
            ClientAgentSSHDiscoveryWorkAttributes.days_of_week,
            ClientAgentSSHDiscoveryWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class SSHKeyUsage(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 on_receipt: bool = False, every_x_minutes: int = None, randomize_minutes: int = 0):
        """
        Schedules the SSH KeyUsage work to run

        .. note::
			Only one of daily, hourly, on_receipt, or every_x_minutes can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            on_receipt: Runs the client work on_receipt
            every_x_minutes: Runs the client work every: 1, 5, 15 or 30 minutes
            randomize_minutes: Randomize the given minutes for agent to send data back to the server
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        attributes = {
            ClientAgentSSHKeyUsageWorkAttributes.interval: randomize_minutes
        }

        if len([x for x in [daily, hourly, on_receipt, every_x_minutes] if x not in [None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,on_receipt, every_x_minutes")

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientAgentSSHKeyUsageWorkAttributes.start_time] =\
                datetime.time(start_time % 24).strftime("%I:00 %p")
            attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.daily
        elif hourly:
            attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.hourly
        elif on_receipt:
            attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.on_receipt
        elif every_x_minutes:
            if every_x_minutes == 30:
                attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHKeyUsageWorkAttributes.start_time] = "12:30:00 AM"
            elif every_x_minutes == 15:
                attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHKeyUsageWorkAttributes.start_time] = "12:15:00 AM"
            elif every_x_minutes == 5:
                attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHKeyUsageWorkAttributes.start_time] = "12:05:00 AM"
            elif every_x_minutes == 1:
                attributes[ClientAgentSSHKeyUsageWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHKeyUsage.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHKeyUsageWorkAttributes.start_time] = "12:01:00 AM"
            else:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply at one of (30, 15, 5, 1) for every_x_minutes")
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply one of (daily, hourly, on_receipt, every_x_minutes)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes)
        )
        response.assert_valid_response()

    def create(self, name: str, limit_cache_size: int = 50000,
               log_threshold: str = ClientWorkAttributeValues.SSHKeyUsage.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a SSH Key Usage Creation client work

        Args:
            name: The name of the client work.
            limit_cache_size: maximum items in the cache
            log_threshold: (optional) Set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientAgentSSHKeyUsageWorkAttributes.created_by   : ClientWorkAttributeValues.SSHKeyUsage.CreatedBy.websdk,
            ClientAgentSSHKeyUsageWorkAttributes.interval     : 0,
            ClientAgentSSHKeyUsageWorkAttributes.log_threshold: log_threshold,
            ClientAgentSSHKeyUsageWorkAttributes.max_row_count: limit_cache_size
        }

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.ssh_key_usage,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientAgentSSHKeyUsageWorkAttributes.start_time,
            ClientAgentSSHKeyUsageWorkAttributes.schedule_type,
            ClientAgentSSHKeyUsageWorkAttributes.interval,
            ClientAgentSSHKeyUsageWorkAttributes.days_of_week,
            ClientAgentSSHKeyUsageWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class SSHRemediation(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def schedule(self, work: Union['Config.Object', str], start_time: int = None, daily: bool = False, hourly: bool = False,
                 on_receipt: bool = False,
                 days_of_week: List[str] = None,
                 days_of_month: List[str] = None, every_x_minutes: int = None, randomize_minutes: int = 0):
        """
        Schedules the SSH Remediation work to run

        .. note::
			Only one of daily, hourly, on_receipt, days_of_week, days_of_month or every_x_minutes can be set.

        Args:
            work: The Config.Object or name of the client work
            start_time: The 24-hour UTC hour format (i.e. 20 = 8PM UTC) for the job to start.
            daily: Runs the client work daily
            hourly: Runs the client work hourly
            on_receipt: Runs the client work on_receipt
            days_of_week: Runs the client work on specific days of the week. It is a Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Runs the client work on specific days of the month.
            every_x_minutes: Runs the client work every: 1, 5, 15 or 30 minutes
            randomize_minutes: Randomize the given minutes for agent to send data back to the server
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        attributes = {
            ClientAgentSSHDiscoveryWorkAttributes.interval: randomize_minutes
        }

        if len([x for x in [daily, hourly, on_receipt, days_of_week, days_of_month, every_x_minutes] if x not in [None, False]]) != 1:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must specify one (and only one) of: daily,hourly,on_receipt,days_of_week,days_of_month,every_x_minutes")

        if daily:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the daily interval")

            attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = \
                datetime.time(start_time % 24).strftime("%I:00 %p")
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHRemediation.ScheduleType.daily
        elif hourly:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHRemediation.ScheduleType.hourly
        elif days_of_week:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_week interval")
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHRemediation.ScheduleType.days_of_week
            attributes[ClientAgentSSHDiscoveryWorkAttributes.days_of_week] = days_of_week
        elif days_of_month:
            if not start_time:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply a 'start_time' to use the days_of_month interval")
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHRemediation.ScheduleType.days_of_month
            attributes[ClientAgentSSHDiscoveryWorkAttributes.days_of_month] = days_of_month
        elif on_receipt:
            attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                ClientWorkAttributeValues.SSHRemediation.ScheduleType.on_receipt
        elif every_x_minutes:
            if every_x_minutes == 30:
                attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHRemediation.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = "12:30:00 AM"
            elif every_x_minutes == 15:
                attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHRemediation.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = "12:15:00 AM"
            elif every_x_minutes == 5:
                attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHRemediation.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = "12:05:00 AM"
            elif every_x_minutes == 1:
                attributes[ClientAgentSSHDiscoveryWorkAttributes.schedule_type] = \
                    ClientWorkAttributeValues.SSHRemediation.ScheduleType.every_x_minutes
                attributes[ClientAgentSSHDiscoveryWorkAttributes.start_time] = "12:01:00 AM"
            else:
                raise FeatureError.InvalidFormat(
                    "Error in Schedule: must supply at one of (30, 15, 5, 1) for every_x_minutes")
        else:
            raise FeatureError.InvalidFormat(
                "Error in Schedule: must supply one of (daily,hourly,on_receipt,days_of_week,days_of_month,every_x_minutes)")

        response = self._api.websdk.Config.Write.post(
            object_dn=work_dn,
            attribute_data=self._name_value_list(attributes, True)
        )
        response.assert_valid_response()

    def create(self, name: str, log_threshold: str = ClientWorkAttributeValues.SSHRemediation.LogThreshold.info,
               get_if_already_exists: bool = True, **kwargs):
        """
        Creates a SSH Remediation client work

        Args:
            name: The name of the client work.
            log_threshold: (optional) Set the logging level (defaults to INFO)
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientAgentSSHDiscoveryWorkAttributes.created_by   : ClientWorkAttributeValues.SSHRemediation.CreatedBy.websdk,
            ClientAgentSSHDiscoveryWorkAttributes.interval     : 0,
            ClientAgentSSHDiscoveryWorkAttributes.log_threshold: log_threshold
        }

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.ssh_remediation,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def unschedule(self, work: Union['Config.Object', str]):
        """
        Removes any scheduling for the client work (does not delete the client work)

        Args:
            work: The Config.Object or name of the client work
        """
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        for attribute_name in {
            ClientAgentSSHDiscoveryWorkAttributes.start_time,
            ClientAgentSSHDiscoveryWorkAttributes.schedule_type,
            ClientAgentSSHDiscoveryWorkAttributes.interval,
            ClientAgentSSHDiscoveryWorkAttributes.days_of_week,
            ClientAgentSSHDiscoveryWorkAttributes.days_of_month
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=work_dn,
                attribute_name=attribute_name
            ).assert_valid_response()


@feature()
class UserCertificateCreation(_ClientWorkBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, certificate_container_dn: str, ca_template_dn: str, contacts: List[str],
               description: str = None,
               naming_pattern: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.naming_pattern,
               common_name: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.common_name,
               organization: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.organization,
               organizational_unit: List[
                   str] = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.organizational_unit,
               city_locality: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.city_locality,
               state_province: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.state_province,
               country: str = ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.country,
               user_email: bool = False, subject_alt_names_email: bool = False, subject_alt_names_upn: bool = False,
               key_bit_strength: int = 2048, automatic_renewal: bool = True, renewal_days_before: int = 30,
               configure_outlook: bool = False, outlook_security_name: str = "", outlook_encrypt_messages: bool = False,
               outlook_send_cleartext_signed: bool = False, outlook_sign_outgoing: bool = False,
               outlook_request_receipts: bool = False,
               publish_to_identity_provider: bool = False, publish_pre_enrollment: bool = False,
               install_previous_certs: bool = False, allow_mobile_sharing: bool = False,
               lifecycle_groups: List[str] = None, lifecycle_revoke_cert: bool = False,
               lifecycle_disable_cert: bool = False,
               portal_friendly_name: str = None, portal_icon: int = 0, portal_download_limit: int = 3,
               portal_instructions: str = None, get_if_already_exists: bool = True, **kwargs):
        """
        Creates a User Certificate Creation client work

        Args:
            name: The name of the client work.
            certificate_container_dn: folder dn to create certificates in
            ca_template_dn: Certificate Authority dn to use
            contacts: List of identity prefixed universal GUIDs. (IE: contacts = [user1.guid, user2.guid])
            description: (optional) a description for the certificates
            naming_pattern: (optional) object naming pattern
            common_name: (optional) common name for the certificate
            organization: (optional) organization for the certificate
            organizational_unit: (optional) A list of organizational units for the certificate
            city_locality: (optional) a city or locality for the certificate
            state_province: (optional) a state or province for the certificate
            country: optional) a country code for the certificate
            user_email: add user's email to the certificate
            subject_alt_names_email: (optional) use subject alternative name email for the certificate
            subject_alt_names_upn: (optional) use subject alternative upn for the certificate
            key_bit_strength: (optional) the key size of the certificate
            automatic_renewal: (optional) enable automatic renewal for the certificate
            renewal_days_before: (optional) the number of days before expiration to renew the certificate
            configure_outlook: (optional) configure Microsoft Outlook for Windows
            outlook_security_name: (optional) security settings name
            outlook_encrypt_messages: (optional) encrypt outgoing messages
            outlook_send_cleartext_signed: (optional) send cleartext signed messages
            outlook_sign_outgoing: (optional) sign outgoing messages
            outlook_request_receipts: (optional) request S/MIME receipts
            publish_to_identity_provider: (optional) publish to identity provider
            publish_pre_enrollment: (optional) publish when a new identity is found (pre-enrollment)
            install_previous_certs: (optional) install previous certificate versions
            allow_mobile_sharing: (optional) allow certificate sharing with mobile devices
            lifecycle_groups: (optional) a list of groups guids [group1.guid, group2.guid] such that when a member is removed from all groups in the list the certificate can be revoked and/or disabled
            lifecycle_revoke_cert: (optional) revoke certificates when a user's membership is removed from all lifecycle groups
            lifecycle_disable_cert: (optional) disable certificates when a user's membership is removed from all lifecycle groups
            portal_friendly_name: (optional) portal friendly name
            portal_icon: (optional) portal icon:
                                    0 - certificate
                                    1 - Envelope
                                    2 - Wi-Fi
                                    3 - VPN
            portal_download_limit: (optional) limit the number of portal downloads
            portal_instructions: (optional) text of portal download instructions
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            A config object representing the client work
        """

        attributes = {
            ClientUserCertificateWorkAttributes.created_by                       : ClientWorkAttributeValues.UserCertificateCreation.CreatedBy.websdk,
            ClientUserCertificateWorkAttributes.certificate_container            : certificate_container_dn,
            ClientUserCertificateWorkAttributes.certificate_authority            : ca_template_dn,
            ClientUserCertificateWorkAttributes.naming_pattern                   : naming_pattern,
            ClientUserCertificateWorkAttributes.contact                          : contacts,
            ClientUserCertificateWorkAttributes.key_bit_strength                 : key_bit_strength,
            ClientUserCertificateWorkAttributes.x509_subject                     : common_name,
            ClientUserCertificateWorkAttributes.organization                     : organization,
            ClientUserCertificateWorkAttributes.organizational_unit              : organizational_unit,
            ClientUserCertificateWorkAttributes.city                             : city_locality,
            ClientUserCertificateWorkAttributes.state                            : state_province,
            ClientUserCertificateWorkAttributes.country                          : country,
            ClientUserCertificateWorkAttributes.disable_automatic_renewal        : int(not automatic_renewal),
            ClientUserCertificateWorkAttributes.publish_to_identity              : int(publish_to_identity_provider),
            ClientUserCertificateWorkAttributes.publish_to_identity_on_pre_enroll: int(publish_pre_enrollment),
            ClientUserCertificateWorkAttributes.transfer_allowed                 : allow_mobile_sharing,
            ClientUserCertificateWorkAttributes.include_historic_certificates    : install_previous_certs,
            ClientUserCertificateWorkAttributes.certificate_icon                 : portal_icon,
            ClientUserCertificateWorkAttributes.download_limit                   : portal_download_limit,
        }

        if description: attributes[ClientUserCertificateWorkAttributes.description] = description
        if user_email:
            attributes[ClientUserCertificateWorkAttributes.x509_e] = \
                ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.user_email
        if subject_alt_names_email:
            attributes[ClientUserCertificateWorkAttributes.x509_subjectaltname_rfc822] = \
                ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.subject_alt_names_email
        if subject_alt_names_upn:
            attributes[ClientUserCertificateWorkAttributes.x509_subjectaltname_othername_upn] = \
                ClientWorkAttributeValues.UserCertificateCreation.DefaultValues.subject_alt_names_upn
        if automatic_renewal: attributes[ClientUserCertificateWorkAttributes.renewal_window] = renewal_days_before

        if configure_outlook:
            attributes[ClientUserCertificateWorkAttributes.outlook_profile_generation] = int(configure_outlook)
            attributes[ClientUserCertificateWorkAttributes.outlook_profile_name] = outlook_security_name
            option_value = 0
            if outlook_encrypt_messages: option_value += 1
            if outlook_sign_outgoing: option_value += 2
            if not outlook_send_cleartext_signed: option_value += 32
            if outlook_request_receipts: option_value += 512
            attributes[ClientUserCertificateWorkAttributes.outlook_profile_options] = option_value

        if lifecycle_groups:
            attributes[ClientUserCertificateWorkAttributes.required_member_identity] = lifecycle_groups
            attributes[ClientUserCertificateWorkAttributes.membership_loss_disable] = lifecycle_disable_cert
            attributes[ClientUserCertificateWorkAttributes.membership_loss_revoke] = lifecycle_revoke_cert

        if portal_friendly_name:
            attributes[ClientUserCertificateWorkAttributes.portal_friendly_name] = portal_friendly_name
        if portal_instructions:
            attributes[ClientUserCertificateWorkAttributes.download_instructions] = portal_instructions

        attributes.update(kwargs)

        return self._config_create(
            name=name,
            parent_folder_dn=self._work_base_dn,
            config_class=ClientWorkClassNames.user_certificate_creation,
            attributes=attributes,
            keep_list_values=True,
            get_if_already_exists=get_if_already_exists
        )
