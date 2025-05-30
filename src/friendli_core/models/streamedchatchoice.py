"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Literal

from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict

from friendli_core.types import (
    UNSET,
    UNSET_SENTINEL,
    BaseModel,
    Nullable,
    OptionalNullable,
)

from .chatlogprobs import ChatLogprobs, ChatLogprobsTypedDict
from .streamedchatchoicedelta import (
    StreamedChatChoiceDelta,
    StreamedChatChoiceDeltaTypedDict,
)

StreamedChatChoiceFinishReason = Literal["stop", "length", "tool_calls", "null"]
r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
`length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
`tool_calls` means the API has generated tool calls.

"""


class StreamedChatChoiceTypedDict(TypedDict):
    delta: StreamedChatChoiceDeltaTypedDict
    index: int
    r"""The index of the choice in the list of generated choices."""
    finish_reason: NotRequired[Nullable[StreamedChatChoiceFinishReason]]
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """
    logprobs: NotRequired[Nullable[ChatLogprobsTypedDict]]


class StreamedChatChoice(BaseModel):
    delta: StreamedChatChoiceDelta

    index: int
    r"""The index of the choice in the list of generated choices."""

    finish_reason: OptionalNullable[StreamedChatChoiceFinishReason] = UNSET
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """

    logprobs: OptionalNullable[ChatLogprobs] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["finish_reason", "logprobs"]
        nullable_fields = ["finish_reason", "logprobs"]
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
