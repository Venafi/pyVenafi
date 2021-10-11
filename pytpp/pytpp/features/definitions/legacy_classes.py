from pytpp.tools.deprecation import DeprecationMeta
from pytpp.properties.config import (
    ApplicationGroupClassNames, ApplicationClassNames, CertificateClassNames, DevicesClassNames, DiscoveryClassNames,
    IdentityClassNames, PlacementRulesClassNames, PlatformsClassNames, WorkflowClassNames, ClientWorkClassNames,
    ClientGroupsClassNames, FolderClassNames, CertificateAuthorityClassNames
)

class Classes(metaclass=DeprecationMeta):
    __deprecation_reason__ = 'Using Classes will be deprecated soon. Get the class names from the attributes using ' \
                             'pytpp.Attributes (from pytpp import Attributes) instead.'
    Application = ApplicationClassNames
    ApplicationGroup = ApplicationGroupClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    ClientGroups = ClientGroupsClassNames
    ClientWork = ClientWorkClassNames
    Device = DevicesClassNames
    Discovery = DiscoveryClassNames
    Folder = FolderClassNames
    Identity = IdentityClassNames
    PlacementRules = PlacementRulesClassNames
    Platforms = PlatformsClassNames
    Workflow = WorkflowClassNames
