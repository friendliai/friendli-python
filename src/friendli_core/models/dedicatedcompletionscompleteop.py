"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from friendli_core.types import (
    UNSET,
    UNSET_SENTINEL,
    BaseModel,
    Nullable,
    OptionalNullable,
)
from friendli_core.utils import FieldMetadata, HeaderMetadata, RequestMetadata

from .dedicatedcompletionsbody import (
    DedicatedCompletionsBody,
    DedicatedCompletionsBodyTypedDict,
)


class DedicatedCompletionsCompleteRequestTypedDict(TypedDict):
    dedicated_completions_body: DedicatedCompletionsBodyTypedDict
    x_friendli_team: NotRequired[Nullable[str]]
    r"""ID of team to run requests as (optional parameter)."""


class DedicatedCompletionsCompleteRequest(BaseModel):
    dedicated_completions_body: Annotated[
        DedicatedCompletionsBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_friendli_team: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="X-Friendli-Team"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = UNSET
    r"""ID of team to run requests as (optional parameter)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["X-Friendli-Team"]
        nullable_fields = ["X-Friendli-Team"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
