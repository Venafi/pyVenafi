from typing import List, Dict, Union
from venafi.properties.config import DiscoveryAttributes, DiscoveryAttributeValues, DiscoveryClassNames
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class NetworkDiscovery(FeatureBase):
    """
    This feature provides high-level interaction with TPP device objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._discovery_dn = r'\VED\Discovery'

    def _is_in_progress(self, job_dn: str):
        return len(self._auth.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.Network.in_progress
        ).values) == 0

    def create(self, name: str, hosts: List[str], default_certificate_dn: str, attributes: dict = None,
               automatically_import: bool = False, blackout: Dict[str, List] = None,
               contacts: List[str] = None, days_of_week: List[str] = None, days_of_month: List[str] = None,
               days_of_year: List[str] = None, description: str = None, exclusion_dns: List[str] = None,
               hour: int = None, placement_rule_guids: List[str] = None, ports: List[Union[str, int]] = None,
               priority: int = None, reschedule: bool = True, resolve_host: bool = True, utc: str = '1'):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

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
            DiscoveryAttributes.Network.automatically_import: "1" if automatically_import else "0",
            DiscoveryAttributes.Network.blackout : blackout,
            DiscoveryAttributes.Network.certificate_location_dn: default_certificate_dn,
            DiscoveryAttributes.contact: contacts,
            DiscoveryAttributes.description: description,
            DiscoveryAttributes.Network.discovery_exclusion_dn: exclusion_dns,
            DiscoveryAttributes.Network.placement_rule: [f'{e}:{guid}' for e, guid in enumerate(placement_rule_guids)],
            DiscoveryAttributes.Network.priority: priority,
            DiscoveryAttributes.Network.reschedule: "1" if hour and reschedule else "0",
            DiscoveryAttributes.Network.resolve_host: "1" if resolve_host else "0",
            DiscoveryAttributes.Network.utc: utc
        })

        if hour:
            attributes[DiscoveryAttributes.Network.hour] = hour
            if days_of_week:
                attributes[DiscoveryAttributes.Network.days_of_week] = days_of_week
            elif days_of_month:
                attributes[DiscoveryAttributes.Network.days_of_month] = days_of_month
            elif days_of_year:
                attributes[DiscoveryAttributes.Network.days_of_year] = days_of_year

        return self._config_create(
            name=name,
            parent_folder_dn=self._discovery_dn,
            config_class=DiscoveryClassNames.network_discovery,
            attributes=attributes
        )

    def delete(self, job_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Discovery.Guid(guid=job_guid).delete()
        response.assert_valid_response()

    def get(self, name: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self._auth.websdk.Config.IsValid.post(object_dn=f'{self._discovery_dn}\\{name}').object

    def schedule(self, name: str, hour: Union[str, int], days_of_week: List[str] = None,
                 days_of_month: List[str] = None, days_of_year: List[str] = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        hour = str(hour)
        if not isinstance(hour, list):
            hour = [hour]

        attributes = {
            DiscoveryAttributes.Network.reschedule: "1",
            DiscoveryAttributes.Network.hour: hour
        }
        if days_of_week:
            attributes[DiscoveryAttributes.Network.days_of_week] = days_of_week
        elif days_of_month:
            attributes[DiscoveryAttributes.Network.days_of_month] = days_of_month
        elif days_of_year:
            attributes[DiscoveryAttributes.Network.days_of_year] = days_of_year

        response = self._auth.websdk.Config.Write.post(
            object_dn=f'{self._discovery_dn}\\{name}',
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def unschedule(self, name: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        job_dn = f'{self._discovery_dn}\\{name}'
        for attribute_name in {
            DiscoveryAttributes.Network.hour,
            DiscoveryAttributes.Network.days_of_year,
            DiscoveryAttributes.Network.days_of_month,
            DiscoveryAttributes.Network.days_of_week,
            DiscoveryAttributes.Network.reschedule
        }:
            self._auth.websdk.Config.ClearAttribute.post(
                object_dn=job_dn,
                attribute_name=attribute_name
            ).assert_valid_response()

    def blackout_schedule(self, name, sunday: list = None, monday: list = None, tuesday: list = None,
                          wednesday: list = None, thursday: list = None, friday: list = None,
                          saturday: list = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        blackout = []
        for e, day in enumerate([sunday, monday, tuesday, wednesday, thursday, friday, saturday]):
            if day:
                hours = ','.join(map(str, day))
                blackout.append(f'{e}:{hours}')
        attributes = {
            DiscoveryAttributes.Network.blackout: blackout
        }
        response = self._auth.websdk.Config.Write.post(
            object_dn=f'{self._discovery_dn}\\{name}',
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def run_now(self, job_guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Jobs.NetworkDiscovery.Guid(guid=job_guid).Actions.post(job_action='runNow')
        response.assert_valid_response()

        job_dn = self._auth.websdk.Config.GuidToDn.post(object_guid=job_guid).object_dn
        with self._Timeout(timeout=10) as to:
            while not to.is_expired():
                if self._is_in_progress(job_dn=job_dn):
                    return

        raise FeatureError.UnexpectedValue(
            f'Expected the job "{job_dn}" to start progress, but it did not.'
        )

    def cancel(self, job_guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Jobs.NetworkDiscovery.Guid(guid=job_guid).Actions.post(job_action='abort')
        response.assert_valid_response()

    def pause(self, job_guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Jobs.NetworkDiscovery.Guid(guid=job_guid).Actions.post(job_action='pause')
        response.assert_valid_response()

    def resume(self, job_guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Jobs.NetworkDiscovery.Guid(guid=job_guid).Actions.post(job_action='resume')
        response.assert_valid_response()

    def place_results(self, job_guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Jobs.NetworkDiscovery.Guid(guid=job_guid).Actions.post(job_action='importResults')
        response.assert_valid_response()

    def get_all_jobs(self):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        jobs = self._auth.websdk.Config.FindObjectsOfClass.post(
            class_name='Discovery',
            object_dn=self._discovery_dn
        )

        return jobs.objects

    def wait_for_job_to_finish(self, job_dn: str, check_interval: int = 30, timeout: int = 300):
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=check_interval):
                if not self._is_in_progress(job_dn=job_dn):
                    return

        status = self._auth.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.Network.status
        ).values[0]
        raise FeatureError.UnexpectedValue(
            f'Expected Network Discovery Job "{job_dn}" to finish within {timeout} seconds, but it is still '
            f'running. It has a status of "{status}."'
        )
