from typing import List, Dict, Union
from pytpp.vtypes import Config
from pytpp.properties.config import DiscoveryClassNames
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.attributes.discovery import DiscoveryAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.placement_job import PlacementJobAttributes


@feature()
class NetworkDiscovery(FeatureBase):
    """
    This feature provides high-level interaction with TPP Network Discovery objects.
    """
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def _is_in_progress(self, job: Union['Config.Object', str]):
        """
        Returns a boolean value according to whether a job is currently in progress or not.

        Args:
            job: Config object or name of the discovery job.

        Returns:
            Boolean value
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status
        )
        in_progress_states = ['Pending Execution', 'Running']
        if response.is_valid_response():
            if len(response.values) > 0:
                status = response.values[0]
                return status in in_progress_states
        return False

    def create(self, name: str, hosts: List[str], default_certificate_dn: str, attributes: dict = None,
               automatically_import: bool = False, blackout: Dict[str, List] = None,
               contacts: List[str] = None, days_of_week: List[str] = None, days_of_month: List[str] = None,
               days_of_year: List[str] = None, description: str = None, exclusion_dns: List[str] = None,
               hour: int = None, placement_rule_guids: List[str] = None, ports: List[Union[str, int]] = None,
               priority: int = None, reschedule: bool = True, resolve_host: bool = True, utc: str = '1',
               get_if_already_exists: bool = True):
        """
        Creates a network discovery job.

        Examples:

        .. code-block::python

                features.discovery.create(
                    name='My Discovery Job',
                    hosts=['192.168.0.1/24', '10.0.1.64-10.0.1.75', '10.0.1.201:80'],
                    default_certificate_dn=r'\VED\Policy\Certificates\Homeless',
                    automatically_import=False,
                    blackout={
                        '0':list(map(str, range(13, 20))),  # Sunday from 1PM-8PM UTC
                    },
                    contacts=[user1.guid, user2.guid],
                    days_of_week=['0', '3'],
                    description='Does important scanning.',
                    hour=4,  # 4AM UTC
                    placement_rule_guids=[rule1.guid, rule2.guid],
                    ports=[22, 80, 443],
                    priority=1,
                    reschedule=True,
                    resolve_host=True,
                )

        Args:
            name: Name of the discovery job.
            hosts: A list of hosts. If specific hosts should scan different ports, then specify by appending the
                   port to the IP address or hostname (i.e. 192.168.0.10:80). If no port is specified, then the
                   `ports` parameter will be appended to those hosts.
            default_certificate_dn: Absolute path to the default folder that will contain all certificates not
                                    matching a placement rule.
            attributes: Additional attributes.
            automatically_import: If `True`, the job will terminate by placing the certificate objects, device
                                  objects, and application objects according to the placement rules.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of identity prefixed universal GUIDs.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            exclusion_dns: List of absolute paths to exclusion DN folders.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            placement_rule_guids: List of GUIDs for the placement rules. The order of the list matters as the
                                  rules are prioritized accordingly.
            ports: List of ports to scan.
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            resolve_host: Resolve the hostname when ``True``.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object of the discovery job.

        """
        ports = ','.join(list(map(str, ports))) if ports else \
            "22,80,443-449,465,563,636,695,981-995,1311,1920,2083,2087,2096,2211,2484,2949,3268,3269,3414," \
            "4712,4843,5223,5358,6619,6679,6697,7002,8080,8222,8243,8333,8443,8878,8881,8882,9043,9090," \
            "9091,9443,18072,18080-18085,18090-18094,28080"
        address_range = [f'{h}:{ports}' if ':' not in h else h for h in hosts]

        if blackout:
            blackout = [f'{k}:{",".join(v)}' for k, v in blackout.items()]

        attributes = attributes or {}
        attributes.update({
            DiscoveryAttributes.address_range: address_range,
            DiscoveryAttributes.automatically_import: "1" if automatically_import else "0",
            ScheduleBaseAttributes.blackout : blackout,
            DiscoveryAttributes.certificate_location_dn: default_certificate_dn,
            DiscoveryAttributes.contact: contacts,
            DiscoveryAttributes.description: description,
            DiscoveryAttributes.discovery_exclusion_dn: exclusion_dns,
            DiscoveryAttributes.placement_rule: [f'{e}:{guid}' for e, guid in enumerate(placement_rule_guids)],
            DiscoveryAttributes.priority: priority,
            ScheduleBaseAttributes.reschedule: "1" if hour and reschedule else "0",
            DiscoveryAttributes.resolve_host: "1" if resolve_host else "0",
            ScheduleBaseAttributes.utc: utc
        })

        if hour:
            attributes[ScheduleBaseAttributes.hour] = hour
            if days_of_week:
                attributes[ScheduleBaseAttributes.days_of_week] = days_of_week
            elif days_of_month:
                attributes[ScheduleBaseAttributes.days_of_month] = days_of_month
            elif days_of_year:
                attributes[ScheduleBaseAttributes.days_of_year] = days_of_year

        return self._config_create(
            name=name,
            parent_folder_dn=self._discovery_dn,
            config_class=DiscoveryClassNames.network_discovery,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, job: Union['Config.Object', str]):
        """
        Deletes the discovery job.

        Args:
            job: Config object or name of the discovery job.
        """
        job_guid = self._get_guid(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Discovery.Guid(guid=job_guid).delete()
        response.assert_valid_response()

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: Name of the discovery job.
            raise_error_if_not_exists: Raise an exception if the discovery job does not exist.

        Returns:
            Config object of the discovery job.
        """
        return self._get_config_object(
            object_dn=f'{self._discovery_dn}\\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists,
            valid_class_names=list(DiscoveryClassNames)
        )

    def schedule(self, job: Union['Config.Object', str], hour: Union[str, int], days_of_week: List[str] = None,
                 days_of_month: List[str] = None, days_of_year: List[str] = None):
        """
        Schedules an existing job.

        Args:
            job: Config object or name of the discovery job.
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
            ScheduleBaseAttributes.reschedule: "1",
            ScheduleBaseAttributes.hour: hour
        }
        if days_of_week:
            attributes[ScheduleBaseAttributes.days_of_week] = days_of_week
        elif days_of_month:
            attributes[ScheduleBaseAttributes.days_of_month] = days_of_month
        elif days_of_year:
            attributes[ScheduleBaseAttributes.days_of_year] = days_of_year

        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def unschedule(self, job: Union['Config.Object', str]):
        """
        Removes a schedule from a job. This does not delete the job.

        Args:
            job: Config object or name of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        for attribute_name in {
            ScheduleBaseAttributes.hour,
            ScheduleBaseAttributes.days_of_year,
            ScheduleBaseAttributes.days_of_month,
            ScheduleBaseAttributes.days_of_week,
            ScheduleBaseAttributes.reschedule
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=job_dn,
                attribute_name=attribute_name
            ).assert_valid_response()

    def blackout_schedule(self, job: Union['Config.Object', str], sunday: List[Union[str, int]] = None, monday: List[Union[str, int]] = None,
                          tuesday: List[Union[str, int]] = None, wednesday: List[Union[str, int]] = None,
                          thursday: List[Union[str, int]] = None, friday: List[Union[str, int]] = None,
                          saturday: List[Union[str, int]] = None):
        """
        Times of the week to restrict a discovery job from processing.

        Args:
            job: Config object or name of the discovery job.
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
            ScheduleBaseAttributes.blackout: blackout
        }
        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def run_now(self, job: Union['Config.Object', str], timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing, or has a `Processing` Attribute.

        Args:
            job: Config object or name of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list({
                "Start Now": ['1']  # Secret config-bridge attribute name.
            })
        )
        response.assert_valid_response()

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if self._is_in_progress(job=job):
                    return

        raise FeatureError.UnexpectedValue(
            f'Expected the job "{job_dn}" to start progress, but it did not.'
        )

    def cancel(self, job: Union['Config.Object', str]):
        """
        Cancels a currently running job.

        Args:
            job: Config object or name of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=PlacementJobAttributes.status,
            values=['Canceled']
        )
        response.assert_valid_response()

    def pause(self, job: Union['Config.Object', str]):
        """
        Pauses a currently running job.

        Args:
            job: Config object or name of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=PlacementJobAttributes.status,
            values=['Paused']
        )
        response.assert_valid_response()

    def resume(self, job: Union['Config.Object', str]):
        """
        Resumes a currently paused job.

        Args:
            job: Config object or name of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=PlacementJobAttributes.status,
            values=['Pending']
        )
        response.assert_valid_response()

    def place_results(self, job: Union['Config.Object', str]):
        """
        Places the results of the discovery job according to the placement rules.

        Args:
            job: Config object or name of the discovery job.
        """
        if self._is_version_compatible(maximum="20.4"):
            job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
            response = self._api.websdk.Config.WriteDn.post(
                object_dn=job_dn,
                attribute_name="Import Results Now",  # Secret config-bridge attribute name.
                values=['1']
            )
            response.assert_valid_response()

    def get_all_jobs(self):
        """
        Returns:
            List of all network discovery jobs.
        """
        jobs = self._api.websdk.Config.FindObjectsOfClass.post(
            class_name='Discovery',
            object_dn=self._discovery_dn
        )

        return jobs.objects

    def wait_for_job_to_finish(self, job: Union['Config.Object', str], check_interval: int = 5, timeout: int = 300):
        """
        Waits for the `Status` attribute to have a value other than `Pending Execution` and `Running`
        on the discovery job. An error is raised if the timeout is exceeded.

        Args:
            job: Config object or name of the discovery job.
            check_interval: Poll interval in seconds to validate that the job finished.
            timeout: Timeout in seconds to wait for the job to finish.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=check_interval):
                if not self._is_in_progress(job=job):
                    return

        status = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=PlacementJobAttributes.status
        ).values[0]
        raise FeatureError.UnexpectedValue(
            f'Expected Network Discovery Job "{job_dn}" to finish within {timeout} seconds, but it is still '
            f'running. It has a status of "{status}."'
        )
