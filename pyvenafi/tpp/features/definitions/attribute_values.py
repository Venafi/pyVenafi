from __future__ import annotations

from pyvenafi.tpp.api.websdk.enums.config import (
    ApplicationAttributeValues,
    CertificateAttributeValues,
    CertificateAuthorityAttributeValues,
    ClientGroupsAttributeValues,
    ClientWorkAttributeValues,
    CodeSignAttributeValues,
    CustomFieldAttributeValues,
    DeviceAttributeValues,
    DiscoveryAttributeValues,
    IdentityAttributeValues,
    JumpServerAttributeValues,
    PlacementRulesAttributeValues,
    WorkflowAttributeValues,
)

class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues
    CertificateAuthority = CertificateAuthorityAttributeValues
    ClientGroups = ClientGroupsAttributeValues
    ClientWork = ClientWorkAttributeValues
    CodeSign = CodeSignAttributeValues
    CustomField = CustomFieldAttributeValues
    Device = DeviceAttributeValues
    Discovery = DiscoveryAttributeValues
    Identity = IdentityAttributeValues
    JumpServer = JumpServerAttributeValues
    PlacementRules = PlacementRulesAttributeValues
    Workflow = WorkflowAttributeValues
