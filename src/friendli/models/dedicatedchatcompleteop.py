"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dedicatedchatcompletionbody import (
    DedicatedChatCompletionBody,
    DedicatedChatCompletionBodyTypedDict,
)
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from friendli.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class DedicatedChatCompleteRequestTypedDict(TypedDict):
    dedicated_chat_completion_body: DedicatedChatCompletionBodyTypedDict
    x_friendli_team: NotRequired[Nullable[str]]
    r"""ID of team to run requests as (optional parameter)."""


class DedicatedChatCompleteRequest(BaseModel):
    dedicated_chat_completion_body: Annotated[
        DedicatedChatCompletionBody,
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
