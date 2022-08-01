from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(alias='Code')
    secret_store_result: str = PayloadField(alias='SecretStoreResult')


class TypedNameValues(PayloadModel):
    name: str = PayloadField(alias='Name')
    type: str = PayloadField(alias='Type')
    value: str = PayloadField(alias='Value')
