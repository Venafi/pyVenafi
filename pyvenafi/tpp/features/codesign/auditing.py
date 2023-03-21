from typing import Union

from pyvenafi.tpp.api.websdk.models.codesign import (
    AppleEnvironment,
    ArchiveFilter,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    KeyPairEnvironment,
)
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

EnvironmentTypes = Union[
    AppleEnvironment,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    KeyPairEnvironment,
]

@feature('Auditing')
class CodeSignAuditing(FeatureBase):
    def retrieve_archive_entries(
        self,
        archive_filter: ArchiveFilter,
        page_size: int = None,
        page: int = None
    ):
        """
        Retrieve archive entries using an :class:`~.models.codesign.ArchiveFilter`.

        Args:
            archive_filter: Contains filters to apply in retrieval search.
            page_size: Size of paginated result.
            page: Page number of results to retrieve.

        Returns:
             Output dataclass containing :class:`~.models.codesign.ArchiveResults`
        """
        output = self._api.websdk.Codesign.RetrieveArchiveEntries.post(
            archive_filter=archive_filter,
            page_size=page_size,
            page=page
        )
        return output
