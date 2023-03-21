from pyvenafi.tpp.api.websdk.enums.config import (
    ApplicationAttributeValues, ClientGroupsAttributeValues, CertificateAttributeValues, CertificateAuthorityAttributeValues,
    DeviceAttributeValues, DiscoveryAttributeValues, CustomFieldAttributeValues, IdentityAttributeValues, WorkflowAttributeValues,
    PlacementRulesAttributeValues, ClientWorkAttributeValues, JumpServerAttributeValues, CodeSignAttributeValues
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
