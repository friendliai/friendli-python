"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .function import Function, FunctionTypedDict
from friendli.types import BaseModel
from typing import Literal
from typing_extensions import TypedDict


FunctionToolType = Literal["function"]
r"""The type of the tool."""


class FunctionToolTypedDict(TypedDict):
    type: FunctionToolType
    r"""The type of the tool."""
    function: FunctionTypedDict


class FunctionTool(BaseModel):
    type: FunctionToolType
    r"""The type of the tool."""

    function: Function
