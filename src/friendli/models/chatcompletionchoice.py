"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .logprobs import Logprobs, LogprobsTypedDict
from friendli.types import BaseModel
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


ChatCompletionChoiceType = Literal["function"]
r"""The type of the tool."""


class ChatCompletionChoiceFunctionTypedDict(TypedDict):
    name: str
    r"""The name of the function to call."""
    arguments: str
    r"""The arguments for calling the function, generated by the model in JSON format.
    Ensure to validate these arguments in your code before invoking the function since the model may not always produce valid JSON.

    """


class ChatCompletionChoiceFunction(BaseModel):
    name: str
    r"""The name of the function to call."""

    arguments: str
    r"""The arguments for calling the function, generated by the model in JSON format.
    Ensure to validate these arguments in your code before invoking the function since the model may not always produce valid JSON.

    """


class ChatCompletionChoiceToolCallsTypedDict(TypedDict):
    id: str
    r"""The ID of the tool call."""
    type: ChatCompletionChoiceType
    r"""The type of the tool."""
    function: ChatCompletionChoiceFunctionTypedDict


class ChatCompletionChoiceToolCalls(BaseModel):
    id: str
    r"""The ID of the tool call."""

    type: ChatCompletionChoiceType
    r"""The type of the tool."""

    function: ChatCompletionChoiceFunction


class ChatCompletionChoiceMessageTypedDict(TypedDict):
    role: str
    r"""Role of the generated message author, in this case `assistant`."""
    content: NotRequired[str]
    r"""The contents of the assistant message."""
    tool_calls: NotRequired[List[ChatCompletionChoiceToolCallsTypedDict]]


class ChatCompletionChoiceMessage(BaseModel):
    role: str
    r"""Role of the generated message author, in this case `assistant`."""

    content: Optional[str] = None
    r"""The contents of the assistant message."""

    tool_calls: Optional[List[ChatCompletionChoiceToolCalls]] = None


class ChatCompletionChoiceTypedDict(TypedDict):
    index: int
    r"""The index of the choice in the list of generated choices."""
    message: ChatCompletionChoiceMessageTypedDict
    finish_reason: str
    r"""Termination condition of the generation. `stop` means the API returned the full chat completion generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """
    logprobs: NotRequired[LogprobsTypedDict]
    r"""Log probability information for the choice."""


class ChatCompletionChoice(BaseModel):
    index: int
    r"""The index of the choice in the list of generated choices."""

    message: ChatCompletionChoiceMessage

    finish_reason: str
    r"""Termination condition of the generation. `stop` means the API returned the full chat completion generated by the model without running into any limits.
    `length` means the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    `tool_calls` means the API has generated tool calls.

    """

    logprobs: Optional[Logprobs] = None
    r"""Log probability information for the choice."""
