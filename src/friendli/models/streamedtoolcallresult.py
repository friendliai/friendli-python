"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .functionresult import FunctionResult, FunctionResultTypedDict
from friendli.types import BaseModel
from friendli.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class StreamedToolCallResultTypedDict(TypedDict):
    function: FunctionResultTypedDict
    id: str
    r"""The ID of the tool call."""
    index: int
    r"""The index of tool call being generated."""
    type: Literal["function"]
    r"""The type of the tool."""


class StreamedToolCallResult(BaseModel):
    function: FunctionResult

    id: str
    r"""The ID of the tool call."""

    index: int
    r"""The index of tool call being generated."""

    TYPE: Annotated[
        Annotated[Literal["function"], AfterValidator(validate_const("function"))],
        pydantic.Field(alias="type"),
    ] = "function"
    r"""The type of the tool."""
