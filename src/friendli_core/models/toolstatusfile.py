"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations

from typing_extensions import TypedDict

from friendli_core.types import BaseModel


class ToolStatusFileTypedDict(TypedDict):
    name: str
    r"""The name of the file generated by the tool's execution."""
    url: str
    r"""URL of the file generated by the tool's execution."""


class ToolStatusFile(BaseModel):
    name: str
    r"""The name of the file generated by the tool's execution."""

    url: str
    r"""URL of the file generated by the tool's execution."""
