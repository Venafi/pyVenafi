from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(alias='Code')
    config_result: str = PayloadField(alias='ConfigResult')


class AttributeDefinition(PayloadModel):
    name: str = PayloadField(alias='Name')
    syntax: str = PayloadField(alias='Syntax')


class ClassDefinition(PayloadModel):
    containment_names: list = PayloadField(alias='ContainmentNames')
    containment_sub_names: list = PayloadField(alias='ContainmentSubNames')
    mandatory_names: list = PayloadField(alias='MandatoryNames')
    name: str = PayloadField(alias='Name')
    naming_names: list = PayloadField(alias='NamingNames')
    optional_names: list = PayloadField(alias='OptionalNames')
    super_class_names: list = PayloadField(alias='SuperClassNames')
