from __future__ import annotations

from typing import (
    List,
    Literal,
    TYPE_CHECKING,
    Union,
)

from pyvenafi.tpp.api.api_base import InvalidResponseError
from pyvenafi.tpp.attributes.discovery import DiscoveryAttributes
from pyvenafi.tpp.attributes.onboard_discovery import OnboardDiscoveryAttributes
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)
from pyvenafi.tpp.features.definitions.exceptions import UnexpectedValue

if TYPE_CHECKING:
    from pyvenafi.tpp.api.websdk.models import (
        config,
        identity as ident,
    )

@feature('Network Discovery')
class NetworkDiscovery(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        hosts: list[str],
        default_certificate_location: 'Union[config.Object, str]',
        attributes: dict = None,
        automatically_import: bool = False,
        blackout: dict[str, List] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        exclusion_locations: 'Union[config.Object, str]' = None,
        hour: int = None,
        placement_rules: 'list[Union[config.Object, str]]' = None,
        ports: list[Union[str, int]] = None,
        priority: int = None,
        reschedule: bool = True,
        resolve_host: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates a Network Discovery job.

        Args:
            name: Name of the discovery job.
            hosts: A list of hosts. If specific hosts should scan different ports, then specify by appending the
                   port to the IP address or hostname (i.e. 192.168.0.10:80). If no port is specified, then the
                   `ports` parameter will be appended to those hosts.
            default_certificate_location: :ref:`config_object` or :ref:`dn` of the folder to place results not 
                                          matching a placement rule.
            attributes: Additional attributes.
            automatically_import: If `True`, the job will terminate by placing the certificate objects, device
                                  objects, and application objects according to the placement rules.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            exclusion_locations: List of :ref:`config_object` or :ref:`dn` of exclusion folders.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            placement_rules: List of :ref:`config_object` or :ref:`dn` for the placement rules. The order of the list matters
                             as the rules are prioritized accordingly.
            ports: List of ports to scan.
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            resolve_host: Resolve the hostname when ``True``.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        placement_rule_guids = None
        if placement_rules:
            placement_rule_guids = [f'{e}:{self._get_guid(pr)}' for e, pr in enumerate(placement_rules)]
        ports = ','.join(list(map(str, ports))) if ports else \
            "22,80,443-449,465,563,636,695,981-995,1311,1920,2083,2087,2096,2211,2484,2949,3268,3269,3414," \
            "4712,4843,5223,5358,6619,6679,6697,7002,8080,8222,8243,8333,8443,8878,8881,8882,9043,9090," \
            "9091,9443,18072,18080-18085,18090-18094,28080"
        address_range = [f'{h}:{ports}' if ':' not in h else h for h in hosts]

        if blackout:
            blackout = [f'{k}:{",".join(v)}' for k, v in blackout.items()]

        attributes = attributes or {}
        attributes.update(
            {
                DiscoveryAttributes.address_range          : address_range,
                DiscoveryAttributes.automatically_import   : "1" if automatically_import else "0",
                DiscoveryAttributes.blackout               : blackout,
                DiscoveryAttributes.certificate_location_dn: self._get_dn(default_certificate_location)
                if default_certificate_location else None,
                DiscoveryAttributes.contact                : [self._get_prefixed_universal(c) for c in
                                                              contacts] if contacts else None,
                DiscoveryAttributes.description            : description,
                DiscoveryAttributes.discovery_exclusion_dn : [self._get_dn(el) for el in exclusion_locations]
                if exclusion_locations else None,
                DiscoveryAttributes.placement_rule         : placement_rule_guids,
                DiscoveryAttributes.priority               : priority,
                DiscoveryAttributes.reschedule             : "1" if hour and reschedule else "0",
                DiscoveryAttributes.resolve_host           : "1" if resolve_host else "0",
                DiscoveryAttributes.utc                    : utc
            }
        )

        if hour:
            attributes[DiscoveryAttributes.hour] = hour
            if days_of_week:
                attributes[DiscoveryAttributes.days_of_week] = days_of_week
            elif days_of_month:
                attributes[DiscoveryAttributes.days_of_month] = days_of_month
            elif days_of_year:
                attributes[DiscoveryAttributes.days_of_year] = days_of_year

        return self._config_create(
            name=name,
            parent_folder_dn=self._discovery_dn,
            config_class=DiscoveryAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, job: 'Union[config.Object, str]'):
        """
        Deletes the discovery job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_guid = self._get_guid(job, parent_dn=self._discovery_dn)
        self._api.websdk.Discovery.Guid(guid=job_guid).delete()

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: Name of the discovery job.
            raise_error_if_not_exists: Raise an exception if the discovery job does not exist.

        Returns:
            :ref:`config_object` of the discovery job.
        """
        return self._get_config_object(
            object_dn=f'{self._discovery_dn}\\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def is_in_progress(self, job: 'Union[config.Object, str]'):
        """
        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.

        Returns:
            bool: ``True`` if the job is in progress or ``False`` if it is not.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        try:
            response = self._api.websdk.Config.Read.post(
                object_dn=job_dn,
                attribute_name=DiscoveryAttributes.status
            )
            in_progress_states = ['Pending Execution', 'Running']
            if len(response.values) > 0:
                status = response.values[0]
                return status in in_progress_states
            return False
        except InvalidResponseError:
            return False

    def schedule(
        self, job: 'Union[config.Object, str]', hour: Union[str, int], days_of_week: list[Union[int, str]] = None,
        days_of_month: list[Union[int, str]] = None, days_of_year: list[str] = None
    ):
        """
        Schedules an existing job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            hour: 24-hour UTC hour format (i.e. 20 = 8PM UTC).
            days_of_week: Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Days of the month without leading zeros.
            days_of_year: Days of the year in "MM/DD" format without leading zeros (i.e. 1/23, 10/3).
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        hour = str(hour)
        if not isinstance(hour, list):
            hour = [hour]

        attributes = {
            DiscoveryAttributes.reschedule: "1",
            DiscoveryAttributes.hour      : hour
        }
        if days_of_week:
            attributes[DiscoveryAttributes.days_of_week] = map(str, days_of_week)
        elif days_of_month:
            attributes[DiscoveryAttributes.days_of_month] = map(str, days_of_month)
        elif days_of_year:
            attributes[DiscoveryAttributes.days_of_year] = days_of_year

        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes)
        )

    def unschedule(self, job: 'Union[config.Object, str]'):
        """
        Removes a schedule from a job. This does not delete the job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        for attribute_name in {
            DiscoveryAttributes.hour,
            DiscoveryAttributes.days_of_year,
            DiscoveryAttributes.days_of_month,
            DiscoveryAttributes.days_of_week,
            DiscoveryAttributes.reschedule
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=job_dn,
                attribute_name=attribute_name
            )

    def blackout_schedule(
        self, job: 'Union[config.Object, str]', sunday: list[Union[str, int]] = None,
        monday: list[Union[str, int]] = None, tuesday: list[Union[str, int]] = None,
        wednesday: list[Union[str, int]] = None, thursday: list[Union[str, int]] = None,
        friday: list[Union[str, int]] = None, saturday: list[Union[str, int]] = None
    ):
        """
        Times of the week to restrict a discovery job from processing.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            sunday: List of hours without leading zeros to restrict processing on Sunday.
            monday: List of hours without leading zeros to restrict processing on Monday.
            tuesday: List of hours without leading zeros to restrict processing on Tuesday.
            wednesday: List of hours without leading zeros to restrict processing on Wednesday.
            thursday: List of hours without leading zeros to restrict processing on Thursday.
            friday: List of hours without leading zeros to restrict processing on Friday.
            saturday: List of hours without leading zeros to restrict processing on Saturday.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        blackout = []
        for e, day in enumerate([sunday, monday, tuesday, wednesday, thursday, friday, saturday]):
            if day:
                hours = ','.join(map(str, day))
                blackout.append(f'{e}:{hours}')
        attributes = {
            DiscoveryAttributes.blackout: blackout
        }
        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes)
        )

    def run_now(self, job: 'Union[config.Object, str]', timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing,
        or has a *Processing* Attribute.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(
                {
                    "Start Now": ['1']  # Secret config-bridge attribute name.
                }
            )
        )

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=0.5):
                if self.is_in_progress(job=job):
                    return

        raise UnexpectedValue(
            f'Expected the job "{job_dn}" to start progress, but it did not.'
        )

    def cancel(self, job: 'Union[config.Object, str]'):
        """
        Cancels a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Canceled']
        )

    def pause(self, job: 'Union[config.Object, str]'):
        """
        Pauses a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Paused']
        )

    def resume(self, job: 'Union[config.Object, str]'):
        """
        Resumes a currently paused job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Pending']
        )

    def place_results(self, job: 'Union[config.Object, str]'):
        """
        .. warning::
            This functionality has been deprecated in TPP 21.1 and will have no effect
            from this version forward.

        Places the results of the discovery job according to the placement rules.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        if self._is_version_compatible(maximum="20.4"):
            job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
            self._api.websdk.Config.WriteDn.post(
                object_dn=job_dn,
                attribute_name="Import Results Now",  # Secret config-bridge attribute name.
                values=['1']
            )
        else:
            self._log_warning_message(
                'Cannot run place_results() because it has been deprecated since TPP 21.1. Results '
                'are placed along with discovery beginning in 21.1.'
            )

    def get_all_jobs(self):
        """
        Returns:
            List of :ref:`config_object` of all network discovery jobs.
        """
        jobs = self._api.websdk.Config.FindObjectsOfClass.post(
            class_name='Discovery',
            object_dn=self._discovery_dn
        )

        return jobs.objects

    def wait_for_job_to_finish(self, job: 'Union[config.Object, str]', check_interval: int = 5, timeout: int = 300):
        """
        Waits for the  *Status* attribute to have a value other than *Pending Execution* and *Running*
        on the discovery job. An error is raised if the timeout is exceeded.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            check_interval: Poll interval in seconds to validate that the job finished.
            timeout: Timeout in seconds to wait for the job to finish.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=check_interval):
                if not self.is_in_progress(job=job):
                    return

        status = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status
        ).values[0]
        raise TimeoutError(
            f'Expected Network Discovery Job "{job_dn}" to finish within {timeout} seconds, but it is still '
            f'running. It has a status of "{status}."'
        )

class OnboardDiscoveryBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def _create(
        self,
        name: str,
        installation_type: str,
        driver_name: str,
        attributes: dict,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        if blackout:
            blackout = [f'{k}:{",".join(v)}' for k, v in blackout.items()]
        attributes.update(
            {
                OnboardDiscoveryAttributes.application_type             : installation_type,
                OnboardDiscoveryAttributes.driver_name                  : driver_name,
                OnboardDiscoveryAttributes.certificates_placement_folder: self._get_dn(certificate_placement_folder),
                DiscoveryAttributes.blackout                            : blackout,
                DiscoveryAttributes.contact                             : [self._get_prefixed_universal(c) for c in
                                                                           contacts] if contacts else None,
                DiscoveryAttributes.description                         : description,
                DiscoveryAttributes.priority                            : priority,
                DiscoveryAttributes.reschedule                          : "1" if hour and reschedule else "0",
                DiscoveryAttributes.utc                                 : utc,

            }
        )

        if hour:
            attributes[DiscoveryAttributes.hour] = hour
            if days_of_week:
                attributes[DiscoveryAttributes.days_of_week] = days_of_week
            elif days_of_month:
                attributes[DiscoveryAttributes.days_of_month] = days_of_month
            elif days_of_year:
                attributes[DiscoveryAttributes.days_of_year] = days_of_year

        return self._config_create(
            name=name, parent_folder_dn=self._discovery_dn,
            config_class=OnboardDiscoveryAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, job: 'Union[config.Object, str]'):
        """
        Deletes the discovery job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._secret_store_delete(job_dn)
        self._config_delete(job_dn)

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: Name of the discovery job.
            raise_error_if_not_exists: Raise an exception if the discovery job does not exist.

        Returns:
            :ref:`config_object` of the discovery job.
        """
        return self._get_config_object(
            object_dn=f'{self._discovery_dn}\\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def is_in_progress(self, job: 'Union[config.Object, str]'):
        """
        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.

        Returns:
            bool: ``True`` if the job is in progress or ``False`` if it is not.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        try:
            response = self._api.websdk.Config.Read.post(
                object_dn=job_dn,
                attribute_name=DiscoveryAttributes.status
            )
            in_progress_states = ['Pending Execution', 'Running']
            if len(response.values) > 0:
                status = response.values[0]
                return status in in_progress_states
            return False
        except InvalidResponseError:
            return False

    def schedule(
        self, job: 'Union[config.Object, str]', hour: Union[str, int], days_of_week: list[Union[int, str]] = None,
        days_of_month: list[Union[int, str]] = None, days_of_year: list[str] = None
    ):
        """
        Schedules an existing job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            hour: 24-hour UTC hour format (i.e. 20 = 8PM UTC).
            days_of_week: Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Days of the month without leading zeros.
            days_of_year: Days of the year in "MM/DD" format without leading zeros (i.e. 1/23, 10/3).
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        hour = str(hour)

        attributes = {
            DiscoveryAttributes.reschedule: "1",
            DiscoveryAttributes.hour      : hour
        }
        if days_of_week:
            attributes[DiscoveryAttributes.days_of_week] = list(map(str, days_of_week))
        elif days_of_month:
            attributes[DiscoveryAttributes.days_of_month] = list(map(str, days_of_month))
        elif days_of_year:
            attributes[DiscoveryAttributes.days_of_year] = list(map(str, days_of_year))

        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes)
        )

    def unschedule(self, job: 'Union[config.Object, str]'):
        """
        Removes a schedule from a job. This does not delete the job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        for attribute_name in {
            DiscoveryAttributes.hour,
            DiscoveryAttributes.days_of_year,
            DiscoveryAttributes.days_of_month,
            DiscoveryAttributes.days_of_week,
            DiscoveryAttributes.reschedule
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=job_dn,
                attribute_name=attribute_name
            )

    def blackout_schedule(
        self, job: 'Union[config.Object, str]', sunday: list[Union[str, int]] = None,
        monday: list[Union[str, int]] = None, tuesday: list[Union[str, int]] = None,
        wednesday: list[Union[str, int]] = None, thursday: list[Union[str, int]] = None,
        friday: list[Union[str, int]] = None, saturday: list[Union[str, int]] = None
    ):
        """
        Times of the week to restrict a discovery job from processing.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            sunday: List of hours without leading zeros to restrict processing on Sunday.
            monday: List of hours without leading zeros to restrict processing on Monday.
            tuesday: List of hours without leading zeros to restrict processing on Tuesday.
            wednesday: List of hours without leading zeros to restrict processing on Wednesday.
            thursday: List of hours without leading zeros to restrict processing on Thursday.
            friday: List of hours without leading zeros to restrict processing on Friday.
            saturday: List of hours without leading zeros to restrict processing on Saturday.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        blackout = []
        for e, day in enumerate([sunday, monday, tuesday, wednesday, thursday, friday, saturday]):
            if day:
                hours = ','.join(map(str, day))
                blackout.append(f'{e}:{hours}')
        attributes = {
            DiscoveryAttributes.blackout: blackout
        }
        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes)
        )

    def run_now(self, job: 'Union[config.Object, str]', timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing,
        or has a *Processing* Attribute.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(
                {
                    "Start Now": ['1']  # Secret config-bridge attribute name.
                }
            )
        )

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=0.5):
                if self.is_in_progress(job=job):
                    return

        raise UnexpectedValue(
            f'Expected the job "{job_dn}" to start progress, but it did not.'
        )

    def cancel(self, job: 'Union[config.Object, str]'):
        """
        Cancels a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Canceled']
        )

    def pause(self, job: 'Union[config.Object, str]'):
        """
        Pauses a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Paused']
        )

    def resume(self, job: 'Union[config.Object, str]'):
        """
        Resumes a currently paused job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Pending']
        )

    def get_all_jobs(self):
        """
        Returns:
            List of :ref:`config_object` of all network discovery jobs.
        """
        jobs = self._api.websdk.Config.FindObjectsOfClass.post(
            class_name=OnboardDiscoveryAttributes.__config_class__,
            object_dn=self._discovery_dn
        )

        return jobs.objects

    def wait_for_job_to_finish(self, job: 'Union[config.Object, str]', check_interval: int = 5, timeout: int = 300):
        """
        Waits for the  *Status* attribute to have a value other than *Pending Execution* and *Running*
        on the discovery job. An error is raised if the timeout is exceeded.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            check_interval: Poll interval in seconds to validate that the job finished.
            timeout: Timeout in seconds to wait for the job to finish.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=check_interval):
                if not self.is_in_progress(job=job):
                    return

        status = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status
        ).values[0]
        raise TimeoutError(
            f'Expected Network Discovery Job "{job_dn}" to finish within {timeout} seconds, but it is still '
            f'running. It has a status of "{status}."'
        )

@feature('Adaptable Onboard Discovery')
class AdaptableOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        devices_to_scan: list[Union[str, config.Object]] = None,
        folder_with_devices_to_scan: Union[str, config.Object] = None,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates an Adaptable Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            devices_to_scan: A list of :ref:`config_object` or :ref:`dn` of the device objects to scan.
            folder_with_devices_to_scan: A :ref:`config_object` or :ref:`dn` of the folder having device objects to scan.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}
        if devices_to_scan:
            devices_to_scan = [self._get_dn(d) for d in devices_to_scan]
            attributes[OnboardDiscoveryAttributes.device] = devices_to_scan
        if folder_with_devices_to_scan:
            attributes[OnboardDiscoveryAttributes.devices_folder] = self._get_dn(folder_with_devices_to_scan)
        return self._create(
            name=name,
            installation_type='Adaptable',
            driver_name='appadaptable',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('AWS Onboard Discovery')
class AmazonOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        amazon_credential: Union[str, config.Object],
        amazon_account_ids: list[str] = None,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates an AWS Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            amazon_credential: A :ref:`config_object` or :ref:`dn` of the Amazon credential.
            amazon_account_ids: A list of Amazon account IDs.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}
        attributes.update(
            {
                OnboardDiscoveryAttributes.credential        : self._get_dn(amazon_credential),
                OnboardDiscoveryAttributes.amazon_account_ids: amazon_account_ids
            }
        )
        return self._create(
            name=name,
            installation_type='Amazon Web Services',
            driver_name='appamazon',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('Azure Onboard Discovery')
class AzureOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        azure_credential: Union[str, config.Object],
        azure_application_id: str,
        azure_tenant_id: str,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates an Azure Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            azure_credential: A :ref:`config_object` or :ref:`dn` of the Azure credential.
            azure_application_id: Azure application ID.
            azure_tenant_id: Azure tenant ID.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}
        attributes.update(
            {
                OnboardDiscoveryAttributes.credential          : self._get_dn(azure_credential),
                OnboardDiscoveryAttributes.azure_application_id: azure_application_id,
                OnboardDiscoveryAttributes.azure_tenant_id     : azure_tenant_id,
            }
        )
        return self._create(
            name=name,
            installation_type='Azure Key Vault',
            driver_name='appazurekeyvault',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('CAPI Onboard Discovery')
class CapiOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        devices_to_scan: list[Union[str, config.Object]] = None,
        extract_private_key_if_possible: bool = False,
        folder_with_devices_to_scan: Union[str, config.Object] = None,
        winrm_port: int = 5986,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates a CAPI (IIS Bindings) Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            extract_private_key_if_possible: If ``True``, extract the private key.
            winrm_port: WinRM port.
            devices_to_scan: A list of :ref:`config_object` or :ref:`dn` of the device objects to scan.
            folder_with_devices_to_scan: A :ref:`config_object` or :ref:`dn` of the folder having device objects to scan.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}
        attributes[OnboardDiscoveryAttributes.port] = winrm_port
        if devices_to_scan:
            devices_to_scan = [self._get_dn(d) for d in devices_to_scan]
            attributes[OnboardDiscoveryAttributes.device] = devices_to_scan
        if folder_with_devices_to_scan:
            attributes[OnboardDiscoveryAttributes.devices_folder] = self._get_dn(folder_with_devices_to_scan)
        if extract_private_key_if_possible:
            attributes[OnboardDiscoveryAttributes.extract_private_key] = "1"
        return self._create(
            name=name,
            installation_type='CAPI (IIS Bindings)',
            driver_name='appcapi',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('Citrix NetScaler Onboard Discovery')
class NetScalerOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        certificates_to_import: Union[Literal['virtual', 'gateway', 'services', 'all'], int],
        keystore_and_private_key_credential: Union[str, config.Object] = None,
        devices_to_scan: list[Union[str, config.Object]] = None,
        extract_private_key_if_possible: bool = False,
        folder_with_devices_to_scan: Union[str, config.Object] = None,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates a Citrix NetScaler Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            devices_to_scan: A list of :ref:`config_object` or :ref:`dn` of the device objects to scan.
            folder_with_devices_to_scan: A :ref:`config_object` or :ref:`dn` of the folder having device objects to scan.
            extract_private_key_if_possible: If ``True``, extract the private key.
            certificates_to_import: Certificate profile from which to import certificates.
            keystore_and_private_key_credential: A :ref:`config_object` or :ref:`dn` of the keystore and private key credential.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}

        if isinstance(certificates_to_import, str):
            certificates_to_import = {
                'virtual' : 0,  # Only Virtual Servers
                'services': 1,  # Only Services and Groups
                'all'     : 2,  # All
                'gateway' : 3,  # Only Gateway Virtual Servers
            }.get(certificates_to_import)

        attributes.update(
            {
                OnboardDiscoveryAttributes.profiles_to_import: certificates_to_import
            }
        )
        if devices_to_scan:
            devices_to_scan = [self._get_dn(d) for d in devices_to_scan]
            attributes[OnboardDiscoveryAttributes.device] = devices_to_scan
        if folder_with_devices_to_scan:
            attributes[OnboardDiscoveryAttributes.devices_folder] = self._get_dn(folder_with_devices_to_scan)
        if extract_private_key_if_possible:
            attributes[OnboardDiscoveryAttributes.extract_private_key] = "1"
        if keystore_and_private_key_credential:
            attributes[OnboardDiscoveryAttributes.credential] = keystore_and_private_key_credential
        return self._create(
            name=name,
            installation_type='Citrix NetScaler',
            driver_name='appnetscaler',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('F5 LTM Advanced Onboard Discovery')
class F5LtmAdvancedOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        certificates_to_import: Union[Literal['server', 'client', 'both'], int],
        port: int = 443,
        devices_to_scan: list[Union[str, config.Object]] = None,
        extract_private_key_if_possible: bool = False,
        folder_with_devices_to_scan: Union[str, config.Object] = None,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates an F5 LTM Advanced Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            devices_to_scan: A list of :ref:`config_object` or :ref:`dn` of the device objects to scan.
            folder_with_devices_to_scan: A :ref:`config_object` or :ref:`dn` of the folder having device objects to scan.
            extract_private_key_if_possible: If ``True``, extract the private key.
            certificates_to_import: Certificate profile from which to import certificates.
            port: Connection port.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}

        if isinstance(certificates_to_import, str):
            certificates_to_import = {
                'both'  : 0,
                'client': 1,
                'server': 2,
            }.get(certificates_to_import)

        attributes.update(
            {
                OnboardDiscoveryAttributes.profiles_to_import: certificates_to_import,
                OnboardDiscoveryAttributes.port              : port
            }
        )
        if devices_to_scan:
            devices_to_scan = [self._get_dn(d) for d in devices_to_scan]
            attributes[OnboardDiscoveryAttributes.device] = devices_to_scan
        if folder_with_devices_to_scan:
            attributes[OnboardDiscoveryAttributes.devices_folder] = self._get_dn(folder_with_devices_to_scan)
        if extract_private_key_if_possible:
            attributes[OnboardDiscoveryAttributes.extract_private_key] = "1"
        return self._create(
            name=name,
            installation_type='F5 LTM Advanced',
            driver_name='appf5ltmadvanced',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )

@feature('IBM DataPower Onboard Discovery')
class IbmDataPowerOnboardDiscovery(OnboardDiscoveryBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(
        self,
        name: str,
        certificates_to_import: Union[Literal['server', 'client', 'proxy', 'all'], int],
        port: int = 443,
        devices_to_scan: list[Union[str, config.Object]] = None,
        extract_private_key_if_possible: bool = False,
        folder_with_devices_to_scan: Union[str, config.Object] = None,
        attributes: dict = None,
        blackout: dict[str, List] = None,
        certificate_placement_folder: Union[str, config.Object] = None,
        contacts: 'list[Union[ident.Identity, str]]' = None,
        days_of_week: list[str] = None,
        days_of_month: list[str] = None,
        days_of_year: list[str] = None,
        description: str = None,
        hour: int = None,
        priority: int = None,
        reschedule: bool = True,
        utc: str = '1',
        get_if_already_exists: bool = True
    ):
        """
        Creates an IBM DataPower Onboard Discovery job.

        Args:
            name: Name of the discovery job.
            devices_to_scan: A list of :ref:`config_object` or :ref:`dn` of the device objects to scan.
            folder_with_devices_to_scan: A :ref:`config_object` or :ref:`dn` of the folder having device objects to scan.
            extract_private_key_if_possible: If ``True``, extract the private key.
            certificates_to_import: Certificate profile from which to import certificates.
            port: Connection port.
            certificate_placement_folder: A :ref:`config_object` or :ref:`dn` of the folder to place the certificates.
            attributes: Additional attributes.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        attributes = attributes or {}

        if isinstance(certificates_to_import, str):
            certificates_to_import = {
                'all'   : 0,
                'client': 1,
                'proxy' : 2,
                'server': 3,
            }.get(certificates_to_import)

        attributes.update(
            {
                OnboardDiscoveryAttributes.profiles_to_import: certificates_to_import,
                OnboardDiscoveryAttributes.port              : port
            }
        )
        if devices_to_scan:
            devices_to_scan = [self._get_dn(d) for d in devices_to_scan]
            attributes[OnboardDiscoveryAttributes.device] = devices_to_scan
        if folder_with_devices_to_scan:
            attributes[OnboardDiscoveryAttributes.devices_folder] = self._get_dn(folder_with_devices_to_scan)
        if extract_private_key_if_possible:
            attributes[OnboardDiscoveryAttributes.extract_private_key] = "1"
        return self._create(
            name=name,
            installation_type='IBM DataPower',
            driver_name='appdatapower',
            attributes=attributes,
            blackout=blackout,
            certificate_placement_folder=certificate_placement_folder,
            contacts=contacts,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
            days_of_year=days_of_year,
            description=description,
            hour=hour,
            priority=priority,
            reschedule=reschedule,
            utc=utc,
            get_if_already_exists=get_if_already_exists,
        )
