"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from friendli.types import BaseModel
from typing_extensions import TypedDict


class ToolStatusErrorTypedDict(TypedDict):
    msg: str
    r"""The message of error."""
    type: str
    r"""The type of error encountered during the tool's execution."""


class ToolStatusError(BaseModel):
    msg: str
    r"""The message of error."""

    type: str
    r"""The type of error encountered during the tool's execution."""
