from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    credential_result: str = PayloadField(alias='CredentialResult', default=None)


class CredentialInfo(PayloadModel):
    class_name: str = PayloadField(alias='ClassName', default=None)
    full_name: str = PayloadField(alias='FullName', default=None)


class NameTypeValue(PayloadModel):
    name: str = PayloadField(alias='Name', default=None)
    type: str = PayloadField(alias='Type', default=None)
    value: str = PayloadField(alias='Value', default=None)
