from pytpp.tools.deprecation import DeprecationMeta
from pytpp.properties.config import (
    ApplicationAttributeValues, ClientGroupsAttributeValues, CertificateAttributeValues, DeviceAttributeValues,
    DiscoveryAttributeValues, CustomFieldAttributeValues, IdentityAttributeValues, WorkflowAttributeValues,
    PlacementRulesAttributeValues, ClientWorkAttributeValues,
)

class AttributeValues(metaclass=DeprecationMeta):
    __deprecation_reason__ = 'Using AttributeValues will be deprecated soon. Please use the ' \
                             'attribute values from "pytpp.attribute_values" instead.'
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
