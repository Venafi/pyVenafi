from pydantic.fields import Undefined
from pydantic import BaseModel, Field
from typing import Any, Optional, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny, NoArgAnyCallable


class PayloadModel(BaseModel): ...


def PayloadField(
        default: Any = None,
        *,
        default_factory: 'Optional[NoArgAnyCallable]' = None,
        alias: str = None,
        title: str = None,
        description: str = None,
        exclude: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None,
        include: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None,
        const: bool = None,
        gt: float = None,
        ge: float = None,
        lt: float = None,
        le: float = None,
        multiple_of: float = None,
        max_digits: int = None,
        decimal_places: int = None,
        min_items: int = None,
        max_items: int = None,
        unique_items: bool = None,
        min_length: int = None,
        max_length: int = None,
        allow_mutation: bool = True,
        regex: str = None,
        discriminator: str = None,
        repr: bool = True,
        **extra: Any,
) -> Any:
    if callable(default_factory):
        default = Undefined
    return Field(
        default=default,
        default_factory=default_factory,
        alias=alias,
        title=title,
        description=description,
        exclude=exclude,
        include=include,
        const=const,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        multiple_of=multiple_of,
        max_digits=max_digits,
        decimal_places=decimal_places,
        min_items=min_items,
        max_items=max_items,
        unique_items=unique_items,
        min_length=min_length,
        max_length=max_length,
        allow_mutation=allow_mutation,
        regex=regex,
        discriminator=discriminator,
        repr=repr,
        **extra
    )
