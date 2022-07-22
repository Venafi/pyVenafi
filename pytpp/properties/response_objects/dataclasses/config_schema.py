from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    config_result: str = PayloadField(alias='ConfigResult', default=None)


class AttributeDefinition(PayloadModel):
    name: str = PayloadField(alias='Name', default=None)
    syntax: str = PayloadField(alias='Syntax', default=None)


class ClassDefinition(PayloadModel):
    containment_names: list = PayloadField(alias='ContainmentNames', default=None)
    containment_sub_names: list = PayloadField(alias='ContainmentSubNames', default=None)
    mandatory_names: list = PayloadField(alias='MandatoryNames', default=None)
    name: str = PayloadField(alias='Name', default=None)
    naming_names: list = PayloadField(alias='NamingNames', default=None)
    optional_names: list = PayloadField(alias='OptionalNames', default=None)
    super_class_names: list = PayloadField(alias='SuperClassNames', default=None)
