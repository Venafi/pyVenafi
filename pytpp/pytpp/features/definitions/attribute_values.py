from pytpp.properties.config import (
    ApplicationAttributeValues, ClientGroupsAttributeValues, CertificateAttributeValues, DeviceAttributeValues,
    DiscoveryAttributeValues, CustomFieldAttributeValues, IdentityAttributeValues, WorkflowAttributeValues,
    PlacementRulesAttributeValues, ClientWorkAttributeValues,
)

class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues
    ClientGroups = ClientGroupsAttributeValues
    ClientWork = ClientWorkAttributeValues
    CustomField = CustomFieldAttributeValues
    Device = DeviceAttributeValues
    Discovery = DiscoveryAttributeValues
    Identity = IdentityAttributeValues
    PlacementRules = PlacementRulesAttributeValues
    Workflow = WorkflowAttributeValues
