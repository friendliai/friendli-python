"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatlogprobs import ChatLogprobs, ChatLogprobsTypedDict
from friendli.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Literal, Optional
from typing_extensions import NotRequired, TypedDict


StreamedChatChoiceType = Literal["function"]
r"""The type of the tool."""


class StreamedChatChoiceFunctionTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the function to call."""
    arguments: NotRequired[str]
    r"""The arguments for calling the function, generated by the model in JSON format.
    Ensure to validate these arguments in your code before invoking the function since the model may not always produce valid JSON.

    """


class StreamedChatChoiceFunction(BaseModel):
    name: Optional[str] = None
    r"""The name of the function to call."""

    arguments: Optional[str] = None
    r"""The arguments for calling the function, generated by the model in JSON format.
    Ensure to validate these arguments in your code before invoking the function since the model may not always produce valid JSON.

    """


class StreamedChatChoiceToolCallsTypedDict(TypedDict):
    index: NotRequired[int]
    r"""The index of tool call being generated."""
    id: NotRequired[str]
    r"""The ID of the tool call."""
    type: NotRequired[StreamedChatChoiceType]
    r"""The type of the tool."""
    function: NotRequired[StreamedChatChoiceFunctionTypedDict]


class StreamedChatChoiceToolCalls(BaseModel):
    index: Optional[int] = None
    r"""The index of tool call being generated."""

    id: Optional[str] = None
    r"""The ID of the tool call."""

    type: Optional[StreamedChatChoiceType] = None
    r"""The type of the tool."""

    function: Optional[StreamedChatChoiceFunction] = None


class DeltaTypedDict(TypedDict):
    role: NotRequired[str]
    r"""Role of the generated message author, in this case `assistant`."""
    content: NotRequired[Nullable[str]]
    r"""The contents of the assistant message."""
    tool_calls: NotRequired[Nullable[StreamedChatChoiceToolCallsTypedDict]]


class Delta(BaseModel):
    role: Optional[str] = None
    r"""Role of the generated message author, in this case `assistant`."""

    content: OptionalNullable[str] = UNSET
    r"""The contents of the assistant message."""

    tool_calls: OptionalNullable[StreamedChatChoiceToolCalls] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["role", "content", "tool_calls"]
        nullable_fields = ["content", "tool_calls"]
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


StreamedChatChoiceFinishReason = Literal["stop", "length", "tool_calls", "null"]
r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
`length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
`tool_calls` means the API has generated tool calls.

"""


class StreamedChatChoiceTypedDict(TypedDict):
    index: NotRequired[int]
    r"""The index of the choice in the list of generated choices."""
    delta: NotRequired[DeltaTypedDict]
    finish_reason: NotRequired[Nullable[StreamedChatChoiceFinishReason]]
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """
    logprobs: NotRequired[Nullable[ChatLogprobsTypedDict]]
    r"""Log probability information for the choice."""


class StreamedChatChoice(BaseModel):
    index: Optional[int] = None
    r"""The index of the choice in the list of generated choices."""

    delta: Optional[Delta] = None

    finish_reason: OptionalNullable[StreamedChatChoiceFinishReason] = UNSET
    r"""Termination condition of the generation. `stop` means the API returned the full chat completions generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """

    logprobs: OptionalNullable[ChatLogprobs] = UNSET
    r"""Log probability information for the choice."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["index", "delta", "finish_reason", "logprobs"]
        nullable_fields = ["finish_reason", "logprobs"]
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
