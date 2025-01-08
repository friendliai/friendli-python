"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .streamedcompletionschoice import (
    StreamedCompletionsChoice,
    StreamedCompletionsChoiceTypedDict,
)
from .usage import Usage, UsageTypedDict
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from friendli.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class StreamedCompletionDataTypedDict(TypedDict):
    choices: List[StreamedCompletionsChoiceTypedDict]
    created: int
    r"""The Unix timestamp (in seconds) for when the token sampled."""
    id: str
    r"""A unique ID of the completion."""
    object: Literal["text_completion"]
    r"""The object type, which is always set to `text_completion`."""
    usage: NotRequired[Nullable[UsageTypedDict]]


class StreamedCompletionData(BaseModel):
    choices: List[StreamedCompletionsChoice]

    created: int
    r"""The Unix timestamp (in seconds) for when the token sampled."""

    id: str
    r"""A unique ID of the completion."""

    OBJECT: Annotated[
        Annotated[
            Literal["text_completion"],
            AfterValidator(validate_const("text_completion")),
        ],
        pydantic.Field(alias="object"),
    ] = "text_completion"
    r"""The object type, which is always set to `text_completion`."""

    usage: OptionalNullable[Usage] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["usage"]
        nullable_fields = ["usage"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
