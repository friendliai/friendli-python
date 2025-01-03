"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


AssistantMessageRole = Literal["assistant"]
r"""The role of the messages author."""

AssistantMessageType = Literal["function"]
r"""The type of tool call."""


class AssistantMessageFunctionTypedDict(TypedDict):
    r"""The function specification"""

    name: str
    r"""The name of function"""
    arguments: str
    r"""The arguments of function in JSON schema format to call the function."""


class AssistantMessageFunction(BaseModel):
    r"""The function specification"""

    name: str
    r"""The name of function"""

    arguments: str
    r"""The arguments of function in JSON schema format to call the function."""


class ToolCallsTypedDict(TypedDict):
    id: str
    r"""The ID of tool call."""
    type: AssistantMessageType
    r"""The type of tool call."""
    function: AssistantMessageFunctionTypedDict
    r"""The function specification"""


class ToolCalls(BaseModel):
    id: str
    r"""The ID of tool call."""

    type: AssistantMessageType
    r"""The type of tool call."""

    function: AssistantMessageFunction
    r"""The function specification"""


class AssistantMessageTypedDict(TypedDict):
    role: AssistantMessageRole
    r"""The role of the messages author."""
    content: NotRequired[str]
    r"""The content of assistant message. Required unless `tool_calls` is specified."""
    name: NotRequired[str]
    r"""The name for the participant to distinguish between participants with the same role."""
    tool_calls: NotRequired[List[ToolCallsTypedDict]]


class AssistantMessage(BaseModel):
    role: AssistantMessageRole
    r"""The role of the messages author."""

    content: Optional[str] = None
    r"""The content of assistant message. Required unless `tool_calls` is specified."""

    name: Optional[str] = None
    r"""The name for the participant to distinguish between participants with the same role."""

    tool_calls: Optional[List[ToolCalls]] = None
