from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.plugins import Authenticate
from pytpp.tools.vtypes import Config
from pytpp.features.bases.feature_base import FeatureError, feature
from pytpp.features.discovery import NetworkDiscovery as _NetworkDiscovery
from pytpp.plugins.properties.network_discovery import NetworkDiscovery as _NetworkDiscoveryProperties


@feature(_NetworkDiscovery.__feature__)
class NetworkDiscovery(_NetworkDiscovery):
    """
    This feature provides high-level interaction with TPP Network Discovery objects.
    """

    def __init__(self, api: 'Authenticate'):
        super().__init__(api=api)
        if TYPE_CHECKING:
            self._api = api

    def run_now(self, job: 'Config.Object', timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing, or has a `Processing` Attribute.

        Args:
            job: Config object of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        response = self._api.aperture.Jobs.NetworkDiscovery.Guid(job.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.run_now
        )
        response.assert_valid_response()

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if self._is_in_progress(job=job):
                    return

        raise FeatureError.UnexpectedValue(
            f'Expected the job "{job.dn}" to start progress, but it did not.'
        )

    def cancel(self, job: 'Config.Object'):
        """
        Cancels a currently running job.

        Args:
            job: Config object of the discovery job.
        """
        response = self._api.aperture.Jobs.NetworkDiscovery.Guid(job.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.cancel
        )
        response.assert_valid_response()

    def pause(self, job: 'Config.Object'):
        """
        Pauses a currently running job.

        Args:
            job: Config object of the discovery job.
        """
        response = self._api.aperture.Jobs.NetworkDiscovery.Guid(job.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.pause
        )
        response.assert_valid_response()

    def resume(self, job: 'Config.Object'):
        """
        Resumes a currently paused job.

        Args:
            job: Config object of the discovery job.
        """
        response = self._api.aperture.Jobs.NetworkDiscovery.Guid(job.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.resume
        )
        response.assert_valid_response()

    def place_results(self, job: 'Config.Object'):
        """
        Places the results of the discovery job according to the placement rules.

        Args:
            job: Config object of the discovery job.
        """
        response = self._api.aperture.Jobs.NetworkDiscovery.Guid(job.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.place_now
        )
        response.assert_valid_response()
