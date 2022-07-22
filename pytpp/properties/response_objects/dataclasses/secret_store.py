from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    secret_store_result: str = PayloadField(alias='SecretStoreResult', default=None)


class TypedNameValues(PayloadModel):
    name: str = PayloadField(alias='Name', default=None)
    type: str = PayloadField(alias='Type', default=None)
    value: str = PayloadField(alias='Value', default=None)
