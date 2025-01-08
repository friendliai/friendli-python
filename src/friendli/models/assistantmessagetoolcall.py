"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assistantmessagetoolcallfunction import (
    AssistantMessageToolCallFunction,
    AssistantMessageToolCallFunctionTypedDict,
)
from friendli.types import BaseModel
from friendli.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AssistantMessageToolCallTypedDict(TypedDict):
    function: AssistantMessageToolCallFunctionTypedDict
    id: str
    r"""The ID of tool call."""
    type: Literal["function"]
    r"""The type of tool call."""


class AssistantMessageToolCall(BaseModel):
    function: AssistantMessageToolCallFunction

    id: str
    r"""The ID of tool call."""

    TYPE: Annotated[
        Annotated[Literal["function"], AfterValidator(validate_const("function"))],
        pydantic.Field(alias="type"),
    ] = "function"
    r"""The type of tool call."""
