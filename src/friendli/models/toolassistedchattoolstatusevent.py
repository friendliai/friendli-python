"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


Name = Literal[
    "math:calculator",
    "math:statistics",
    "math:calendar",
    "web:search",
    "web:url",
    "code:python-interpreter",
    "file:text",
]
r"""The name of the built-in tool."""

Status = Literal["STARTED", "UPDATING", "ENDED", "ERRORED"]
r"""Indicates the current execution status of the tool."""


class ToolAssistedChatToolStatusEventParametersTypedDict(TypedDict):
    name: str
    r"""The name of the tool’s function parameter."""
    value: str
    r"""The value of the tool’s function parameter."""


class ToolAssistedChatToolStatusEventParameters(BaseModel):
    name: str
    r"""The name of the tool’s function parameter."""

    value: str
    r"""The value of the tool’s function parameter."""


class FilesTypedDict(TypedDict):
    name: str
    r"""The name of the file generated by the tool’s execution."""
    url: str
    r"""URL of the file generated by the tool’s execution."""


class Files(BaseModel):
    name: str
    r"""The name of the file generated by the tool’s execution."""

    url: str
    r"""URL of the file generated by the tool’s execution."""


class ErrorTypedDict(TypedDict):
    type: str
    r"""The type of error encountered during the tool’s execution."""
    msg: str
    r"""The message of error."""


class Error(BaseModel):
    type: str
    r"""The type of error encountered during the tool’s execution."""

    msg: str
    r"""The message of error."""


class ToolAssistedChatToolStatusEventTypedDict(TypedDict):
    tool_call_id: str
    r"""The ID of the tool call."""
    name: Name
    r"""The name of the built-in tool."""
    status: Status
    r"""Indicates the current execution status of the tool."""
    parameters: List[ToolAssistedChatToolStatusEventParametersTypedDict]
    result: str
    r"""The output from the tool’s execution."""
    timestamp: float
    r"""The Unix timestamp (in seconds) for when the event occurred."""
    files: NotRequired[List[FilesTypedDict]]
    message: NotRequired[str]
    r"""Message generated by the tool’s execution."""
    error: NotRequired[ErrorTypedDict]


class ToolAssistedChatToolStatusEvent(BaseModel):
    tool_call_id: str
    r"""The ID of the tool call."""

    name: Name
    r"""The name of the built-in tool."""

    status: Status
    r"""Indicates the current execution status of the tool."""

    parameters: List[ToolAssistedChatToolStatusEventParameters]

    result: str
    r"""The output from the tool’s execution."""

    timestamp: float
    r"""The Unix timestamp (in seconds) for when the event occurred."""

    files: Optional[List[Files]] = None

    message: Optional[str] = None
    r"""Message generated by the tool’s execution."""

    error: Optional[Error] = None
