"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from friendli.types import BaseModel


class FunctionalityTypedDict(TypedDict):
    r"""Functionality of the model."""

    parallel_tool_call: bool
    tool_call: bool
    structured_output: NotRequired[bool]


class Functionality(BaseModel):
    r"""Functionality of the model."""

    parallel_tool_call: bool

    tool_call: bool

    structured_output: Optional[bool] = True
